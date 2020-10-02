from Sala import Sala 
from Midgard import Midgard 
from Asgard import Asgard 

class Administrador:
    def __init__(self, nome, senha, *salas):
        """
        construtor da classe Administrador 
<<<<<<< HEAD
=======


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


        Returns
        -------
        str
            nome de usuário do Administrador.
<<<<<<< HEAD
=======


        """
        
        return self._nome
    
    
    @nome.setter 
    def set_nome(self, novo_nome):
        """
        atribui um novo valor para o nome
<<<<<<< HEAD
=======


        Parameters
        ----------
        novo_nome : str
            novo nome a ser atribuido ao administrador.
<<<<<<< HEAD
=======


        """
        
        self._nome = novo_nome
     
        
    @property
    def senha(self):
        """
        retorna a senha de acesso do Administrador.
<<<<<<< HEAD
=======


        Returns
        -------
        str
            senha de acesso do Administrador.
<<<<<<< HEAD
=======


        """
        
        return self._senha
    
    
    @senha.setter
    def set_senha(self, nova_senha):
        """
        atribui um novo valor para a senha
<<<<<<< HEAD
=======


        Parameters
        ----------
        novo_nome : str
            nova senha a ser atribuido ao administrador.
<<<<<<< HEAD
=======


        """
        
        self._senha = nova_senha
    
    
    @property
    def salas(self):
        """
        retorna as salas administradas pelo Administrador.
<<<<<<< HEAD
=======


        Returns
        -------
        list
            lista com as salas administradas pelo Administrador.
<<<<<<< HEAD
=======


        """
        
        return self.salas
    
    def add_sala(self, nova_sala):
        """
        adiciona uma nova sala na lista de salas administradas pelo Administrador
<<<<<<< HEAD
=======


        Parameters
        ----------
        nova_sala : Sala
            sala a ser adicionada.
<<<<<<< HEAD
=======


        """
        
        self._salas.append(nova_sala)
    
    def rm_sala(self, sala):
        """
        remove uma sala da lista de salas administradas pelo Administrador
<<<<<<< HEAD
=======


        Parameters
        ----------
        nova_sala : Sala
            sala a ser removida.
<<<<<<< HEAD
        """
        
        self._salas.remove(sala)
        
   #"def get_ingressos_vendidos():"

    def verificar_programacao(self, Sala, Sessao):
        for cada_sessao in Sala:
           print(Sessao.filme, Sessao.hora, Sessao.data)



        
