from datetime import date, time
from Filme import Filme

class Sessao:
    def __init__(self, data, hora, filme):
        self._data = data #'AAAA-MM-DD'
        self._hora = hora #'HH:MM:SS'
        self._filme = filme
        
    @property
    def data(self):
        return self._data
    '''
    @data.setter
    def set_data(self, val):
        self._data = val
    '''
    @property 
    def hora(self):
        return self._hora
    
    @hora.setter
    def set_hora(self, val):
        self._hora = val
    
    @property
    def filme(self):
        return self._filme
    
    @filme.setter
    def set_filme(self, val):
        self.filme = val
    
filme = Filme("Vida de Inseto", 18, 120)
data = date.fromisoformat("2020-03-03")
hora = time.fromisoformat("16:30:00")
print(data)
sessao = Sessao(data, hora, filme)
print(Sessao.data)