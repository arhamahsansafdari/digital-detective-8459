# Mission 5 — Numbers and Data

## 1. Task / objective

The objective of Mission 5 is to understand how computers represent numerical and textual information.

This mission focuses on decimal, binary and hexadecimal number systems, manual number conversions, Python verification, creating a number converter program, and understanding character encoding standards such as ASCII and UTF-8.

The goal is to understand how information is represented using bits and bytes and how programming languages can convert between different number systems.

## 2. Work completed

### Task 5.1 — Convert numbers by hand

A bit is the smallest unit of binary information and can have a value of either 0 or 1. Eight bits form one byte.

Decimal is base 10, binary is base 2, and hexadecimal is base 16.

**Conversion 1: Decimal 13 to binary**

| Division | Quotient | Remainder |
|---|---|---|
| 13 ÷ 2 | 6 | 1 |
| 6 ÷ 2 | 3 | 0 |
| 3 ÷ 2 | 1 | 1 |
| 1 ÷ 2 | 0 | 1 |

Reading the remainders from bottom to top gives `1101`.

**Answer: 13 (decimal) = 1101 (binary)**

**Conversion 2: Decimal 25 to binary**

| Division | Quotient | Remainder |
|---|---|---|
| 25 ÷ 2 | 12 | 1 |
| 12 ÷ 2 | 6 | 0 |
| 6 ÷ 2 | 3 | 0 |
| 3 ÷ 2 | 1 | 1 |
| 1 ÷ 2 | 0 | 1 |

Reading the remainders from bottom to top gives `11001`.

**Answer: 25 (decimal) = 11001 (binary)**

**Conversion 3: Binary 1010 to decimal**

1010 = (1 × 2³) + (0 × 2²) + (1 × 2¹) + (0 × 2⁰)

= 8 + 0 + 2 + 0

= 10

**Answer: 1010 (binary) = 10 (decimal)**

**Conversion 4: Binary 1101 to decimal**

1101 = (1 × 2³) + (1 × 2²) + (0 × 2¹) + (1 × 2⁰)

= 8 + 4 + 0 + 1

= 13

**Answer: 1101 (binary) = 13 (decimal)**

**Conversion 5: Hexadecimal A to decimal**

In hexadecimal, A represents decimal 10.

**Answer: A (hexadecimal) = 10 (decimal)**

**Conversion 6: Hexadecimal 1F to decimal**

1F = (1 × 16¹) + (15 × 16⁰)

= 16 + 15

= 31

**Answer: 1F (hexadecimal) = 31 (decimal)**

**Conversion 7: Binary 1111 to hexadecimal**

1111 = 8 + 4 + 2 + 1

= 15 (decimal)

Decimal 15 is represented by F in hexadecimal.

**Answer: 1111 (binary) = F (hexadecimal)**

### Task 5.2 — Verify conversions using Python

Python provides built-in functions for converting between number systems.

I used the following expressions to check the manual calculations.

| Python expression | Result | Matches manual answer |
|---|---|---|
| `bin(13)` | `0b1101` | Yes |
| `bin(25)` | `0b11001` | Yes |
| `int("1010", 2)` | `10` | Yes |
| `int("1101", 2)` | `13` | Yes |
| `int("A", 16)` | `10` | Yes |
| `int("1F", 16)` | `31` | Yes |
| `hex(int("1111", 2))` | `0xf` | Yes |
| `hex(31)` | `0x1f` | Yes |

The prefix `0b` identifies a binary representation, while `0x` identifies a hexadecimal representation.

The `bin()` function converts an integer into a binary string.

The `hex()` function converts an integer into a hexadecimal string.

The `int()` function converts a string into an integer using the specified base.

### Task 5.3 — Build a number converter

I created a Python program named `number_converter.py`.

The program asks the user to enter a decimal number and displays its binary and hexadecimal representations.

**Python source code:**

```python
# Mission 5 - Number Converter

number = int(input("Enter a positive decimal number: "))

binary_number = bin(number)
hexadecimal_number = hex(number)

print("Decimal:", number)
print("Binary:", binary_number)
print("Hexadecimal:", hexadecimal_number)
```

**Command to run the program:**

```bash
python3 mission-05-numbers-data/number_converter.py
```

**Test cases and expected results:**

| Test number | Binary output | Hexadecimal output |
|---|---|---|
| 13 | `0b1101` | `0xd` |
| 25 | `0b11001` | `0x19` |
| 31 | `0b11111` | `0x1f` |

**Explanation of the program:**

The `input()` function accepts a value typed by the user.

The `int()` function converts the input string into an integer.

The `bin()` function converts the integer into a binary representation.

The `hex()` function converts the integer into a hexadecimal representation.

The `print()` function displays the results in Terminal.

The program demonstrates how Python's built-in functions can perform number-system conversions.

### Task 5.4 — How is text stored?

Computers represent text using character encoding standards.

An encoding standard defines how characters are represented using numerical values and bytes.

**Q1. Find the ASCII decimal codes for uppercase A and lowercase a.**

| Character | ASCII decimal code |
|---|---|
| A | 65 |
| a | 97 |

**Q2. Why does a computer need an encoding standard to store text?**

Computers need character encoding standards because text must be represented as numerical data that can be stored and processed. Shared encoding standards allow different programs and devices to interpret text consistently.

**Q3. Name a character that is not part of basic ASCII.**

The euro symbol `€` is not part of basic ASCII.

UTF-8 can represent this symbol and many other characters from different languages.

**Difference between ASCII and UTF-8:**

ASCII represents a basic set of 128 characters, including English letters, digits, punctuation and control characters.

UTF-8 is a Unicode encoding that supports a much wider range of characters while remaining compatible with ASCII for its basic characters.

## 3. Commands / tools used

| Command / tool | Purpose |
|---|---|
| `cd` | Navigate to the assignment repository. |
| `pwd` | Display the current working directory. |
| `python3 --version` | Check the installed Python version. |
| `python3` | Open Python's interactive environment. |
| `bin()` | Convert an integer to a binary string. |
| `hex()` | Convert an integer to a hexadecimal string. |
| `int()` | Convert input text into an integer using a specified base. |
| `input()` | Accept user input. |
| `print()` | Display output. |
| `ord()` | Find the Unicode code point of a character, including ASCII characters. |
| `touch` | Create the Python file. |
| `python3 mission-05-numbers-data/number_converter.py` | Execute the number converter. |
| Visual Studio Code | Write and edit the Python program and README. |
| Git | Track changes and create a commit. |
| GitHub | Publish the mission files. |

## 4. My understanding

Through this mission, I learned how computers represent numbers using different number systems.

I understood that binary uses only two digits, 0 and 1, while decimal uses ten digits and hexadecimal uses sixteen symbols.

I learned how to convert decimal numbers to binary using repeated division by two and how to convert binary numbers to decimal using powers of two.

I also learned how hexadecimal values are converted into decimal numbers using powers of sixteen.

Another important part of this mission was learning Python's built-in conversion functions.

I understood how `bin()`, `hex()` and `int()` work and how they can be used to verify manual calculations.

By studying the number converter program, I learned how Python accepts user input, stores values in variables and displays converted results.

Finally, I understood why character encoding standards are necessary and how ASCII and UTF-8 represent textual information.

## 5. Difficulties faced

The main concepts that required careful attention were understanding positional values in binary and hexadecimal numbers, remembering the correct order of remainders during decimal-to-binary conversion, and understanding Python's conversion functions.

Another learning challenge was understanding why Python adds prefixes such as `0b` and `0x` to converted numbers.

It was also important to understand why the value returned by `input()` must be converted into an integer before performing numerical conversions.

## 6. How I resolved them

I studied the positional-value method and practised breaking binary numbers into powers of two.

For decimal-to-binary conversions, I used repeated division by two and read the remainders from bottom to top.

For hexadecimal conversions, I learned that the symbols A through F represent decimal values from 10 through 15.

I compared manual calculations with Python's built-in conversion functions to understand the results.

I also examined the number converter program line by line to understand how input, integer conversion, binary conversion, hexadecimal conversion and output work together.

These steps helped me understand number representation and conversion more clearly.

## 7. Evidence / files

The Mission 5 folder contains:

```text
mission-05-numbers-data/
├── README.md
└── number_converter.py
```

**README.md**

Contains the mission objectives, seven manual number conversions, Python verification results, number converter explanation, test cases, text-encoding notes and learning reflections.

**number_converter.py**

Contains the Python program that accepts a decimal integer and displays its binary and hexadecimal representations.

The program can be executed using:

```bash
python3 mission-05-numbers-data/number_converter.py
```

The three documented test values are 13, 25 and 31.

## 8. Commit details

**GitHub repository:** https://github.com/arhamahsansafdari/digital-detective-8459

**Branch:** `main`

**Planned commit message:** `Complete number systems and Python converter mission`

**Files to commit:**

- `mission-05-numbers-data/README.md`
- `mission-05-numbers-data/number_converter.py`

The mission is ready for final verification after the program has been tested, the documentation has been reviewed, and the files have been committed and pushed to GitHub.
