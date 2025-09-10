def filtrar_pares(lista):
    return [num for num in lista if num % 2 == 0]

numeros = [1, 2, 3, 4, 5, 6]
pares = filtrar_pares(numeros)
print(pares)
# [2, 4, 6]