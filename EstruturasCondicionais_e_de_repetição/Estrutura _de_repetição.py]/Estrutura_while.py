opcao = -1

#while opcao != 0 : 
   # opcao = int(input("[1] Sacar \n[2] Extrtato \n[0] sair \n"))

  #  if opcao == 1 :
    #    print("Sacando ...")
   # elif opcao == 2  :
  #      print("Extrato imprimindo")
   # else:
   #     print("saindo")


#break loop infinito 

while True:
    numero =int(input("Digite um numero :"))

    if numero == 13:
        print("Obrigado por usar nosso programa!")
        break

    print(numero)


for numero_for in range(100):
    if numero_for == 12:
        break


    print(numero_for)



















