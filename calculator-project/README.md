# Calculator Project

A simple calculator project built with Python using the uv packaging tool. This project demonstrates basic arithmetic operations: addition, subtraction, multiplication, and division.

## Features

- Addition (`add` function)
- Subtraction (`subtract` function)
- Multiplication (`multiply` function)
- Division (`divide` function) with zero-division error handling
- A utility function (`calculate_all_operations`) that performs all operations at once

## Usage

To run the calculator demonstration:

```bash
uv run main.py
```

To run the tests:

```bash
uv run test_calc.py
```

## Functions

- `add(a, b)`: Returns the sum of a and b
- `subtract(a, b)`: Returns the difference of a and b (a - b)
- `multiply(a, b)`: Returns the product of a and b
- `divide(a, b)`: Returns the quotient of a and b (a / b), raises ZeroDivisionError if b is 0
- `calculate_all_operations(a, b)`: Returns a dictionary with results of all operations

## Examples

The main module demonstrates calculations with example numbers and shows:
- Basic arithmetic operations
- Error handling for division by zero
- Usage of the calculate_all_operations function