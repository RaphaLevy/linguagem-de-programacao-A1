from Sala import Sala

class Midgard(Sala):
    MAX_ASSENTOS = 120
    MIN_ASSENTOS = 60
    def __init__(self, nro_assentos, preco):  
        super().__init__(nro_assentos, preco)
        
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
'''            
mid = Midgard(int(90), int(20))
print(mid.nro_assentos)

mid1 = Midgard(int(50), int(30))
'''