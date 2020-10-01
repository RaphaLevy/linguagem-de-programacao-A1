from Sessao import Sessao
from Filme import Filme

class Sala():
    MAX_ASSENTOS = 120
    MIN_ASSENTOS = 15
    def _init_(self, nro_assentos, preco):
        #self._tipo(tipo)
        self._nro_assentos = nro_assentos
        self._assentos = range(self.nro_assentos)
        self._sessoes = []
        self._preco = preco
        
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
        
    @property 
    def preco(self):
        return self._preco
    
    @preco.setter
    def set_preco(self, valor):
        self._preco = valor
    
'''    
    def add_sessao(self, nova_sessao):
        for cada_sessao in self.sessoes:
'''      
            
        
    '''
    @assentos.setter
    def set_assentos(self, nro_assentos):
        self.assentos = []
        for i in range(0, self.nro_assentos):
            self.assentos.append(1)
    '''
