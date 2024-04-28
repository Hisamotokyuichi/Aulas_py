

import textwrap


def menu ():

    menu = """\n
    ================ MENU ================
    [d]\tDepositar
    [s]\tSacar
    [e]\tExtrato
    [nc]\tNova conta
    [lc]\tListar contas
    [cri]\tNovo usuário
    [q]\tSair
    => """
    return input(textwrap.dedent(menu))


    # menu =  """

    # [d] Depositar
    # [s] Sacar
    # [e] Extrato
    # [cri] criar conta
    # [lc]  listar contas
    # [nu] novo usuario
    # [q] Sair

    # => 

    # """
    




def depositar(saldo , valor , extrato,/):

    if valor > 0 :
        saldo += valor
        extrato += f"Deposito: {valor:.2f} \n"
        print("Depósito realizado com sucesso !")

    else :
        print("A operação falhou , por favor tente novamente !")

    return saldo , extrato


def sacar (*,saldo, valor , extrato , limite ,numero_saque ,limite_saque ):

            excedeu_saldo = valor > saldo 
            excedeu_limite = valor > limite
            excedeu_saques = numero_saque >= limite_saque

            if excedeu_saldo :
                print(f"Erro , saldo insuficiente!\n")

            elif excedeu_limite :
                print("Erro , limite de saque excedido!")

            elif excedeu_saques:
                print("Erro , Limite de saques diario excedido!")

            elif valor > 0:
                saldo -= valor 
                extrato += f"Saque: R${valor:.2f}\n"
                numero_saque += 1
                print("\n=== Saque realizado com sucesso! ===")

            else :
                print("Erro , valor inválido!")

            return saldo , extrato


def exibir_extrato (saldo, /,*,extrato):
    print("**********Extrato*************")
    print("Não houve movimentações."if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("********************************")


def crir_usuario (usuarios):
    cpf = input("Digite o seu cpf por favor ")
    usuario = filtrar_usuario(cpf,usuarios)

    if usuario: 
        print("já existe usuário com esse cpf !")
        return
    
    nome = input("Digite seu nome completo: ")
    data_nascimento= input("Informe sua data de nasimento (dd-mm-aaaa)")
    endereco = input("Informe seu endereço !")

    usuarios.append({"nome":nome , "data_nascimento":data_nascimento,"cpf":cpf, "endereco" :endereco })

    print("Usuário criado com sucesso !")





def filtrar_usuario(cpf,usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"]== cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None 


def criar_conta (agencia , numero_conta, usuarios):
    cpf = input("Informe seu cpf :")
    usuario = filtrar_usuario(cpf,usuarios)

    if usuario:
        print("conta criada com sucesso!")
        return {"agencia":agencia, "numero_conta":numero_conta,"usuario":usuario}
    
    print("usuário não encontrado , sua conta não foi criada !")



def listar_contas(contas):
    for conta in contas :
        linha = f"""\
            Agência:\t{conta['agencia']}
            C/C:\t\t{conta['numero_conta']}
            Titular:\t{conta['usuario']['nome']}
        """
        print("=" * 100)
        print(textwrap.dedent(linha))
        







   


def main ():
    LIMITE_SAQUE = 3
    AGENCIA = "0001"

    saldo = 1000
    limite = 500
    extrato =" "
    numero_saque = 0 
    usuarios = []
    contas = []

    while True:

        opcao = menu()

        if opcao == "d":
            
            valor = float(input("Digite o valor que deseja depositar: "))
            saldo,extrato = depositar(saldo,valor,extrato)
            
            #Aqui estou armazenando o valor depositado , para assim poder mostra no Extrato.
            # if valor > 0:
            #     saldo += valor 
            #     extrato += f"Depósito: R${valor:.2f}\n"  
    
            # else :
            #     print("erro , valor informado invalido.!")
        
        elif opcao == "s":
            print("Sacar")

            valor = float(input("Qual o valor que deseja sacar: "))

            saldo , extrato = sacar(saldo=saldo,
                                    valor=valor,
                                    extrato=extrato, 
                                    limite=limite,
                                    numero_saque=numero_saque,
                                    limite_saque=LIMITE_SAQUE )

            # excedeu_saldo = valor > saldo 

            # excedeu_limite = valor > limite

            # excedeu_saques = numero_saque >= LIMITE_SAQUE

            # if excedeu_saldo :
            #     print(f"Erro , saldo insuficiente!\n")

            # elif excedeu_limite :
            #     print("Erro , limite de saque excedido!")

            # elif excedeu_saques:
            #     print("Erro , Limite de saques diario excedido!")

            # elif valor > 0:
            #     saldo -= valor 
            #     extrato += f"Saque: R${valor:.2f}\n"
            #     numero_saque += 1
            
            # else :
            #     print("Erro , valor inválido!")
                

        elif opcao == "e":
            exibir_extrato(saldo,extrato=extrato)


        elif opcao =="cri":

            crir_usuario(usuarios)

        elif opcao == "nc":
             numero_conta = len(contas) + 1
             conta = criar_conta(AGENCIA, numero_conta, usuarios)
        
             if conta:
                contas.append(conta)

        elif opcao == "lc":
        
            listar_contas(contas)

        elif opcao == "q":
            break

        else :
            print("Operação invalidada , selecione outra opção!")


main()