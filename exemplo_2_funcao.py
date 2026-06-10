# Criar a função
def calcularMedia(nota1, nota2, nota3, nota4):  
    media = (nota1 + nota2 + nota3 + nota4)/4
    print("Sua média é: ", media)

# Chamar a função para o 1º aluno
calcularMedia(4, 10, 9, 7)

# Chamar a função para o 2º aluno
n1 = int(input("Digite a nota 1: "))
n2 = int(input("Digite a nota 2: "))
n3 = int(input("Digite a nota 3: "))
n4 = int(input("Digite a nota 4: "))
calcularMedia(n1, n2, n3, n4)