from Sala import Sala

class Asgard(Sala):
    MAX_ASSENTOS = 30
    MIN_ASSENTOS = 15
    def __init__(self, nro_assentos, preco):  
        super().__init__(nro_assentos, preco)
        self.sessoes = []


    @property
    def nro_assentos(self):
        return self._nro_assentos
    
    @nro_assentos.setter
    def set_nro_assentos(self, qtd_assentos):
        if qtd_assentos >= self.MIN_ASSENTOS and qtd_assentos <= self.MAX_ASSENTOS:
            self._nro_assentos = qtd_assentos
           #self._assentos = range(self.nro_assentos)
            return 1
        else:
            del self 
            
#Testes da classe
'''   
asg = Asgard(int(20), int(20))
print(asg.nro_assentos)

asg1 = Asgard(int(25), int(30))            
'''