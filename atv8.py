numeros = [1, 2, 3, 4]

if all(num > 0 for num in numeros):
    print("Todos os números são positivos")
else:
    print("Há números negativos ou zero")
