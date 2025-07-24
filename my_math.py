pi=3.1473
def add(x, y):
    """Returns the sum of x and y."""
    return x + y
def subtract(x, y):
    """Returns the difference of x and y."""
    return x - y
def multiply(x, y):
    """Returns the product of x and y."""
    return x * y
def divide(x, y):
    """Returns the quotient of x and y."""
    if y == 0:
        raise ValueError("Cannot divide by zero.")
    return x / y
def power(x, y):
    """Returns x raised to the power of y."""
    return x ** y
def factorial(n):
    """Returns the factorial of n."""
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    if n == 0 or n == 1:
        return 1
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result
def square_root(x):
    """Returns the square root of x."""
    if x < 0:
        raise ValueError("Cannot compute square root of negative number.")
    return x ** 0.5
def absolute_value(x):
    """Returns the absolute value of x."""
    return abs(x)
def logarithm(x, base=10):
    """Returns the logarithm of x to the specified base."""
    if x <= 0:
        raise ValueError("Logarithm is not defined for non-positive numbers.")
    if base <= 1:
        raise ValueError("Base must be greater than 1.")
    import math
    return math.log(x, base)
