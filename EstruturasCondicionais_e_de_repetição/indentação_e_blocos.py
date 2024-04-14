
#def metodo
def sacar( valor ) :
    saldo = 500 
    
    if saldo  >= valor:
        print("valor sacado")
        print("retire o seu dinheiro na boca do caixa")

    print("obrigado por ser nosso cliente")


def depositar(valor):
    saldo = 500
    saldo += valor

    if (valor >= 1):
        print(f"valor depositado foi de :" ,valor)

    print(f"Saldo atual na conta é de :" , saldo)


sacar(100)
depositar(100)

