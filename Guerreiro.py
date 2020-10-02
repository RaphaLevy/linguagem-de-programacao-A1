#from Sala import Sala

class Guerreiro:
    """ A classe Guerreiro define um guerreiro por seu Nome e Idade"""
    def __init__(self, nome, idade): 
        self._nome = nome
        self._idade = int(idade)

    @property
    def nome(self):
        """Getter do nome do Guerreiro"""
        return self._nome
            
    @nome.setter
    def set_nome(self, apelido):
        """Setter do nome do Guerreiro"""
         self._nome = apelido
         
    @property
    def idade(self):
        """Getter da idade do Guerreiro"""
        return self._idade
    
    @idade.setter
    def set_idade(self, anos):
        """Setter da idade do Guerreiro"""
         self._idade = int(anos)