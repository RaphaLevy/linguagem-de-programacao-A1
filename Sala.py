class Sala():
    MAX_ASSENTOS = 120
    MIN_ASSENTOS = 15
    def _init_(self, nro_assentos):
        #self._tipo(tipo)
        self._nro_assentos = nro_assentos
        self.assentos = range(self.nro_assentos)
        
    '''        
    @property
    def tipo(self):
        return self._tipo
            
    @tipo.setter
    def set_tipo(self, tipo):
         self._tipo = tipo
    '''
    
    @property
    def nro_assentos(self):
        return self._assentos
    
    @nro_assentos.setter
    def set_nro_assentos(self, qtd_assentos):
        if qtd_assentos >= self.MIN_ASSENTOS and qtd_assentos <= self.MAX_ASSENTOS:
            self._nro_assentos = qtd_assentos
            self._assentos = range(self.nro_assentos)
            return 1
        else:
            del self 
        
    '''
    @assentos.setter
    def set_assentos(self, nro_assentos):
        self.assentos = []
        for i in range(0, self.nro_assentos):
            self.assentos.append(1)
    '''
