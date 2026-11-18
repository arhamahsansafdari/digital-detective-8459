
# Mission 6 — Git and GitHub

## Git Workflow Practice

Git helps track changes to files and preserves earlier versions.

I am practising the workflow of checking status, staging a file, committing it, and viewing commit history.

# Mission 6 — Git and GitHub

## 1. Task / objective

The objective of Mission 6 is to understand version control using Git and learn how GitHub supports collaboration.

The mission focuses on checking repository status, staging changes, creating commits, viewing history, creating branches, publishing changes, and opening Pull Requests.

The goal is to understand how developers manage changes to a project while maintaining a reliable record of their work.

## 2. Work completed

### Task 6.1 — Understand the basic Git workflow

Git is a distributed version control system that records changes to files over time.

GitHub is an online platform used to host Git repositories and collaborate on software projects.

I practised the basic Git workflow by updating the Mission 6 README, staging the change, committing it, and examining the commit history.

| Git operation | Command | Explanation |
|---|---|---|
| Check repository status | `git status` | Displays the current state of tracked and untracked files. |
| Stage selected changes | `git add mission-06-git-github/README.md` | Selects the README changes to include in the next commit. |
| Create a commit | `git commit -m "Document basic Git workflow practice"` | Records a snapshot of the staged changes in Git history. |
| View commit history | `git log -5 --oneline` | Displays recent commits with shortened identifiers and messages. |

**Difference between staging and committing**

Staging is the process of selecting changes that should be included in the next commit.

Committing records those staged changes as a new snapshot in the repository's history.

The `git add` command stages changes, while `git commit` records them.

This separation allows developers to review and organise changes before saving them in Git history.

### Task 6.2 — Create and use a branch

A Git branch is a separate line of development that allows changes to be made without immediately modifying another branch.

I created a branch named `update-about` for updating the root README.

**Commands used:**

```bash
git switch -c update-about
git branch
git status
git diff README.md
git add README.md
git commit -m "Add My Learning section to root README"
git push -u origin update-about
```

**Change made**

I added a section titled **My Learning** to the root README.

The section describes three topics explored during the assignment:

1. Terminal commands and file management.
2. Operating-system responsibilities and processes.
3. Python programming and number-system conversions.

**Why branches are useful**

Branches allow developers to work on changes independently.

For example, one developer can improve documentation while another works on program functionality.

The changes can later be reviewed and integrated into the main branch.

### Task 6.3 — Create a Pull Request

A Pull Request is a request to review changes from one branch before merging them into another branch.

The purpose of a Pull Request is to support discussion, code review and controlled integration of changes.

**Pull Request title:**

`Add My Learning section to root README`

**Source branch:** `update-about`

**Target branch:** `main`

**Pull Request description**

The Pull Request proposes adding a My Learning section to the root README.

This section summarises knowledge gained from Terminal operations, operating systems, Python programming and number-system conversions.

**Pull Request review**

The Files changed tab can be used to inspect the proposed README update and verify that only the intended changes are included.

**Pull Request status**

Record the actual PR status here after creating it:

- Open — if the instructor has not requested a merge.
- Merged — if the instructor requested and the merge was completed.

**Pull Request URL**

Add the actual GitHub Pull Request URL after creating it.

**Why Pull Requests are useful**

Pull Requests allow developers to propose changes and request feedback before those changes are integrated.

They provide a visible record of the proposed modification and its review.

They are especially useful when multiple developers contribute to the same repository.

### Task 6.4 — Build a Git command glossary

| Git operation | Command | Explanation |
|---|---|---|
| Initialise a repository | `git init` | Creates a new Git repository. |
| Check status | `git status` | Shows file changes and staging information. |
| Stage changes | `git add filename` | Selects changes for the next commit. |
| Commit changes | `git commit -m "message"` | Records staged changes in repository history. |
| View history | `git log --oneline` | Displays recent commits. |
| Create a branch | `git branch branch-name` | Creates a separate development branch. |
| List branches | `git branch` | Displays local branches. |
| Switch branches | `git switch branch-name` | Changes the active branch. |
| Publish changes | `git push origin branch-name` | Uploads local commits to the remote repository. |
| Retrieve remote changes | `git pull origin main` | Fetches and integrates changes from the remote main branch. |

## 3. Commands / tools used

| Command / tool | Purpose |
|---|---|
| `git status` | Inspect repository changes. |
| `git add` | Stage selected files. |
| `git commit` | Record staged changes. |
| `git log` | Examine commit history. |
| `git branch` | Create or list branches. |
| `git switch` | Switch between branches. |
| `git diff` | Review file changes. |
| `git push` | Publish commits to GitHub. |
| `git pull` | Retrieve and integrate remote changes. |
| VS Code | Edit README documentation. |
| GitHub Pull Requests | Review proposed branch changes. |

## 4. My understanding

Through this mission, I learned how Git tracks changes to project files.

I understood that Git and GitHub serve different purposes. Git manages version history, while GitHub hosts repositories and provides collaboration features.

I learned the difference between staging and committing changes.

I also understood why branches are important for developing changes independently.

By studying Pull Requests, I learned how developers can propose, review and discuss changes before merging them.

This mission helped me understand the basic workflow used in collaborative software development.

## 5. Difficulties faced

The main concepts that required careful attention were understanding the difference between staging and committing, distinguishing local branches from remote branches, and understanding how a Pull Request connects two branches.

Another important learning challenge was understanding the difference between pushing changes and merging changes.

These concepts are closely related but perform different functions in the Git workflow.

## 6. How I resolved them

I studied the Git workflow step by step and examined the purpose of each command.

I learned that `git add` prepares selected changes and `git commit` records them in history.

I also learned that `git push` publishes local commits to a remote repository.

I compared the roles of `main` and `update-about` to understand how branches separate development work.

Finally, I studied the Pull Request workflow to understand how proposed changes can be reviewed before integration.

## 7. Evidence / files

**Repository:**

https://github.com/arhamahsansafdari/digital-detective-8459

**Files involved:**

- `mission-06-git-github/README.md` — Mission 6 documentation.
- `README.md` — Root README updated with the My Learning section.

**GitHub activity to verify:**

- Task 6.1 commit.
- Published `update-about` branch.
- Commit containing the My Learning section.
- Pull Request from `update-about` into `main`.
- Mission 6 documentation commit.

The Pull Request's actual status and URL should be recorded in Task 6.3.

## 8. Commit details

**Repository:** https://github.com/arhamahsansafdari/digital-detective-8459

**Branch for documentation:** `main`

**Task 6.1 commit message:**

`Document basic Git workflow practice`

**Branch update commit message:**

`Add My Learning section to root README`

**Final Mission 6 documentation commit message:**

`Complete Git and GitHub collaboration mission`

**Verification:** Confirm that the commits, branch, Pull Request and final Mission 6 README are visible on GitHub before beginning Mission 7.
