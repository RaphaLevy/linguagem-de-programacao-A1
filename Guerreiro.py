#Na verdade essa classe não existe, percebemos que o sistema não precisa dela para funcionar

class Guerreiro:
    """ A classe Guerreiro define um guerreiro por seu Nome e Idade"""
    def __init__(self, nome, idade):
        '''
        Init da classe Guerreiro

        Parameters
        ----------
        nome : string
            Nome do Guerreiro.
        idade : int
            Idade do GUerreiro.

        Returns
        -------
        None.

        '''
        self._nome = nome
        self._idade = int(idade)

    @property
    def nome(self):
        '''
        Getter do nome do Guerreiro

        Returns
        -------
        string
            Getter que retorna o nome do Guerreiro.

        '''
        return self._nome
            
    @nome.setter
    def set_nome(self, apelido):
        '''
        Setter do nome do Guerreiro

        Parameters
        ----------
        apelido : string
            Setter para o nome do guerreiro.

        Returns
        -------
        None.

        '''
        self._nome = apelido
         
    @property
    def idade(self):
        '''
        Getter da idade do Guerreiro

        Returns
        -------
        GUERREIRO
            Getter da idade do Guerreiro.

        '''
        return self._idade
    
    @idade.setter
    def set_idade(self, anos):
        '''
        Setter da idade do Guerreiro

        Parameters
        ----------
        anos : int
            Setter da idade do Guerreiro.

        Returns
        -------
        None.

        '''
        self._idade = int(anos)