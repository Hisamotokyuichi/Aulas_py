# ordena de tamando crecente ou decresente


lista=["python", "js","c","c++"]

lista.sort()

#ordena de traz para frente 
lista=["python", "js","c","c++"]
lista.sort(reverse=True)


#ordena por tamanho da string 
lista=["python", "js","c","c++"]
lista.sort(key= lambda x: len(x))
#ordena por tamanho da string inverso
lista.sort(key=lambda x: len(x), reverse=True)





