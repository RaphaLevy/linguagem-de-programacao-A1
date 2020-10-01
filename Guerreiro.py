#from Sala import Sala

class Guerreiro:
    def __init__(self, nome, idade): 
        self._nome = nome
        self._idade = int(idade)

    @property
    def nome(self):
      return self._nome
            
    @nome.setter
    def set_nome(self, apelido):
         self._nome = apelido
         
    @property
    def idade(self):
        return self._idade
    
    @idade.setter
    def set_idade(self, anos):
         self._idade = int(anos)