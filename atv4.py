texto = "Python é incrível"
vogais = "aeiouáéíóú"
contador = sum(1 for letra in texto.lower() if letra in vogais)

print(f"Número de vogais: {contador}")
# Número de vogais: 6