# Lab 4: Git & GitHub - notes

**Question 1.** `--global` saves the setting in my user-wide config file (`~/.gitconfig`), so it applies to every repository on this computer. Without it, the name and email would be saved only in the current repository's `.git/config` and would apply to that repository alone.

**Question 2.** `ls -a` showed a hidden `.git` folder that plain `ls` does not show, because its name starts with a dot. Inside it Git keeps the whole history of the repository: `objects` (the saved file contents and commits), `refs` (branches and tags), `HEAD`, `config`, `index` (the staging area), `hooks` and `logs`.

**Question 3.** Git offered to track about a dozen untracked entries: my lab folders and notebooks, but also lecture slides (`.pptx`), PDFs, a `.zip` and the `.vscode/` editor settings. Those last ones are not code I wrote; they are downloads and editor files that do not belong in the repository.

**Question 4.** After adding `.gitignore`, anything that matches its patterns (`.venv/`, `__pycache__/`, `*.pyc`, `.DS_Store`) no longer appears under "Untracked files". There is one new entry instead: `.gitignore` itself.

**Question 5.** It should be committed. It is part of the project's setup, so anyone who clones the repository (or me on another laptop) gets the same ignore rules and does not accidentally commit `.venv/` or other junk.

**Question 6.** `README.md` moved from "Untracked files" to "Changes to be committed". In the three-places model it moved from the working directory into the staging area (index): it is now ready to go into the next commit, but not committed yet.

**Question 7.** Git printed the branch and the short hash with the message, for example `[main (root-commit) b5d1694] ...`, followed by a summary like `1 file changed, 727 insertions(+)` and a `create mode` line for each new file. My first commit in this repository changed 1 file (`labs/lab5.ipynb`), because I set up the repository after the earlier labs.

**Question 8.** They are the short form of the commit hash (the commit ID), a unique fingerprint Git calculates from the commit's contents. We use it to refer to one exact commit, for example in `git show b5d1694`, `git checkout` or when tagging.

**Question 9.** Edit (change files in the working directory), check with `git status`, stage with `git add`, and save with `git commit`. Then `git log` shows the new commit and the loop starts again.

**Question 10.** GitHub (and most tools) look for a file named `README.md` in the top folder and show it automatically on the repository's front page. That makes it the first thing a visitor reads, so it explains what the project is and who made it, unlike ordinary notes inside a lab folder.

**Question 11.** It signed me in through the browser and saved an access token on my computer, then set itself up as Git's credential helper. When I push over HTTPS, Git gets that token from `gh` instead of asking for a password.

**Question 12.** The front page shows the list of files and, below it, `README.md` rendered as formatted text (headings, bold, lists). GitHub always displays the README from the top folder because it is the project's introduction.

**Question 13.** No. `git log --oneline` shows the same commits with the same hashes; the only difference is that `origin/main` now appears next to my latest commit. Pushing copies commits to GitHub; it does not change my local history.

**Question 14.** A private repository exists on GitHub, but only I and the people I invite (here the TAs) can see it; for everyone else it shows as "not found". A repository that does not exist on GitHub is only on my laptop, so nobody can see it, there is no online backup and nobody can collaborate on it.
