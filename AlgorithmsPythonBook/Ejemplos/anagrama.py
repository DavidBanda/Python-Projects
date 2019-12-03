def anagrama(cadena1, cadena2):

    arrCadena1 = [0]*26
    arrCadena2 = [0]*26

    for i in range(len(cadena1)):
        arrCadena1[ord(cadena1[i]) - ord('a')] += 1
        arrCadena2[ord(cadena2[i]) - ord('a')] += 1

    for i in range(len(arrCadena1)):
        if arrCadena1[i] != arrCadena2[i]:
            return False
    return True


print(anagrama("aloh", "xddd"))

