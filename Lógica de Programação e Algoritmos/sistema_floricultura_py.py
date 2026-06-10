# Sistema de cadastro de usuários, cadastro de entrega e produtos
# O sistema deverá permitir:
# - cadastrar
# - listar
# - deletar
# - sair

# Criação das listas
entregas = []
produtos = []

# -----------------------------------
# ------ Função Menu Usuários -------
def menu_usuarios():
    opcao_menu_usuario = 0

    while(opcao_menu_usuario != 3):
        print()
        print("----- Menu Usuários -----")
        print("1 - Cadastrar Entregas")
        print("2 - Listar Entregas")
        print("3 - Deletar Entregas")
        print("4 - Sair")

        opcao_menu_usuario = int(input("Escolha uma opção: "))

        match opcao_menu_usuario:
            # Cadastrar Usuário
            case 1:
                nome_comprador = input("Digite o nome do comprador: ")
                telefone_comprador = input("Digite o telefone do comprador: ")
                nome_recebedor = input("Digite o nome do recebedor: ")
                telefone_recebedor = int(input("Digite o telefone do recebedor: "))
                endereco_recebedor = input("Digite o endereço do recebedor: ")
                produto_entrega = input("Digite o produto a ser entregue: ")

                # Criação do json de usuários (chave: valor)
                entrega = {
                    "nome_comprador": nome_comprador,
                    "telefone_comprador": telefone_comprador,
                    "nome_recebedor": nome_recebedor,
                    "telefone_recebedor": telefone_recebedor,
                    "endereco_recebedor": endereco_recebedor,
                    "produto_entrega": produto_entrega

                    
                }
                # Adicionar json no array
                entregas.append(entrega)
                print(f"Entrega de {entrega['nome_comprador']} cadastrado com sucesso!")
            # Listar Entregas
            case 2:
                print("\n Lista de Entregas: ")

                if(len(entregas) == 0):
                    print("Nenhum usuário cadastrado!")
                else:
                    for ent in entregas:
                        print("---------")
                        print("Nome: ", ent["nome_comprador"])
                        print("Telefone: ", ent["telefone_comprador"])
                        print("Nome: ", ent["nome_recebedor"])
                        print("Telefone: ", ent["telefone_recebedor"])
                        print("Endereco_recebedor: ", ent["endereco_recebedor"])
                        print("Produto_entrega: ", ent["produto_entrega"])
                        
            # Deletar Entregas
            case 3: 
                entrega_deletar = input("Digite o nome do comprador da entrega que deseja deletar: ")
                encontrado = False 

                for ent in entregas: 
                    if(ent["nome_comprador"] == entrega_deletar):
                        entregas.remove(ent)
                        encontrado = True
                        print("Entrega removida com sucesso!")

                if(encontrado == False):
                    print("Entrega não encontrada!")
            # Voltar ao menu principal
            case 4:
                print("Voltando ao menu principal...")
                break 

# -----------------------------------
# ------ Função Menu Produtos -------
def menu_produtos():
    opcao_menu_produto = 0

    while(opcao_menu_produto != 5):
        print()
        print("----- Menu Produtos -----")
        print("1 - Cadastrar Produto")
        print("2 - Listar Produtos")
        print("3 - Deletar Produto")
        print("4 - Calcular Total")
        print("5 - Voltar")

        opcao_menu_produto = int(input("Escolha uma opção: "))

        match opcao_menu_produto:
            # Cadastrar Prouto
            case 1:
                nome = input("Digite o nome: ")
                descricao = input("Digite a descrição: ")
                quantidade = int(input("Digite a quantidade: "))
                valor = float(input("Digite o valor: "))

                # Criação do json de produtos (chave: valor)
                produto = {
                    "nome": nome,
                    "descricao": descricao,
                    "quantidade": quantidade,
                    "valor": valor
                }
                # Adicionar json no array
                produtos.append(produto)
                print(f"Produto {produto['nome']} cadastrado com sucesso!")
            # Listar Produtos
            case 2:
                print("\n Lista de Produtos: ")

                if(len(produtos) == 0):
                    print("Nenhum produto cadastrado!")
                else:
                    for pro in produtos:
                        print("---------")
                        nome = input("Nome: ", pro["nome"])
                        descricao = input("Descrição: ", pro["descricao"])
                        qtd = int(input("Quantidade: ", pro["quantidade"]))
                        valor = float(input("Valor: ", pro["valor"]))
            # Deletar Produto
            case 3: 
                nome_deletar = input("Digite o nome do produto que deseja deletar: ")
                encontrado = False 

                for pro in produtos: 
                    if(pro["nome"] == nome_deletar):
                        produtos.remove(pro)
                        encontrado = True
                        print("Produto removido com sucesso!")

                if(encontrado == False):
                    print("Produto não encontrado!")
            # Calcular Total
            case 4:
                nome_calcular = input("Digite o nome do produto que deseja calcular: ")
                encontrado = False 

                for pro in produtos: 
                    if(pro["nome"] == nome_calcular):
                        print("Total = ", pro["valor"] * pro["quantidade"])

            
            # Voltar ao menu principal
            case 5:
                print("Voltando ao menu principal...")
                break 
# ------------------------------------------------
# ---- Menu Principal ----
opcao_menu = 0
while(opcao_menu != 3):
    print("----- Menu - Sistema de Cadastro -----")
    print("Opções: ")
    print("1 - Clientes")
    print("2 - Produtos")
    print("3 - Sair")
    opcao_menu = int(input("Escolha uma opção: "))

    match opcao_menu:
        # Menu Usuários
        case 1: 
            menu_usuarios()
        # Menu Produtos
        case 2:
            menu_produtos()
        case 3:
            print("👋🏼 Até Logo!")
        case _:
            print("❌ Opção Inválida!")
