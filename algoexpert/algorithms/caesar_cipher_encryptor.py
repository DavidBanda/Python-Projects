string = 'abc'
digit = 7


def caesarCipherEncryptor(string, key):

    str_con = []
    key = key % 26
    for i in range(len(string)):
        new_letter = ord(string[i]) + key
        if new_letter <= 122:
            str_con.append(chr(new_letter))
        else:
            str_con.append(chr(96 + new_letter % 122))

    return "".join(str_con)


print(caesarCipherEncryptor(string, digit))


