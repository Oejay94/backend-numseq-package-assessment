def is_prime(n):
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
    stack = []
    for y in range(1, n + 1):
        if is_prime(y):
            stack.append(y)
    return stack