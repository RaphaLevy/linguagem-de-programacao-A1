import Sala from Sala
import Midgard from Midgard
import Asgard from Asgard

class Administrador:
    def __init__(self, nome, senha, *salas):
        """
        construtor da classe Administrador 
<<<<<<< HEAD
=======

>>>>>>> c6c490012e91adf42ff32c75019a294223aea290
        Parameters
        ----------
        nome : str
            nome de usuário do Administrador.
        senha : str
            senha de acesso do Administrador.
        *salas : list de Salas
            salas administradas pelo Administrador.
<<<<<<< HEAD
=======

>>>>>>> c6c490012e91adf42ff32c75019a294223aea290
        """
        
        self._nome = nome
        self._senha = senha
        self._salas = salas
        
        
    @property
    def nome(self):
        """
        retorna o nome de usuário do Administrador.
<<<<<<< HEAD
=======

>>>>>>> c6c490012e91adf42ff32c75019a294223aea290
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
        atribui um novo valor para a senha
<<<<<<< HEAD
=======

>>>>>>> c6c490012e91adf42ff32c75019a294223aea290
        Parameters
        ----------
        novo_nome : str
            nova senha a ser atribuido ao administrador.
<<<<<<< HEAD
=======

>>>>>>> c6c490012e91adf42ff32c75019a294223aea290
        """
        
        self._senha = nova_senha
    
    
    @property
    def salas(self):
        """
        retorna as salas administradas pelo Administrador.
<<<<<<< HEAD
=======

>>>>>>> c6c490012e91adf42ff32c75019a294223aea290
        Returns
        -------
        list
            lista com as salas administradas pelo Administrador.
<<<<<<< HEAD
=======

>>>>>>> c6c490012e91adf42ff32c75019a294223aea290
        """
        
        return self.salas
    
    def add_sala(self, nova_sala):
        """
        adiciona uma nova sala na lista de salas administradas pelo Administrador
<<<<<<< HEAD
=======

>>>>>>> c6c490012e91adf42ff32c75019a294223aea290
        Parameters
        ----------
        nova_sala : Sala
            sala a ser adicionada.
<<<<<<< HEAD
=======

>>>>>>> c6c490012e91adf42ff32c75019a294223aea290
        """
        
        self._salas.append(nova_sala)
    
    def rm_sala(self, sala):
        """
        remove uma sala da lista de salas administradas pelo Administrador
<<<<<<< HEAD
=======

>>>>>>> c6c490012e91adf42ff32c75019a294223aea290
        Parameters
        ----------
        nova_sala : Sala
            sala a ser removida.
<<<<<<< HEAD
        """
        
        self._salas.remove(sala)
        
   def get_ingressos_vendidos()

   def verificar_programacao(self, Sala):
       for each Sessao in Sala:
           print(Sessao.filme, Sessao.hora, Sessao.data)
=======

        """
        
        self._salas.remove(sala)
>>>>>>> c6c490012e91adf42ff32c75019a294223aea290
