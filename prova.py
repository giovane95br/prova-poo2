class Veiculos:
    def __init__(self, movimento): 
        self.movimento = movimento

    def movimentar(self):
        return self.movimento  

class Carro(Veiculos): 
    pass  

class Moto(Veiculos): 
    pass 

movimento_carro = "Carro esta dirigindo"
carro = Carro(movimento_carro)  
print(carro.movimentar())

movimento_moto = "Moto esta acelerando"
moto = Moto(movimento_moto)  
print(moto.movimentar())
