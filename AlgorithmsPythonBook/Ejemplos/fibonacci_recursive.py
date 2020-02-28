def fibonacci_recursive(n):

    if n == 0:
        return 0

    if n == 1 or n == 2:
        return 1

    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)


print(fibonacci_recursive(11))