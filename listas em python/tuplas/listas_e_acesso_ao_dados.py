#list
frutas = ["laranja", " maça" , "uva"]
print(frutas)
#lista vazia 
frutas = []
print(frutas)

letras = list("python")
print(letras)
#cada letra tem um valor dentro da lista

numeros = list (range(10))
print (numeros)


carro = ["Ferrari", "F8" , 420000 , 2020 , 2900, " são paulo", True]

print (carro)

# indexação negativa.
fruts= ["carro", "moto" , "barco"]
print(fruts[-1])


#matrix bidimencional
matrix = [
    [0,2,"b"],
    [8,15,"m"],
    [10,2,5]

]

print(matrix[2][-1])

#comando for 

carros = ["celta", "celta","palio"]
for carro in carro:
    print(carro)

for indice , carro in enumerate(carros):
    print(f"{indice}:{carro}")





