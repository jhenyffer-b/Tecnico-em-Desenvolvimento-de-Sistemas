dados_matricula = {}

dados_matricula["Nome"] = input("Digite o nome: ")
dados_matricula["Idioma"] = input("Digite o idioma: ")
dados_matricula["Nivel"] = int(input("Digite o nível: "))
dados_matricula["ValorMensalidade"] = float(input("Digite o valor da mensalidade: "))

def mostrar_matricula(dados_matricula):
# Nome
    print(dados_matricula["Nome"])

# Idade
    print(dados_matricula["Idioma"])

# Curso
    print(dados_matricula["Nivel"])

# Nota
    print(dados_matricula["ValorMensalidade"])

mostrar_matricula(dados_matricula)