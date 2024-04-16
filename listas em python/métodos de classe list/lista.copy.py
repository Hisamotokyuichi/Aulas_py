
list=[1, 'isaque', [90, 80, 7]]

l2 = list.copy()
#executando uma copia 

print(l2)
#verificando o id da lista e da copia.
print(id(l2), id (list))

l2[0]=1999
print (l2)






