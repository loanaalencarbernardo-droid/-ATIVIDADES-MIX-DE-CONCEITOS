frase = "Python é incrível e python é divertido"
palavras = frase.lower().split()
contagem = {}

for palavra in palavras:
    contagem[palavra] = contagem.get(palavra, 0) + 1

print(contagem)
# {'python': 2, 'é': 2, 'incrível': 1, 'e': 1, 'divertido': 1}