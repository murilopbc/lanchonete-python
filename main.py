lanches = {
    1: "Hamburguer",
    2: "Cheeseburger",
    3: "X-Egg",
    4: "X-Salada",
    5: "X-Frango",
    6: "X-Vegetariano",
}

bebidas = {
    1: "Refrigerante",
    2: "Suco",
    3: "Água",
    4: "Chá",
}

sobremesas = {
    1: "Picolé",
    2: "Churros",
    3: "Petit Gateau",
    4: "Pudim",
}

pedido = []


def fazer_pedido(cardapio):
    print("Cardápio:")
    for indice, item in cardapio.items():
        print(f"{indice}: {item}")

    try:
        indice = int(input("Digite o índice do item desejado: "))
        if indice in cardapio:
            pedido.append(cardapio[indice])
            print(f"{cardapio[indice]} foi adicionado ao seu pedido.")
        else:
            print("Índice inválido. Tente novamente.")
    except ValueError:
        print("Entrada inválida. Digite um número válido.")


def finalizar_pedido():
    print("Seu pedido atual:")
    for item in pedido:
        print(item)

    resposta = input("Seu pedido está correto? (S para Sim / N para Não): ").lower()

    if resposta == 's':
        print("Pedido finalizado!")
    elif resposta == 'n':
        print("Pedido cancelado. Por favor, faça um novo pedido.")
    else:
        print("Resposta inválida. Digite 'S' para Sim ou 'N' para Não.")


while True:
    print("Escolha uma opção:")
    print("1. Fazer pedido de lanche")
    print("2. Fazer pedido de bebida")
    print("3. Fazer pedido de sobremesa")
    print("4. Finalizar pedido")

    opcao = input("Digite o número da opção desejada: ")

    if opcao == '1':
        fazer_pedido(lanches)
    elif opcao == '2':
        fazer_pedido(bebidas)
    elif opcao == '3':
        fazer_pedido(sobremesas)
    elif opcao == '4':
        finalizar_pedido()
        break
    else:
        print("Opção inválida. Tente novamente.")
