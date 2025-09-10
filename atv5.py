def atualizar_idade(dicionario, nome, nova_idade):
    if nome in dicionario:
        dicionario[nome]['idade'] = nova_idade
    else:
        print("Pessoa não encontrada")

pessoas = {"Ana": {"idade": 25}}
atualizar_idade(pessoas, "Ana", 26)
print(pessoas)
# {'Ana': {'idade': 26}}