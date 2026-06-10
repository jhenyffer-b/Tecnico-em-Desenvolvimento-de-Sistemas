print("---- Menu de Opção ----")
print("1 - Econômica")
print("2 - Conforto")
print("3 - Luxo")
opcao = int(input("Digite uma opção: "))

match opcao:
    case 1: 
        print("Econômica")
    case 2:
        print("Conforto")
    case 3:
        print("Luxo")
    case _:
        print("Opção Inválida")