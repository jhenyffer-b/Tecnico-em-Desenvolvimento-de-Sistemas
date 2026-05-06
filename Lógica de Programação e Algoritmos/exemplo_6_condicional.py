valorCompra = float(input("Digite o valor da compra: "))
cupomDesconto = input("Possui cupom de desconto? ")

if(valorCompra >= 200 or cupomDesconto == "Sim"):   
    print("Você ganhou um desconto de 15%!")
else:
    print("Você não tem direito a descontos no momento!")