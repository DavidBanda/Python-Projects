def anagrama(str1, str2):

    if len(str1) != len(str2):
        return False

    arrCadena = [0]*26

    for i in range(len(str1)):
        # print(str1[i], ord(str1[i]) - 97)
        arrCadena[ord(str1[i]) - 97] += 1
        arrCadena[ord(str2[i]) - 97] -= 1

    for i in range(len(arrCadena)):
        if arrCadena[i] != 0:
            return False

    return True


print(anagrama("hola", "aloh"))



