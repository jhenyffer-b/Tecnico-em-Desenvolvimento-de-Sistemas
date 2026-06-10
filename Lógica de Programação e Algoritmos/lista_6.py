def gerar_resumo(tipo, valor):
    print("O tipo do ingressos é: ", tipo)
    print("O valor do ingresso é: ", valor)

nome = input("Digite seu nome: ")
print("----- Menu de ingresos -----")
print("1 - Normal")
print("2 - Estudante")
print(" 3 - Idoso")
opcao = int(input("Digite a opção do ingresso: "))

match opcao:
    case 1:
        gerar_resumo("Normal", 30)
    case 2:
        gerar_resumo("Estudante", 15)
    case 3:
        gerar_resumo("Idoso", 20)
    case _:
        print("Opção Inválida!")