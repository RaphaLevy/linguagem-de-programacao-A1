from Sala import Sala

class Asgard(Sala):
    MAX_ASSENTOS = 30
    MIN_ASSENTOS = 15
    def __init__(self, nro_assentos):  
        super().__init__(nro_assentos)

    @property
    def nro_assentos(self):
        return self.assentos
    
    @nro_assentos.setter
    def set_nro_assentos(self, qtd_assentos):
        if qtd_assentos >= self.MIN_ASSENTOS and qtd_assentos <= self.MAX_ASSENTOS:
            self._nro_assentos = qtd_assentos
            return 1
        else:
            del self 