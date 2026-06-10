nome_bebida = (input("Digite o nome da bebida: "))
preco = float(input("Digite o preço da bebida: "))
qtd = int(input("Digite a quantidade: "))


def calcular_total(preco,qtd):
    total = preco * qtd
    print("O valor final é: ", total)

calcular_total(preco, qtd)


