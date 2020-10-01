class Sala():
    def __init__(self, tipo, nro_assentos):
        self.tipo(tipo)
        #self.nro_assentos = nro_assentos
        self.assentos(nro_assentos)
            
    @property
    def tipo(self):
        return self.tipo
            
    @tipo.setter
    def set_tipo(self, tipo):
         self._tipo = tipo
         
    @property
    def assentos(self):
        return self.assentos
    
    @assentos.setter
    def set_assentos(self, nro_assentos):
        self.assentos = []
        for i in range(0, self.nro_assentos):
            self.assentos.append(1)
