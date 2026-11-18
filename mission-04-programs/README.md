# Mission 4 — How Programs Run

## 1. Task / objective

The objective of Mission 4 is to understand how computer programs are executed and learn the difference between a compiler and an interpreter.

This mission involves creating a simple Python program, running it using Python 3, verifying its output, and comparing compilation with interpretation.

The main goal is to understand how instructions written by a programmer are processed and executed by a computer.

## 2. Work completed

### Task 4.1 — Create and run a Python program

I created a Python file named `hello.py` inside the `mission-04-programs` directory.

**Python code:**

```python
print("Hello from Python")
```

**Command used to run the program:**

```bash
python3 mission-04-programs/hello.py
```

**Program output:**

```text
Hello from Python
```

**My observation:**

When the Python program is executed successfully, the Terminal displays the message `Hello from Python`.

This demonstrates how Python executes instructions written in a source file and produces output.

The program contains a single `print()` statement, which sends the specified text to standard output.

**Explanation of the code:**

The `print()` function is a built-in Python function used to display information.

The text `Hello from Python` is a string because it is enclosed in quotation marks.

When Python executes the `print()` statement, the message appears in Terminal.

### Task 4.2 — Compare compiler and interpreter

| Point | Compiler | Interpreter |
|---|---|---|
| When translation / execution happens | Usually translates source code before the resulting program runs. | Executes program instructions at runtime. |
| Typical output | Translated code, such as object code or machine code. | Results of program execution without necessarily producing a separate executable. |
| One example | GCC compiling C programs. | CPython executing Python bytecode. |
| One advantage | Native compiled programs can execute efficiently. | Convenient for interactive execution, testing and debugging. |

**Difference between a compiler and an interpreter:**

A compiler generally translates source code into another representation before the resulting program is executed, whereas an interpreter executes program instructions during runtime. Compilers can produce native machine code, while interpreters provide an environment for carrying out instructions. GCC is an example of a compiler, while CPython compiles Python source code into bytecode and executes it using a virtual machine. Modern programming-language implementations can combine both approaches.

## 3. Commands / tools used

| Command / tool | Purpose |
|---|---|
| `cd` | Used to navigate to the assignment repository. |
| `pwd` | Displays the current working directory. |
| `python3 --version` | Checks the installed Python version. |
| `touch` | Creates a new file. |
| `python3 mission-04-programs/hello.py` | Executes the Python program. |
| `ls -l` | Displays detailed information about files. |
| `cat` | Displays the contents of a file in Terminal. |
| Visual Studio Code | Used to create and edit the Python program and README. |
| Git | Used to track changes and create commits. |
| GitHub | Used to publish and maintain the assignment repository. |

## 4. My understanding

Through this mission, I learned how to create a Python source file and execute it using Terminal.

I understood that a program is a collection of instructions written to perform a particular task.

I learned that Python provides a runtime environment that processes and executes Python instructions.

I also understood how the `print()` function works and how strings are displayed as output.

Another important concept was the difference between a compiler and an interpreter.

A compiler translates source code into another representation, while an interpreter executes instructions during runtime.

I learned that compilation and interpretation are not completely separate approaches because modern programming-language implementations can use both.

This mission helped me understand the basic process of writing, executing and testing a computer program.

## 5. Difficulties faced

The main learning challenges in this mission were understanding the difference between compilation and interpretation and understanding how Python executes a program.

Initially, it can be confusing to understand why some programming languages are commonly described as compiled while others are described as interpreted.

Another important concept was understanding the purpose of the `python3` command and how it executes instructions stored in a `.py` file.

Understanding the relationship between source code, the Python runtime and program output required careful attention.

## 6. How I resolved them

I studied the basic differences between compilers and interpreters and compared their purposes using examples.

I learned that a compiler translates source code into another representation, while an interpreter executes program instructions during runtime.

I also examined the Python program line by line to understand how the `print()` function works.

By studying the command `python3 mission-04-programs/hello.py`, I understood that Python is instructed to execute the source file located at the specified path.

I used the expected output to understand how a successful execution can be verified.

These activities helped clarify the relationship between source code, execution and output.

## 7. Evidence / files

The following files are included in Mission 4:

```text
mission-04-programs/
├── README.md
└── hello.py
```

**File descriptions:**

**1. README.md**

Contains the mission objectives, Python program explanation, compiler-versus-interpreter comparison, commands, learning reflections and documentation.

**2. hello.py**

Contains the Python program:

```python
print("Hello from Python")
```

The expected output of the program is:

```text
Hello from Python
```

The Python source file provides reproducible evidence of the program. Its execution can be verified using the `python3` command.

## 8. Commit details

**GitHub repository:** https://github.com/arhamahsansafdari/digital-detective-8459

**Branch:** `main`

**Commit message:** `Complete Python program and compiler interpreter comparison`

**Files to commit:**

- `mission-04-programs/README.md`
- `mission-04-programs/hello.py`

**GitHub verification:** The mission is complete after both files have been committed, pushed and verified in the public GitHub repository.
