# numeros = [1,2,3,4,5,6,7,8,8,9,0,99,77,]
# pares = []

# for numero in numeros :
#     if numero % 2 == 0:
#         pares.append(numero)


numeros = [1,2,3,4,5,6,7,8,8,9,0,99,77,]
pares = [numero for numero in numeros if numero % 2 ==0]
print(pares)
quadrados = [numero ** 2 for numero in numeros ] 
print(quadrados)







