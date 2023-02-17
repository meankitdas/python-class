class FactorialError(Exception): pass


def factorial(n):

    if n < 0:
        raise FactorialError('Factorial expects non-negative integers')
    return 1 if n == 0 else n*factorial(n-1)


factorial(-1)