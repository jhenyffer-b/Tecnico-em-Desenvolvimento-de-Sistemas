nome_roupa = input("Digite o nome da roupa: ")
preco = float(input("Digite o valor da roupa: "))

def aplicar_desconto(preco):
    total = preco * 0.90
    print("O valor com desconto é: ", total)

aplicar_desconto(preco)