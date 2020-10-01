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
    
    @data.setter
    def set_data(self, val):
        self._data = date.fromisoformat(val)
    
    @property 
    def hora(self):
        return self._hora
    
    @hora.setter
    def set_hora(self, tempo):
        self._hora = time.fromisoformat(tempo)
    
    @property
    def filme(self):
        return self._filme
    
    @filme.setter
    def set_filme(self, ver):
        self.filme = ver

