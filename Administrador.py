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
<<<<<<< HEAD
=======

>>>>>>> c6c490012e91adf42ff32c75019a294223aea290
        """
        
        return self._nome
    
    
    @nome.setter 
    def set_nome(self, novo_nome):
        """
        atribui um novo valor para o nome
<<<<<<< HEAD
=======

>>>>>>> c6c490012e91adf42ff32c75019a294223aea290
        Parameters
        ----------
        novo_nome : str
            novo nome a ser atribuido ao administrador.
<<<<<<< HEAD
=======

>>>>>>> c6c490012e91adf42ff32c75019a294223aea290
        """
        
        self._nome = novo_nome
     
        
    @property
    def senha(self):
        """
        retorna a senha de acesso do Administrador.
<<<<<<< HEAD
=======

>>>>>>> c6c490012e91adf42ff32c75019a294223aea290
        Returns
        -------
        str
            senha de acesso do Administrador.
<<<<<<< HEAD
=======

>>>>>>> c6c490012e91adf42ff32c75019a294223aea290
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
    
    
  
