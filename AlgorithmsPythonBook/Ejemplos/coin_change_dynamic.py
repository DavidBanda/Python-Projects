def vueltasRec(lista_valores_monedas, vueltas):
    min_monedas = vueltas
    if vueltas in lista_valores_monedas:
        return 1
    else:
        for i in [m for m in lista_valores_monedas if m <= vueltas]:
            numero_monedas = 1 + vueltasRec(lista_valores_monedas, vueltas-i)
            if numero_monedas < min_monedas:
                min_monedas = numero_monedas
    return min_monedas


print(vueltasRec([1, 5, 10, 25], 2))










