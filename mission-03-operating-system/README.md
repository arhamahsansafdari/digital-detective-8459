# Mission 3 — Understand the Operating System

## 1. Task / objective

The objective of Mission 3 is to understand how an operating system manages computer hardware, software, files, memory, processes, and security.

In this mission, I explored macOS using Terminal commands to understand the operating system environment, storage information, system activity, running processes, directory paths, and file permissions.

I also studied the six major responsibilities of an operating system and how they help a computer function efficiently.

The main purpose of this mission is to develop a practical understanding of how macOS works behind the graphical user interface.

## 2. Work completed

### Task 3.1 — Explore my operating system

I studied four important types of system information: operating system details, current user identity, storage usage, and running system activity.

The following commands can be used to investigate this information:

```bash
uname -s
sw_vers
whoami
df -h /
top -l 1 -n 5
```

**System information and observations**

| Information explored | What it tells me | Observation / interpretation |
|---|---|---|
| Operating system / system details | Identifies the operating system environment and its version. | macOS uses the Darwin operating-system core. The `sw_vers` command displays the installed macOS version and build information. |
| Current account identity | Identifies the user account executing Terminal commands. | The `whoami` command displays the active account username. The actual username is excluded for privacy. |
| Available and used storage | Shows information about the filesystem's capacity, used space and available space. | The `df -h /` command displays storage information for the filesystem mounted at `/`. |
| System activity snapshot | Shows running processes and system resource usage. | The `top` command provides information about process activity, CPU usage and memory. |

**Explanation of each command**

**1. `uname -s`**

This command displays the kernel's operating-system name. On macOS, it normally displays `Darwin`, which is the Unix-based foundation of macOS.

**2. `sw_vers`**

This command displays information about the installed macOS version, including the product name, product version and build version.

**3. `whoami`**

This command displays the username of the account executing the command. It is useful for understanding which account is active.

**4. `df -h /`**

This command displays storage information for the filesystem mounted at the root directory. The `-h` option makes storage sizes easier to read.

**5. `top -l 1 -n 5`**

This command displays a snapshot of system activity. It helps inspect running processes and resource usage without continuously monitoring the system.

**My understanding**

I learned that the operating system provides tools for examining hardware resources and system activity.

I understood that storage information helps explain how disk space is being used, while process-monitoring tools provide information about applications and background tasks.

I also learned that system commands may display private information, so sensitive details should not be included in a public repository.

### Task 3.2 — Understand processes

A process is a running instance of a program.

When an application is launched, the operating system manages its execution and the resources required for it to operate.

Processes may belong to applications opened by the user or background services required by the operating system.

**Commands studied**

```bash
ps -axo pid,comm | head -n 15
pgrep -fl Safari
```

The `ps` command displays process information.

The `pgrep` command searches for processes matching a specified name or command-line pattern.

**Q1. What is a process?**

A process is an instance of a program that is currently running.

For example, when a user opens a web browser, the operating system manages one or more processes associated with that application.

Each process has execution information and resources managed by the operating system.

**Q2. What does PID mean?**

PID stands for Process Identifier.

A PID is a numerical identifier assigned by the operating system to a process.

It allows the operating system and monitoring tools to distinguish between running processes.

For example, two processes belonging to the same application can have different PIDs.

**Q3. Give two examples of processes that may run on a Mac.**

**Example 1 — Safari**

Safari is a web browser. When it runs, macOS manages processes responsible for browser functionality.

**Example 2 — Visual Studio Code**

Visual Studio Code is a code editor. When it runs, macOS manages its processes and provides the resources needed for editing files and running development tools.

**Difference between a program and a process**

A program is a collection of instructions stored on a computer.

A process is a running instance of a program.

For example, Visual Studio Code installed on a computer is a program. When it is launched and running, it has associated processes.

**My understanding**

I learned that multiple processes can run on a computer at the same time.

The operating system schedules CPU time and manages resources so that different applications can operate.

I also understood that the PID is important for identifying and monitoring individual processes.

### Task 3.3 — Understand paths and permissions

#### Part A — Absolute and relative paths

A path describes the location of a file or directory in a filesystem.

There are two important types of paths: absolute paths and relative paths.

**Commands studied**

```bash
cd ~/Desktop/digital-detective-8459
pwd

cd mission-03-operating-system
pwd

cd ..
pwd
```

**1. Absolute path**

An absolute path specifies a location starting from the filesystem's root directory.

Example:

`/Users/[redacted]/Desktop/digital-detective-8459/mission-03-operating-system`

This path describes the complete location of the Mission 3 folder.

**2. Relative path**

A relative path describes a location in relation to the current working directory.

Example:

`mission-03-operating-system`

When the current directory is the assignment repository, this relative path refers to the Mission 3 folder.

**Comparison**

| Feature | Absolute path | Relative path |
|---|---|---|
| Starting point | Filesystem root | Current working directory |
| Begins with | `/` on macOS | Usually a directory or filename |
| Depends on current location | No | Yes |
| Length | Usually longer | Often shorter |
| Example | `/Users/[redacted]/Desktop/digital-detective-8459/README.md` | `README.md` |

**My understanding**

I learned that the `pwd` command displays the current working directory.

The `cd` command changes the current directory, while `cd ..` moves to its parent.

Absolute paths are useful when specifying complete file locations. Relative paths are convenient when working inside a project because they avoid repeatedly writing the full path.

#### Part B — File permissions

File permissions control which operations different users can perform on files and directories.

The following command displays file details, including permissions:

```bash
ls -l mission-02-terminal/terminal-practice/notes.txt
```

**Example permission string**

```text
-rw-r--r--
```

This is an illustrative permission string, not a recorded result from my computer.

**Explanation**

The first character identifies the file type.

The next three characters describe permissions for the file owner.

The following three describe group permissions, and the final three describe permissions for others.

| Permission | Meaning | Example |
|---|---|---|
| `r` — Read | Allows reading a file's contents. | Opening a text file. |
| `w` — Write | Allows modifying a file's contents. | Editing a README file. |
| `x` — Execute | Allows executing a file when applicable. | Running an executable script. |

**Interpreting the example `-rw-r--r--`**

| User category | Permissions | Meaning |
|---|---|---|
| Owner | `rw-` | Can read and write but does not have execute permission. |
| Group | `r--` | Can read but cannot write or execute. |
| Others | `r--` | Can read but cannot write or execute. |

**My understanding**

I learned that permissions are an important part of operating-system security.

They help control who can access, modify or execute files.

I also understood that the owner, group and other users can have different permissions for the same file.

No file permissions were changed during this mission.

### Task 3.4 — Explain operating-system responsibilities

An operating system performs several responsibilities to manage computer resources and provide services to applications.

| OS responsibility | Explanation | Example |
|---|---|---|
| Process management | The operating system creates, schedules, monitors and manages running processes. | macOS manages Safari and VS Code while both are running. |
| Memory management | The operating system manages RAM allocation and helps applications use memory efficiently. | macOS allocates memory to a Python program when it runs. |
| Device management | The operating system coordinates communication between software and hardware devices. | Keyboard input is delivered to the active application. |
| File management | The operating system organises files and directories and manages file access. | Creating, saving and opening a README file. |
| User interface / shell | The operating system provides interfaces through which users can interact with the computer. | Finder provides a graphical interface, while Terminal provides command-line access through a shell. |
| Security and permissions | The operating system manages user access and helps protect files and system resources. | File permissions restrict reading, writing and execution. |

**Detailed understanding**

**1. Process management**

Process management involves controlling running programs and allocating CPU time.

It helps the computer run multiple applications and background services.

**2. Memory management**

Memory management controls how RAM is allocated and used by applications.

It helps prevent processes from interfering with each other's memory.

**3. Device management**

Device management allows applications to interact with hardware through operating-system services and drivers.

Examples include keyboards, displays, printers and storage devices.

**4. File management**

File management involves creating, organising, reading, writing and deleting files and directories.

The operating system also manages file metadata and access permissions.

**5. User interface and shell**

The operating system provides ways for users to communicate with the computer.

A graphical user interface allows interaction through windows, icons and menus.

A command-line shell allows interaction through typed commands.

**6. Security and permissions**

Security mechanisms help prevent unauthorised access to files and system resources.

Permissions help determine which users can read, modify or execute files.

## 3. Commands / tools used

| Command / tool | Purpose |
|---|---|
| `uname -s` | Displays the kernel's operating-system name. |
| `sw_vers` | Displays macOS version information. |
| `whoami` | Displays the current account username. |
| `df -h /` | Displays storage information for the root filesystem. |
| `top -l 1 -n 5` | Displays a snapshot of system activity. |
| `ps -axo pid,comm` | Displays process identifiers and command names. |
| `pgrep -fl Safari` | Searches for processes matching Safari. |
| `pwd` | Displays the current working directory. |
| `cd` | Changes the working directory. |
| `cd ..` | Moves to the parent directory. |
| `ls -l` | Displays detailed file information and permissions. |
| macOS Terminal | Provides a command-line environment. |
| Visual Studio Code | Used for editing Markdown documentation. |
| Git | Tracks changes and records commits. |
| GitHub | Hosts the public assignment repository. |

## 4. My understanding

Through this mission, I developed a better understanding of how an operating system works.

I learned that macOS manages hardware resources and provides the environment required for applications to run.

I understood that processes are running instances of programs and that each process has an identifier called a PID.

I also learned how Terminal commands can be used to inspect system information, storage usage and running processes.

Another important concept was the difference between absolute and relative paths.

I learned that file permissions control access to files and that read, write and execute permissions have different purposes.

Finally, I understood how process management, memory management, device management, file management, user interfaces and security work together to support the computer.

This mission helped connect the theoretical responsibilities of an operating system with practical computer activities.

## 5. Difficulties faced

The concepts that required the most attention were:

1. Understanding the difference between a program and a process.
2. Interpreting the PID column in process-monitoring output.
3. Understanding absolute and relative paths.
4. Reading permission strings such as `-rw-r--r--`.
5. Understanding the different types of information displayed by system-monitoring commands.

These are learning challenges discussed during the mission, rather than a record of specific Terminal errors.

## 6. How I resolved them

I studied the difference between a stored program and a running process using familiar applications such as Safari and Visual Studio Code.

I learned that PID values identify individual processes.

I compared absolute and relative path examples to understand how directory locations are represented.

I divided the example permission string into file type, owner, group and others to understand how access permissions are organised.

I also reviewed the purposes of commands such as `df`, `ps` and `top` to understand what information each command provides.

These explanations helped me understand the concepts more clearly.

## 7. Evidence / files

**Main documentation**

`mission-03-operating-system/README.md`

This file contains:

- Operating-system information and command explanations.
- Process and PID concepts.
- Absolute and relative path examples.
- File-permission explanations.
- Six operating-system responsibilities.
- Learning reflections and documentation.

**Privacy precautions**

Private usernames, device identifiers, IP addresses and other sensitive system information are excluded from the public documentation.

## 8. Commit details

**Repository:** https://github.com/arhamahsansafdari/digital-detective-8459

**Branch:** `main`

**Planned commit message:** `Document operating system and file management`

**Commit scope:** Mission 3 README and any associated privacy-safe evidence.

**Verification procedure:** After committing, push the changes to GitHub and confirm that the Mission 3 README and commit are visible in the public repository.

**Status:** Commit and push must be verified before Mission 4 begins.
