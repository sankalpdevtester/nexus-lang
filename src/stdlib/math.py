import math

def add(a, b):
    """
    Adds two numbers together.

    Args:
        a (float): The first number.
        b (float): The second number.

    Returns:
        float: The sum of a and b.
    """
    return a + b

def subtract(a, b):
    """
    Subtracts one number from another.

    Args:
        a (float): The first number.
        b (float): The second number.

    Returns:
        float: The difference between a and b.
    """
    return a - b

def multiply(a, b):
    """
    Multiplies two numbers together.

    Args:
        a (float): The first number.
        b (float): The second number.

    Returns:
        float: The product of a and b.
    """
    return a * b

def divide(a, b):
    """
    Divides one number by another.

    Args:
        a (float): The dividend.
        b (float): The divisor.

    Returns:
        float: The quotient of a and b.

    Raises:
        ZeroDivisionError: If b is zero.
    """
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return a / b

def power(a, b):
    """
    Raises one number to the power of another.

    Args:
        a (float): The base.
        b (float): The exponent.

    Returns:
        float: The result of a raised to the power of b.
    """
    return a ** b

def sqrt(a):
    """
    Calculates the square root of a number.

    Args:
        a (float): The number.

    Returns:
        float: The square root of a.

    Raises:
        ValueError: If a is negative.
    """
    if a < 0:
        raise ValueError("Cannot calculate square root of negative number")
    return math.sqrt(a)

def sin(a):
    """
    Calculates the sine of an angle in radians.

    Args:
        a (float): The angle in radians.

    Returns:
        float: The sine of a.
    """
    return math.sin(a)

def cos(a):
    """
    Calculates the cosine of an angle in radians.

    Args:
        a (float): The angle in radians.

    Returns:
        float: The cosine of a.
    """
    return math.cos(a)

def tan(a):
    """
    Calculates the tangent of an angle in radians.

    Args:
        a (float): The angle in radians.

    Returns:
        float: The tangent of a.
    """
    return math.tan(a)