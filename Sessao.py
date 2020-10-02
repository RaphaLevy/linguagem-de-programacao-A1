from datetime import date, time
from Filme import Filme

class Sessao:
    """A classe Sessao define uma sessão por sua Data e Hora."""
    def __init__(self, data, hora, filme):
        self._data = data #'AAAA-MM-DD'
        self._hora = hora #'HH:MM:SS'
        self._filme = filme
        
    @property
    def data(self):
        """Getter da data da sessão."""
        return self._data
    
    @data.setter
    def set_data(self, val):
        """Setter da data da sessão."""
        self._data = date.fromisoformat(val)
    
    @property 
    def hora(self):
        """Getter da hora da sessão."""
        return self._hora
    
    @hora.setter
    def set_hora(self, tempo):
        """Setter da hora da sessão."""
        self._hora = time.fromisoformat(tempo)
    
    @property
    def filme(self):
        """Getter do filme da sessão."""
        return self._filme
    
    @filme.setter
    def set_filme(self, ver):
        """Setter doo filme da sessão."""
        self.filme = ver

