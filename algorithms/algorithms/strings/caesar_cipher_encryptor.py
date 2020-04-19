string = 'xyz'
digit = 2


def caesarCipherEncryptor(string, key):

    encrypt = []
    key = key % 26

    for i in string:
        chr_transform = ord(i) + key
        if chr_transform <= 122:
            encrypt.append(chr(chr_transform))
        else:
            new_chr = 96 + (chr_transform % 122)
            encrypt.append(chr(new_chr))

    return "".join(encrypt)


print(caesarCipherEncryptor(string, digit))


