

class Bicicleta :

    def __init__(self, cor , modelo ,ano,valor):
        self.cor = cor
        self.modelo = modelo
        self.ano = ano 
        self.valor = valor 


    def buzinar(self):
        print("plim....plim")

    def parar(self):
        print("parando bicicleta")

    def correr (self):
        print("vrummmmm....")


b1 = Bicicleta( "vermelho", "caloi", 2025 , 600) 
b1 .buzinar()
b1.correr()
b1.parar()
print(b1.cor,b1.modelo,b1.ano,b1.valor)


b2 = Bicicleta("verde" ,"caloi", 2021 ,400)
b2.buzinar()
print(b2.cor)


















