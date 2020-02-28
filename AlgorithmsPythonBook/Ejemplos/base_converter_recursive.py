def my_base_converter(num, base):
    digits = '0123456789ABCDEF'
    result = ''

    while num > 0:
        res_temp = digits[num % base]
        result = f'{res_temp}' + result
        num = num // base

    return result


def my_base_converter_factorial(num, base):
    digits = '0123456789ABCDEF'

    if num <= 0:
        return ''

    return my_base_converter_factorial(num // base, base) + digits[num % base]


print(my_base_converter(100010101, 2))
print(my_base_converter_factorial(100010101, 2))






