remedios = []

for i in range(4):
    remedio = {}
    remedio["Nome"] = input("Digite o nome: ")
    remedio["Fabricante"] = input("Digite o fabricante: ")
    remedio["Qtd"] = int(input("Digite a quantidade: "))
    remedio["Preco"] = float(input("Digite o preço: "))

    remedios.append(remedio)

    if(remedio["Qtd"] < 10):
        # Nome
        print(remedio["Nome"])

        # Idade
        print(remedio["Fabricante"])

        # Curso
        print(remedio["Qtd"])

        # Nota
        print(remedio["Preco"])