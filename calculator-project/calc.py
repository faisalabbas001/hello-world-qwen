"""
Basic arithmetic calculations module.
Contains functions for addition, subtraction, multiplication, and division.
"""


def add(a, b):
    """
    Perform addition of two numbers.
    
    Args:
        a: First number
        b: Second number
    
    Returns:
        The sum of a and b
    """
    return a + b


def subtract(a, b):
    """
    Perform subtraction of two numbers.
    
    Args:
        a: First number
        b: Second number
    
    Returns:
        The difference of a and b (a - b)
    """
    return a - b


def multiply(a, b):
    """
    Perform multiplication of two numbers.
    
    Args:
        a: First number
        b: Second number
    
    Returns:
        The product of a and b
    """
    return a * b


def divide(a, b):
    """
    Perform division of two numbers.
    
    Args:
        a: First number (dividend)
        b: Second number (divisor)
    
    Returns:
        The quotient of a and b (a / b)
    
    Raises:
        ZeroDivisionError: If b is zero
    """
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return a / b


def calculate_all_operations(a, b):
    """
    Calculate all arithmetic operations for two numbers.
    
    Args:
        a: First number
        b: Second number
    
    Returns:
        A dictionary containing all operation results
    """
    return {
        "addition": add(a, b),
        "subtraction": subtract(a, b),
        "multiplication": multiply(a, b),
        "division": divide(a, b) if b != 0 else "Cannot divide by zero"
    }