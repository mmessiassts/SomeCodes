import textwrap

def menu():
    menu = """\n
    ================ MENU ================
    [d]\tDepositar
    [s]\tSacar
    [e]\tExtrato
    [nc]\tNova Conta
    [lc]\tListar Contas
    [nu]\tNovo Usuário
    [q]\tSair
    => """
    return input(textwrap.dedent(menu))

def depositar(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito:\tR$ {valor:.2f}\n"
        print("\n=== Depósito realizado com sucesso! ===")
    else:
        print("\n@@@ Operação falhou! O valor informado é inváido. @@@")

    return saldo, extrato    

def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques > limite_saques

    if excedeu_saldo:
        print("\n@@@ Operação falhou, você não tem saldo suficiente. @@@")

    elif excedeu_limite:
        print("\n@@@ Operação falhou, valor do saque excede o limite. @@@")

    elif excedeu_saques:
        print("\n@@@ Operação falhou, número máximo de saques excedido. @@@")

    elif valor > 0:
        saldo -= valor
        extrato += f"Saque:\t\tR$ {valor:.2f}\n"
        numero_saques +=1 
        print("=== Saque realizado com sucesso. ===")

    else:
        print("\n@@@ Operação falhou, o valor informado é inválido. @@@") 

    return saldo, extrato                   

def exibir_extrato(saldo, /, *, extrato):
    print("\n============ EXTRATO ============")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo:\t\tR$ {saldo:.2f}")
    print("==================")

def criar_usuario(usuarios):
    cpf = input("Informe o cpf(somente números): ")
    usuario = filtrar_usuario(cpf, usuarios)
    
    if usuario:
        print("\n@@@ Já existe usuário com esse cpf! @@@")
        return 
    nome = input("Informe o nome completo: ")
    data_nascimento = input("Infome a data de nascimento (dd-mm-aa): ")
    endereço = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado ): ")

    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereço": endereço})

    print("=== Usuário criado com sucesso! ===")

def filtrar_usuario(cpf, usuarios):
    usuarios_fitrados = [usuario for usuario in usuarios if usuario[cpf] == cpf]
    return usuarios_fitrados[0] if usuarios_fitrados else None
                    
def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o cpf do usuário: ")
    usuario = filtrar_usuario(cpf, usuario)

    if usuario:
        print("\n=== Conta criada com sucesso! ===")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}

        print("\n@@@ Usuário não encontrado, fluxo de criação de conta encerrado, @@@")    

def listar_contas(contas):
    for conta in contas:
        linha = f"""\
              Agência:\t{conta["agencia"]}
              C/C:\t{conta["numero_conta"]}
              Titular:\t{conta["usuario"]["nome"]}
              """
        print("=" * 100)
        print(textwrap.dedent(linha))

def main():
    LIMITE_SAQUES = 3
    AGENCIA = "0001"

    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    usuarios = []
    conta = []
    

    while True:
        opção = menu()

        if opção == "d":
        valor = float(input("Informe valor do depósito: "))
        saldo, extrato = depositar(saldo, valor, extrato)

        elif opção == "s":
        valor = float(input("Informe o valor do saque: "))

        saldo, extrato = sacar(
             saldo=saldo,
             valor=valor,
             extrato=extrato,
             limite=limite,
             numero_saques=numero_saques,
             limite_saques= LIMITE_SAQUES


        elif opção == "e":
            exibir_extrato(saldo, extrato=extrato)

        elif opção == "nu":
            criar_usuario(usuarios)

        elif opção == "nc":
            numero_conta = len(contas) +1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)
            if conta:
                contas.append(conta)

        elif opção == "lc":
              listar_contas(contas) 

        elif opção == "q":
             break           

        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")  

main()                                   