# Controle de Estoque Simples

estoque = {}

def adicionar_produto():
    nome = input("Nome do produto: ").strip().lower()
    
    if nome in estoque:
        print("Produto já existe! Use a opção de entrada de estoque.")
        return
    
    try:
        quantidade = int(input("Quantidade inicial: "))
        if quantidade < 0:
            print("Quantidade não pode ser negativa.")
            return
    except ValueError:
        print("Digite um número válido.")
        return

    estoque[nome] = quantidade
    print(f"Produto '{nome}' adicionado com sucesso!")

def entrada_estoque():
    nome = input("Nome do produto: ").strip().lower()

    if nome not in estoque:
        print("Produto não encontrado.")
        return

    try:
        quantidade = int(input("Quantidade de entrada: "))
        if quantidade <= 0:
            print("Digite um valor maior que zero.")
            return
    except ValueError:
        print("Número inválido.")
        return

    estoque[nome] += quantidade
    print(f"Entrada realizada! Novo estoque de {nome}: {estoque[nome]}")

def saida_estoque():
    nome = input("Nome do produto: ").strip().lower()

    if nome not in estoque:
        print("Produto não encontrado.")
        return

    try:
        quantidade = int(input("Quantidade de saída: "))
        if quantidade <= 0:
            print("Digite um valor maior que zero.")
            return
    except ValueError:
        print("Número inválido.")
        return

    if quantidade > estoque[nome]:
        print("Erro: estoque insuficiente!")
        return

    estoque[nome] -= quantidade
    print(f"Saída realizada! Novo estoque de {nome}: {estoque[nome]}")

def listar_produtos():
    if not estoque:
        print("Nenhum produto cadastrado.")
        return

    print("\n--- ESTOQUE ATUAL ---")
    for produto, qtd in estoque.items():
        print(f"{produto}: {qtd}")
    print("---------------------\n")

def menu():
    while True:
        print("\n===== CONTROLE DE ESTOQUE =====")
        print("1 - Adicionar produto")
        print("2 - Entrada no estoque")
        print("3 - Saída do estoque")
        print("4 - Listar produtos")
        print("5 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            adicionar_produto()
        elif opcao == "2":
            entrada_estoque()
        elif opcao == "3":
            saida_estoque()
        elif opcao == "4":
            listar_produtos()
        elif opcao == "5":
            print("Saindo do sistema...")
            break
        else:
            print("Opção inválida!")

# Iniciar programa
menu()
