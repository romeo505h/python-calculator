# Python Calculator

A command-line calculator built with Python.

It supports several arithmetic operations, handles invalid input and division by zero, and allows multiple calculations in one session.

## Features

* Supports whole numbers and decimal numbers
* Addition, subtraction, multiplication, and division
* Power calculations with `**`
* Modulus with `%`
* Floor division with `//`
* Handles invalid number input
* Handles division by zero
* Allows multiple calculations in one session

## Supported Operators

| Operator | Operation      |
| -------- | -------------- |
| `+`      | Addition       |
| `-`      | Subtraction    |
| `*`      | Multiplication |
| `/`      | Division       |
| `**`     | Power          |
| `%`      | Modulus        |
| `//`     | Floor division |

## Concepts Used

This project uses several Python concepts, including:

* Functions and parameters
* Return values
* `while` loops
* Conditional statements
* Boolean logic
* Input validation
* `try` / `except`
* `ValueError`
* `ZeroDivisionError`
* Multiple return values
* Tuples
* String methods such as `.lower()`
* Membership testing with `in`

The program separates number input and calculation into reusable functions. The `calculator()` function returns both a result and an error value, which keeps the calculation logic separate from the user interaction.

## Error Handling

Invalid numerical input is handled with `ValueError`, allowing the program to ask for another number instead of stopping.

Division by zero is handled with `ZeroDivisionError` and returned to the main program as an error value.

## How to Run

Make sure Python is installed on your computer.

Clone the repository:

```bash
git clone https://github.com/romeo505h/python-calculator.git
```

Navigate to the project:

```bash
cd python-calculator
```

Run the calculator:

```bash
python calculator.py
```

## Example

```text
Welcome to Romina's Calculator!

enter the first number: 12
enter the second number: 4
Choose an operator (+, -, *, /, **, %, //): /

3.0

do you still want to continue? (y/n): n
Goodbye
```

## Future Improvements

Possible improvements for future versions:

* Add an operation menu
* Refactor repeated error handling
* Add more mathematical operations
* Improve the command-line interface
* Add automated tests
* Experiment with dictionaries for operation handling
* Improve the overall project structure
