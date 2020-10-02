from Sessao import Sessao
from Sala import Sala 
from Midgard import Midgard 
from Asgard import Asgard 

class Administrador:
    def __init__(self, nome, senha):
        """
        construtor da classe Administrador 

        Parameters
        ----------
        nome : str
            nome de usuário do Administrador.
        senha : str
            senha de acesso do Administrador.
        *salas : list de Salas
            salas administradas pelo Administrador.
        """
        
        self._nome = nome
        self._senha = senha

        
        
    @property
    def nome(self):
        """
        retorna o nome de usuário do Administrador.

        Returns
        -------
        str
            nome de usuário do Administrador.

        """
        
        return self._nome
    
    
    @nome.setter 
    def set_nome(self, novo_nome):
        """
        atribui um novo valor para o nome

        Parameters
        ----------
        novo_nome : str
            novo nome a ser atribuido ao administrador.

        """
        
        self._nome = novo_nome
     
        
    @property
    def senha(self):
        """
        retorna a senha de acesso do Administrador.

        Returns
        -------
        str
            senha de acesso do Administrador.

        """
        
        return self._senha
    
    
    @senha.setter
    def set_senha(self, nova_senha):
        """
        atribui um novo valor para a senha.

        Parameters
        ----------
        novo_nome : str
            nova senha a ser atribuido ao administrador.

        """
        
        self._senha = nova_senha
    
    
  
