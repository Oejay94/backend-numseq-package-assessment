"""
Contains a function that returns the nth fibonacci number
"""
def fibonacci(n):
    """Returns the nth fibonacci number"""
    if n > 1:
        return fibonacci(n-1) + fibonacci(n-2)
    return n