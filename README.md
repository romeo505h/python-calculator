# Python Calculator v1

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
Welcome to my first Python Calculator!
=======
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
* Improve the overall project structure

___________________________________________________________________________________________________________________________________________________________

# Python Calculator V2

A command-line calculator built with Python.

This is the second version of my calculator project. I improved the structure of the original program, added better input validation, calculation history, and a smoother user experience.

## Features

- Addition
- Subtraction
- Multiplication
- Division
- Power with `**`
- Modulus with `%`
- Floor division with `//`
- Supports whole numbers and decimal numbers
- Validates numerical input
- Validates operator input
- Handles division by zero
- Allows multiple calculations in one session
- Keeps a history of calculations
- Displays the calculation history when the user exits
- Includes a command-line menu

## Supported Operators

| Operator | Operation |
|----------|-----------|
| `+` | Addition |
| `-` | Subtraction |
| `*` | Multiplication |
| `/` | Division |
| `**` | Power |
| `%` | Modulus |
| `//` | Floor Division |

## How It Works

Each arithmetic operation has its own function.

The functions are stored in a dictionary where the operator is the key and the corresponding function is the value.

For example:

    operations = {
        '+': add,
        '-': subtract,
        '*': multiply,
        '/': divide,
        '//': floor_divide,
        '%': modulus,
        '**': power
    }

This allows the program to select the correct function based on the operator entered by the user instead of using a long chain of `if` and `elif` statements.

## Input Validation

The calculator uses a separate `get_number()` function to validate numerical input.

If the user enters something that cannot be converted into a number, the program catches the `ValueError` and asks for another input instead of stopping.

The operator also has its own validation function. If the user enters an unsupported operator, the program asks for another operator without making the user enter the numbers again.

I noticed this while testing the program myself. Having to enter the numbers again after making a mistake with the operator felt unnecessary, so I changed the input flow to make the calculator easier to use.

## Error Handling

The calculator uses `try` and `except` to handle errors that could otherwise stop the program.

Invalid numerical input is handled with `ValueError`.

Division by zero is handled with `ZeroDivisionError`.

A failed division attempt is also saved in the calculation history.

## Calculation History

The calculator stores each calculation in a list using `.append()`.

When the user chooses to stop calculating, the program displays the history.

Example:

    -----History-----
    12.0 + 5.0 = 17.0
    20.0 / 4.0 = 5.0
    10.0 * 3.0 = 30.0

## Concepts Practiced

This project gave me practice with:

- Functions
- Parameters and arguments
- Return values
- Dictionaries
- Functions as dictionary values
- Lists
- `.append()`
- `while` loops
- `for` loops
- Conditional statements
- Boolean values
- Membership testing with `in`
- `.lower()`
- f-strings
- Input validation
- `try` / `except`
- `ValueError`
- `ZeroDivisionError`
- Basic command-line interface design
- User experience through testing and iteration

## What Changed From V1

The first version of the calculator used `if` and `elif` statements to determine which operation to perform.

In V2, I changed this structure by using a dictionary to connect each operator with its corresponding function.

I also added:

- A command-line menu
- Separate operator validation
- Calculation history
- Better input validation
- Division-by-zero handling
- Multiple calculations in one session
- Improved interaction based on testing the program

The main goal of V2 was not simply to add more operations, but to make the existing program more organized and easier to use.

## Example

    ------Calculator------
    + Addition
    - Subtraction
    * Multiplication
    / Division
    ** Power
    % Modulus
    // Floor Division
    ----------------------

    Please enter the first number: 12
    Please enter the second number: 4
    Choose an operator: /

    3.0

    Would you like to continue? (y/n): y

    Please enter the first number: 10
    Please enter the second number: 3
    Choose an operator: *

    30.0

    Would you like to continue? (y/n): n

    -----History-----
    12.0 / 4.0 = 3.0
    10.0 * 3.0 = 30.0

    Bye.

## How to Run

Make sure Python is installed on your computer.

Clone the repository:

    git clone https://github.com/romeo505h/python-calculator.git

Navigate to the project folder:

    cd python-calculator

Run the calculator:

    python calculator.py
