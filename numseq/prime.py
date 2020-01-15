"""
Contains functions that handle prime numbers
"""
def is_prime(n):
    """Returns true if n is a prime number 
    but returns false if not """
    if n <= 1:
        return False
    elif n == 2:
        return True
    else:
        for x in range(2,n):
            if n % x == 0:
                return False
        return True


def prime(n):
    """Returns a list of all prime numbers less than n"""
    stack = []
    for y in range(1, n + 1):
        if is_prime(y):
            stack.append(y)
    return stack