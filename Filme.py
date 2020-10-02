class Filme:
    """ A classe Filme define um filme por seu Título, Classificação e Duração"""
    def __init__(self, titulo, classificacao, duracao):
        '''
        Init da classe filme

        Parameters
        ----------
        titulo : str
            Define o título do filme.
        classificacao : int
            Define a classificação do filme.
        duracao : int
            Define a duração do filme.

        Returns
        -------
        None.

        '''
        self._titulo = titulo
        self._classificacao = classificacao
        self._duracao = duracao
        
    @property
    def titulo(self):
        '''
        Getter do título do Filme

        Returns
        -------
        FILME
            Retorna o título do filme.

        '''
        return self._titulo
            
    @titulo.setter
    def set_titulo(self, nome):
        '''
        Setter do título do filme

        Parameters
        ----------
        nome : str
            Define o nome do filme.

        Returns
        -------
        None.

        '''
        self._titulo = nome
         
    @property
    def classificacao(self):
        '''
        Getter da classificação do filme

        Returns
        -------
        FILME
            Retorna o filme.

        '''
        return self._classificacao
    
    @classificacao.setter
    def set_classificacao(self, idade):
        '''
        Setter da classificação do filme

        Parameters
        ----------
        idade : int
            Define a idade que pode assistir ao filme, classificação etária.

        Returns
        -------
        None.

        '''
        self._classificacao = int(idade)
         
    @property
    def duracao(self):
        '''
        Getter da duração do filme

        Returns
        -------
        FILME
            Retorna a duração do filme.

        '''
        return self._duracao
    
    @duracao.setter
    def set_duracao(self, tempo):
        '''
        Setter da duração do filme

        Parameters
        ----------
        tempo : int
            Define o tempo de duração do filme.

        Returns
        -------
        None.

        '''

        self._duracao = int(tempo)       
        
"""   
#TESTES DA CLASSE         

filme01 = Filme("Thor", 12, 120)
print(filme01.classificacao)

filme01._duracao = 90
filme01._classificacao = 0
print(filme01.duracao, filme01.classificacao)
"""