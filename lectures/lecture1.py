import asyncio
from dataclasses import dataclass
from typing import Any, Awaitable, Callable, Generic, TypeVar


T = TypeVar("T")
Handler = Callable[[T], Awaitable[None]]


class ComponentMeta(type):
	"""Registers every concrete component as soon as its class is created."""
	registry: dict[str, type[Any]] = {}

	def __new__(metaclass, name: str, bases: tuple[type, ...], namespace: dict[str, Any]):
		component = super().__new__(metaclass, name, bases, namespace)
		if name != "Component":
			metaclass.registry[name] = component
		return component


class Component(metaclass=ComponentMeta):
	pass


@dataclass(frozen=True)
class Token(Component):
	value: str


@dataclass(frozen=True)
class RenderedMessage(Component):
	value: str


class EventBus(Generic[T]):
	def __init__(self) -> None:
		self._handlers: list[Handler[T]] = []

	def subscribe(self, handler: Handler[T]) -> None:
		self._handlers.append(handler)

	async def publish(self, event: T) -> None:
		await asyncio.gather(*(handler(event) for handler in self._handlers))


class DependencyContainer:
	def __init__(self) -> None:
		self._providers: dict[type[Any], Callable[[], Any]] = {}

	def register(self, contract: type[T], provider: Callable[[], T]) -> None:
		self._providers[contract] = provider

	def resolve(self, contract: type[T]) -> T:
		return self._providers[contract]()


class TokenSource(Component):
	async def emit(self, bus: EventBus[Token]) -> None:
		for value in (" Hello ", " World! "):
			await bus.publish(Token(value))


class UppercaseMiddleware(Component):
	async def handle(self, token: Token, bus: EventBus[Token]) -> None:
		await bus.publish(Token(token.value.strip()))


class MessageRenderer(Component):
	def __init__(self) -> None:
		self._tokens: list[str] = []

	async def collect(self, token: Token) -> None:
		self._tokens.append(token.value)

	async def render(self, bus: EventBus[RenderedMessage]) -> None:
		await bus.publish(RenderedMessage(" ".join(self._tokens)))


async def print_hello_world() -> None:
	container = DependencyContainer()
	container.register(TokenSource, TokenSource)
	container.register(UppercaseMiddleware, UppercaseMiddleware)
	container.register(MessageRenderer, MessageRenderer)

	token_bus: EventBus[Token] = EventBus()
	rendered_bus: EventBus[RenderedMessage] = EventBus()
	middleware = container.resolve(UppercaseMiddleware)
	renderer = container.resolve(MessageRenderer)

	async def normalize(token: Token) -> None:
		await middleware.handle(token, normalized_bus)

	async def collect(token: Token) -> None:
		await renderer.collect(token)

	async def output(message: RenderedMessage) -> None:
		print(message.value)

	normalized_bus: EventBus[Token] = EventBus()
	token_bus.subscribe(normalize)
	normalized_bus.subscribe(collect)
	rendered_bus.subscribe(output)

	source = container.resolve(TokenSource)
	await source.emit(token_bus)
	await renderer.render(rendered_bus)


if __name__ == "__main__":
	asyncio.run(print_hello_world())
