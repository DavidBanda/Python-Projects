def getNthFib(n):

    if n <= 0:
        return 0
    if n == 1:
        return 1

    return getNthFib(n - 1) + getNthFib(n - 2)


print(getNthFib(4))

