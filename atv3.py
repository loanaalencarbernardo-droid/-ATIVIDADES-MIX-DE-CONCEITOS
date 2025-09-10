estoque = {"maçã": 10, "banana": 5}

print("Menu:")
print("1 - Ver estoque")
print("2 - Adicionar item")
opcao = input("Escolha uma opção: ")

if opcao == "1":
    print("Estoque atual:", estoque)
elif opcao == "2":
    item = input("Nome do item: ")
    quantidade = int(input("Quantidade: "))
    estoque[item] = estoque.get(item, 0) + quantidade
    print("Estoque atualizado:", estoque)
else:
    print("Opção inválida")
