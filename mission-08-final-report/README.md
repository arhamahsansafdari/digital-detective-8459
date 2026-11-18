# Mission 8 — Final Report and Submission

## 1. Task / objective

The objective of Mission 8 is to review the Digital Detective assignment repository, verify the required mission files and Git history, update the root README, and prepare the repository for final submission.

The final review also includes checking the Mission 6 branch and Pull Request activity.

## 2. Work completed

### Task 8.1 — Repository structure review

The repository contains nine mission folders, numbered from Mission 0 to Mission 8.

| Mission | Topic | Status |
|---|---|---|
| Mission 0 | Repository and workspace setup | Completed |
| Mission 1 | Computer fundamentals and IPOS | Completed |
| Mission 2 | Terminal and file management | Completed |
| Mission 3 | Operating systems | Completed |
| Mission 4 | Python execution and compiler comparison | Completed |
| Mission 5 | Number systems and Python converter | Completed |
| Mission 6 | Git, GitHub, branches and Pull Requests | Completed — PR remains open |
| Mission 7 | Computer networking | Completed, subject to final GitHub verification |
| Mission 8 | Final report and submission | Final verification in progress |

### Task 8.2 — Root README update

The root README includes:

- An introduction to the Digital Detective assignment.
- A mission index linking to the nine mission folders.
- A list of topics explored.
- Instructions for running the Python number converter.
- A summary of learning outcomes.
- Information about Git and GitHub collaboration.

### Task 8.3 — Python program verification

**Hello World program**

File: `mission-04-programs/hello.py`

Command:

```bash
python3 mission-04-programs/hello.py
```

Expected output:

```text
Hello from Python
```

**Number converter**

File: `mission-05-numbers-data/number_converter.py`

Command:

```bash
python3 mission-05-numbers-data/number_converter.py
```

Expected test results:

| Decimal | Binary | Hexadecimal |
|---|---|---|
| 13 | `0b1101` | `0xd` |
| 25 | `0b11001` | `0x19` |
| 31 | `0b11111` | `0x1f` |

### Task 8.4 — Git and GitHub verification

Git was used to track changes and maintain separate commits for each mission.

The following commands were used to inspect the repository:

```bash
git status
git log --oneline --all
git branch -a
```

**Mission 6 branch and Pull Request**

- Source branch: `update-about`
- Target branch: `main`
- Pull Request purpose: Add a My Learning section to the root README.
- Pull Request status: Open — not merged.
- Reason: The assignment instructs students to merge the PR only when requested by the instructor.

The Pull Request remains available for review on GitHub.

The final Mission 8 documentation is prepared on the `main` branch without merging `update-about`.

### Task 8.5 — Final submission preparation

Repository URL:

https://github.com/arhamahsansafdari/digital-detective-8459

The repository is intended to contain all required mission files, Python programs, README documentation and Git history.

The final submission is the public GitHub repository URL.

## 3. Commands / tools used

| Command / tool | Purpose |
|---|---|
| `pwd` | Display the current directory. |
| `find` | Inspect the repository structure. |
| `git status` | Check repository changes. |
| `git branch -a` | Display local and remote branches. |
| `git log --oneline --all` | Inspect commit history across branches. |
| `git add` | Stage documentation changes. |
| `git commit` | Record final documentation changes. |
| `git push` | Publish commits to GitHub. |
| `python3` | Execute and test Python programs. |
| VS Code | Edit Markdown documentation. |
| GitHub | Verify the public repository and Pull Request. |

## 4. My understanding

Through this assignment, I developed a basic understanding of computer hardware, software and operating systems.

I learned how to use Terminal commands to navigate directories and manage files.

I also practised Python programming and number-system conversions.

Git and GitHub helped me understand how developers record changes and collaborate using branches and Pull Requests.

I learned that a Pull Request can remain open for review without being merged.

Finally, I explored networking concepts, including DNS, routers, protocols and client-server communication.

## 5. Difficulties faced

The main concepts requiring attention during the final review were understanding the relationship between local and remote branches, checking Git commit history, and distinguishing an open Pull Request from a merged Pull Request.

It was also important to verify that the final documentation was prepared on the correct branch.

## 6. How I resolved them

I used `git branch -a` to review branches and `git log --oneline --all` to inspect the repository's commit history.

I learned that creating a Pull Request does not automatically merge its changes.

I kept the `update-about` Pull Request open and prepared the final documentation on `main`.

I also reviewed the repository structure and Python execution commands to understand how to verify the project before submission.

## 7. Evidence / files

The repository contains:

- A root README.
- Separate README documentation for Missions 0–8.
- `mission-04-programs/hello.py`.
- `mission-05-numbers-data/number_converter.py`.
- Git commit history.
- The `update-about` branch.
- An open Pull Request from `update-about` into `main`.

Repository:

https://github.com/arhamahsansafdari/digital-detective-8459

The Pull Request remains unmerged as required by the current instructor instructions.

## 8. Commit details

**Repository:** https://github.com/arhamahsansafdari/digital-detective-8459

**Final documentation branch:** `main`

**Mission 6 PR status:** Open — not merged

**Final commit message:**

`Complete final report with open Pull Request`

**Files to commit:**

- `README.md`
- `mission-08-final-report/README.md`


