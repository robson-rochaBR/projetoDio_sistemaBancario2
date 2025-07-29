def menu():
    """Exibe o menu de opções e retorna a escolha do usuário."""
    menu_str = """
============= Menu =============

Digite a opção desejada:
                        
    [1] - Deposito        
    [2] - Saque           
    [3] - Extrato
    [4] - Novo Usuário    
    [5] - Criar conta
    [6] - Listar contas           
                        
================================

▶ """
    return int(input(menu_str)) 

def depositar(saldo, extrato, /):
  
    deposito = float(input('Digite o valor do depósito: '))
    
    if deposito <= 0:
        print('\n Desculpe! Valor de depósito inválido!')
    else:
        saldo += deposito
        extrato.append({"tipo": "Depósito", "valor": deposito})
        print(f'\n=== Depósito de R${deposito:.2f} realizado com sucesso! ===')
    return saldo, extrato

def sacar(*, saldo, extrato, limite, numero_saques, limite_saques):
   
    saque = float(input('Digite o valor do saque: '))

    if saque > saldo:
        print('\nDesculpe! Não será possível realizar o saque, saldo insuficiente! ')
    elif saque > limite:
        print('\n Desculpe! Valor de saque excede o limite permitido! ')
    elif numero_saques >= limite_saques:
        print('\n Desculpe! Número máximo de saques diários excedido! ')
    else:
        saldo -= saque
        numero_saques += 1
        extrato.append({"tipo": "Saque", "valor": saque})
        print(f'\n=== Saque de R${saque:.2f} realizado com sucesso! ===')
    return saldo, extrato, numero_saques

def exibir_extrato(saldo, /, *, extrato_lista): 
      
    print('\n\n\n===== EXTRATO =====')
    if not extrato_lista:
        print('Não há transações para exibir no extrato!')
    else:
        for transacao in extrato_lista:
            print(f'{transacao["tipo"]}: R${transacao["valor"]:.2f}')
    print(f'\nSaldo atual: R${saldo:.2f}')
    print('===================\n\n\n')

def criar_usuario(usuarios):
      
    cpf = input("Informe o CPF (somente números): ")
    
    for usuario in usuarios:
        if usuario["cpf"] == cpf:
            print("\nERRO: Já existe usuário com este CPF! ")
            return None

    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/estado): ") 
    novo_usuario = {
        "nome": nome,
        "data_nascimento": data_nascimento,
        "cpf": cpf,
        "endereco": endereco
    }
    usuarios.append(novo_usuario)
    print("\n=== Usuário criado com sucesso! ===")
    return novo_usuario

def criar_conta_corrente(contas, usuarios):
       
    cpf = input("Informe o CPF do usuário para quem a conta será criada: ")
    usuario_encontrado = None
    for usuario in usuarios:
        if usuario["cpf"] == cpf:
            usuario_encontrado = usuario
            break
    
    if not usuario_encontrado:
        print("\n ERRO: Usuário não encontrado! Crie o usuário primeiro. ")
        return None

    # Verifica se o usuário já tem uma conta (opcional, dependendo da regra de negócio)
    for conta in contas:
        if conta["usuario"]["cpf"] == cpf:
            print("\nERRO: Este usuário já possui uma conta! ")
            return None

    numero_conta = len(contas) + 1 # Gera um número de conta simples
    agencia = "0001" 

    nova_conta = {
        "agencia": agencia,
        "numero_conta": numero_conta,
        "usuario": usuario_encontrado, 
        "saldo": 0.0,
        "limite": 500.0,
        "extrato": [],
        "numero_saques": 0,
        "limite_saques": 3
    }
    contas.append(nova_conta)
    print(f"\n=== Conta Corrente criada com sucesso! ===")
    print(f"Agência: {agencia}")
    print(f"Número da Conta: {numero_conta}")
    print(f"Titular: {usuario_encontrado['nome']}")
    return nova_conta

def listar_contas(contas):
    
    if not contas:
        print("\nNão há contas cadastradas! ")
        return

    print("\n============== LISTA DE CONTAS ==============")
    for conta in contas:
        print(f"Agência:\t{conta['agencia']}")
        print(f"Conta:\t\t{conta['numero_conta']}")
        print(f"Titular:\t{conta['usuario']['nome']} (CPF: {conta['usuario']['cpf']})")
        print("-------------------------------------")
    print("=============================================")

def main():
      
    saldo = 0.0 # O saldo de uma conta específica
    limite = 500.0
    extrato = []
    numero_saques = 0
    LIMITE_SAQUES = 3

    usuarios = [] 
    contas = []   

    while True:
        opcao = menu() 
        print()

        if opcao == 1: # Deposito
            # Em um sistema mais avançado, aqui você pediria qual conta depositar
            saldo, extrato = depositar(saldo, extrato)
        
        elif opcao == 2: # Saque
            # Aqui também pediria qual conta sacar
            saldo, extrato, numero_saques = sacar(saldo=saldo, extrato=extrato, limite=limite, numero_saques=numero_saques, limite_saques=LIMITE_SAQUES)
        
        elif opcao == 3: # Extrato
            # E qual conta exibir extrato
            exibir_extrato(saldo, extrato_lista=extrato)
        
        elif opcao == 4: # Novo Usuário
            criar_usuario(usuarios)

        elif opcao == 5: # Criar conta-corrente
            criar_conta_corrente(contas, usuarios)
        
        elif opcao == 6: # Listar contas
            listar_contas(contas)
        
        else:
            print('\nOpção inválida! Por favor, escolha uma opção válida. ')

        # Pergunta ao usuário se deseja continuar, exceto se a opção foi 'Sair'
        if opcao != 7: 
            continuar = input("\nDeseja realizar outra operação? (s/n): ").lower()
            if continuar != 's':
                print("Obrigado por utilizar nossos serviços!")
                break

main()
