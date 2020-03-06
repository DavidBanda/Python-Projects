# o(2^n)
def get_nth_fib_2_n(n):

    if n <= 2:
        return n - 1

    return get_nth_fib_2_n(n - 1) + get_nth_fib_2_n(n - 2)


# 0,1,1,2,3,5,8,13,21,34
# o(n) ST
def get_nth_fib_n(n, memoize={1:0, 2:1}):

    if n in memoize:
        return memoize[n]
    else:
        memoize[n] = get_nth_fib_n(n - 1, memoize) + get_nth_fib_n(n - 2, memoize)
        return memoize[n]


print(get_nth_fib_n(8))


# 0,1,1,2,3,5,8,13,21,34
# o(n) T, o(1) S
def get_nth_fib_n_2(n):

    case_base = [0, 1]
    for i in range(n - 2):
        next = case_base[0] + case_base[1]
        case_base[0] = case_base[1]
        case_base[1] = next
    return case_base[1]


print(get_nth_fib_n_2(9))

