class carro :

    def __init__(self,potencia, peso , cor) :
        self.potencia = potencia
        self.cor = cor
        self.peso = peso

    
    def ligar (self):
        print('estou ligando')

    def falta_de_combustivel (self):
        print('por favor abastecer o veiculo ')

    def pneu_mucho (self):
        print('por favor calibrar o pneu')

    def desligar (self):
        print('estou desligando')


carro1 = carro ("100 cavalos" ,"500 kilos" ,"preto")
print(carro1.cor)
carro2 = carro ('500 cavalos ', '200 kilos' , 'azul')
print(carro2.cor)
carro1.ligar()
carro1.falta_de_combustivel()
carro1.pneu_mucho()
carro1.desligar()
