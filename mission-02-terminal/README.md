# Mission 2 — Become Comfortable with the Terminal

## 1. Task / objective

The objective of Mission 2 is to learn how to use the Command-Line Interface (CLI) to interact with my computer.

In this mission, I practised navigating directories, listing files, creating and modifying files, copying and renaming files, and displaying file contents using Terminal commands.

I also explored command flags, pipes, output redirection, and the purpose of package managers.

All file-management practice was carried out inside my assignment repository to avoid modifying important system files.

## 2. Work completed

### Task 2.1 — Explore basic Terminal operations

I opened Terminal on my Mac and navigated to my assignment repository.

**Project directory:** `~/Desktop/digital-detective-8459`

I performed the following operations:

| Operation / command name | What it does | Example observation |
|---|---|---|
| Current-directory display — `pwd` | Displays the absolute path of the current working directory. | Showed the location of my assignment repository. |
| Directory listing — `ls` | Lists files and folders in the current directory. | Displayed my mission folders and README file. |
| Detailed listing — `ls -l` | Displays file permissions, ownership, size and modification information. | Showed more details than the normal listing. |
| Change directory — `cd ..` | Moves to the parent directory. | Changed my working directory from the project folder to Desktop. |
| Create directory — `mkdir` | Creates a new directory. | Created a folder named `terminal-practice`. |
| Create empty file — `touch` | Creates an empty file if it does not already exist. | Created `sample.txt` inside my practice folder. |
| Copy file — `cp` | Creates a copy of an existing file. | Created `sample-copy.txt` while keeping the original file. |
| Move / rename file — `mv` | Moves or renames a file. | Renamed `sample-copy.txt` to `renamed-sample.txt`. |
| Display file contents — `cat` | Displays the contents of a text file. | Produced no text because `sample.txt` was empty. |

**Commands practised:**

```bash
pwd
ls
ls -l
cd ..
cd ~/Desktop/digital-detective-8459
mkdir -p mission-02-terminal/terminal-practice
touch mission-02-terminal/terminal-practice/sample.txt
cp mission-02-terminal/terminal-practice/sample.txt mission-02-terminal/terminal-practice/sample-copy.txt
mv mission-02-terminal/terminal-practice/sample-copy.txt mission-02-terminal/terminal-practice/renamed-sample.txt
cat mission-02-terminal/terminal-practice/sample.txt
```

**What I learned:**

I learned that Terminal commands allow me to perform file-management tasks without using the graphical file manager. Each command has a specific purpose, and the current working directory affects how relative paths are interpreted.

### Task 2.2 — Practise file changes safely

For this task, I worked inside the `mission-02-terminal/terminal-practice` directory.

I created a text file named `notes.txt`, added two lines of text, displayed its contents, created a backup and renamed the backup.

**Commands used:**

```bash
cd mission-02-terminal/terminal-practice

echo "This is my first line." > notes.txt
echo "This is my second line." >> notes.txt

cat notes.txt

cp notes.txt notes-backup.txt
mv notes-backup.txt notes-saved.txt

ls -l
```

**Expected contents of `notes.txt`:**

```text
This is my first line.
This is my second line.
```

**Questions and answers**

**Q1. What is the difference between replacing a file's contents and adding text to the end?**

The `>` operator redirects output into a file and replaces its previous contents. The `>>` operator appends new output to the end of the file without removing the existing text.

For example, I used `>` to write the first line and `>>` to add the second line. Both lines were visible when I displayed the file.

**Q2. What is the difference between copying a file and moving a file?**

Copying a file creates another file containing the same data while keeping the original file.

Moving a file changes its location or name. When I renamed the backup using `mv`, the old backup filename was no longer present.

**Q3. What information does the current-directory display provide?**

The `pwd` command displays the absolute path of the directory in which I am currently working.

It helps me confirm my location before creating or modifying files.

**Q4. Why is a directory-listing operation useful?**

The `ls` command helps me see the files and folders available in a directory.

It is useful for checking whether a file was created, copied, renamed or saved successfully.

### Task 2.3 — Understand flags and pipes

A flag, also called an option, modifies the behaviour of a command.

I compared different versions of the `ls` command.

| Command | Purpose | Example observation |
|---|---|---|
| `ls` | Displays a normal directory listing. | Showed visible filenames. |
| `ls -l` | Displays a detailed listing. | Included permissions, sizes and modification information. |
| `ls -la` | Displays a detailed listing including hidden entries. | Included entries such as `.` and `..`. |
| `ls -lah` | Displays detailed information with human-readable sizes. | Used readable size units where appropriate. |
| `ls -l \| head -n 5` | Displays only the first five lines of the detailed listing. | Showed a shortened version of the listing. |

**Explanation of flags:**

- `-l` enables the long-listing format.
- `-a` includes hidden files and directory entries.
- `-h` displays file sizes in human-readable units when used with the long listing.

**What is a pipe?**

A pipe is represented by the `|` symbol.

It connects two commands by sending the standard output of the first command to the standard input of the second command.

**Example:**

```bash
ls -l | head -n 5
```

Here, `ls -l` generates a detailed directory listing.

The `|` symbol passes that listing to `head -n 5`.

The `head` command displays only the first five lines it receives.

**What I learned:**

I learned that flags help customise command output, while pipes allow multiple commands to work together.

Pipes are useful when a command produces more information than I need.

### Task 2.4 — Understand package managers

A package manager is a tool that helps users install, update, manage and remove software packages.

On macOS, Homebrew is a commonly used package manager.

**Commands checked:**

```bash
brew --version
brew list
```

**My actual observation:**

[Write whether Homebrew was installed. If installed, record the version and whether the package list appeared. If it was not installed, state that the command was unavailable and that no installation was performed.]

**Why package managers are useful:**

Package managers simplify software management by providing commands to install and maintain applications and development tools. They can help manage software dependencies and updates. This reduces the amount of manual setup required.

No software was installed or uninstalled during this task.

## 3. Commands / tools used

### Tools

- **macOS Terminal:** Used to execute command-line instructions.
- **Visual Studio Code:** Used to edit the README and inspect project files.
- **Git:** Used to track and commit the completed mission.
- **GitHub:** Used to publish the mission documentation.
- **Homebrew:** Investigated as an example of a package manager.

### Command reference

| Command | Meaning / purpose |
|---|---|
| `pwd` | Print the current working directory. |
| `ls` | List directory contents. |
| `ls -l` | Show a detailed directory listing. |
| `ls -la` | Include hidden entries in a detailed listing. |
| `ls -lah` | Display a detailed listing with readable file sizes. |
| `cd` | Change the current directory. |
| `cd ..` | Move to the parent directory. |
| `mkdir` | Create a directory. |
| `touch` | Create an empty file or update timestamps. |
| `cp` | Copy a file or directory with appropriate options. |
| `mv` | Move or rename a file or directory. |
| `cat` | Display or combine file contents. |
| `echo` | Output text. |
| `>` | Redirect output and overwrite the destination file. |
| `>>` | Redirect output and append to the destination file. |
| `\|` | Connect the output of one command to the input of another. |
| `head -n 5` | Display the first five lines of input. |
| `brew --version` | Display the Homebrew version if available. |
| `brew list` | List packages managed by Homebrew if available. |
| `git status` | Check repository changes. |
| `git add` | Stage files for a commit. |
| `git commit` | Record staged changes in Git history. |
| `git push` | Upload local commits to the remote repository. |

## 4. My understanding

Through this mission, I learned how to use the Terminal to perform basic operations on files and directories.

I understood that `pwd` identifies my current working directory, `ls` shows directory contents, and `cd` allows me to move between directories.

I learned how to create folders using `mkdir`, create empty files using `touch`, copy files using `cp`, and rename files using `mv`.

I also understood the difference between overwriting a file using `>` and appending text using `>>`.

Another important concept was the use of flags. I learned that options such as `-l`, `-a` and `-h` modify the output of commands.

I learned that pipes allow commands to be connected so that the output of one command becomes the input of another.

Finally, I understood the basic purpose of package managers and why they are useful for software management.

**The most important lesson from this mission was that I should understand the effect of a command and confirm my working directory before modifying files.**

## 5. Difficulties faced

[Replace this section with difficulties you actually experienced.]

Possible examples, only if applicable:

- Initially, I found it confusing to distinguish between `>` and `>>`.
- I needed practice understanding relative paths and the effect of `cd ..`.
- I was unsure why an empty file displayed no output when using `cat`.

## 6. How I resolved them

[Describe how you actually resolved the difficulties mentioned above.]

For example, I compared the results of writing text with `>` and `>>` and then used `cat` to check the file contents.

I used `pwd` after changing directories to confirm my current location.

I also checked the practice directory using `ls -l` to verify that files had been created and renamed as intended.

## 7. Evidence / files

The following files contain my Mission 2 work:

```text
mission-02-terminal/
├── README.md
└── terminal-practice/
    ├── sample.txt
    ├── renamed-sample.txt
    ├── notes.txt
    └── notes-saved.txt
```

**Evidence description:**

- `README.md` — Contains the command reference, observations, answers and explanations.
- `sample.txt` — Empty file created during command practice.
- `renamed-sample.txt` — Demonstrates file copying and renaming.
- `notes.txt` — Contains two lines added using output redirection.
- `notes-saved.txt` — Backup copy of the text file.

[Include screenshots or additional evidence only if you actually saved them. Remove private usernames, device names and other identifying information.]

## 8. Commit details

**Repository:** https://github.com/arhamahsansafdari/digital-detective-8459

**Branch:** `main`

**Commit message:** `Complete Terminal and file management mission`

**Files committed:** Mission 2 README and practice files.


.]
