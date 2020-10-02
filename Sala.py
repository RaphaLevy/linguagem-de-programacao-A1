from Sessao import Sessao
from Filme import Filme
from datetime import date, time, datetime, timedelta

class Sala():
    ''' A classe sala define uma sala de cinema por seu número de assentos e preço.'''
    MAX_ASSENTOS = 120
    MIN_ASSENTOS = 15
    def __init__(self, nro_assentos, preco):
        '''
        Init da classe Sala

        Parameters
        ----------
        nro_assentos : int
            Define o número de assentos de uma sala de cinema.
        preco : float
            Define o valor do ingresso por assento de uma sala de cinema.

        Returns
        -------
        None.

        '''
        #self._tipo(tipo)
        self._nro_assentos = nro_assentos
        #self._assentos = range(self.nro_assentos)
        self._preco = preco
        self.sessoes = []
        
    @property
    def nro_assentos(self):
        '''
        Getter do número de assentos

        Returns
        -------
        int
            Retorna o número de assentos da sala.

        '''
        return self._nro_assentos
    
    @nro_assentos.setter
    def set_nro_assentos(self, qtd_assentos):
        '''
        Setter do número de assentos

        Parameters
        ----------
        qtd_assentos : int
            Define a quantidade de assentos de uma sala de cinema.

        Returns
        -------
        int
            Retorna 1 de acordo com a lotação da sala.

        '''
        if qtd_assentos >= self.MIN_ASSENTOS and qtd_assentos <= self.MAX_ASSENTOS:
            self._nro_assentos = qtd_assentos
           #self._assentos = range(self.nro_assentos)
            return 1
        else:
            del self 
        
    @property 
    def preco(self):
        '''
        Getter do preço da sala de cinema

        Returns
        -------
        int
            Retorn o valor do preço de um ingresso por assento de uma sala de cinema.

        '''
        return self._preco
    
    @preco.setter
    def set_preco(self, valor):
        '''
        Setter do preço por assento da sala de cinema

        Parameters
        ----------
        valor : float
            Define o valor de um ingresso por assento na sala de cinema.

        Returns
        -------
        None.

        '''
        self._preco = valor
    
    def add_sessao(self, nova_sessao):
        '''
        for cada_sessao in self.sessoes:
            if cada_sessao.data == nova_sessao.data:
                if (nova_sessao.hora >= cada_sessao.hora and 
                    nova_sessao <= (cada_sessao.hora.timedelta(minutes = Sessao.filme.duracao))
                    ):
                        print("entrou")
                else:
                    print("n pode não")
            else:
                print("foi aqui ó")
        print("aeo")
        '''
        
        
        if len(self.sessoes) == 0:
            print("Sessão adicionada com sucesso")
            print(nova_sessao.to_str())
            self.sessoes.append(nova_sessao)
            return 1
        else:
            for cada_sessao in self.sessoes:
                if datetime.fromisoformat(nova_sessao.data) >= datetime.fromisoformat(cada_sessao.data) and datetime.fromisoformat(nova_sessao.data) < cada_sessao.calcular_termino():
                    print("Erro ao inserir nova sessão:")
                    print(f"Já existe uma sessão entre {cada_sessao.data} e {cada_sessao.calcular_termino()}")
                    return 0
                else:
                    print("Sessão adicionada com sucesso")
                    print(nova_sessao.to_str())
                    self.sessoes.append(nova_sessao)
                    return 1
                
    def rm_sessao(self, sessao):
        """
        remove uma das sessões administradas pelo Administrador
            
        ----------
        sessão a ser removida.
        """
        
        self.sessoes.remove(sessao)                
                    
    def verificar_programacao(self):
         '''
        Verifica a programação da sala, se há sessões múltiplas.

        Returns
        -------
        None.

        '''
        for cada_sessao in self.sessoes:
            cada_sessao.to_str()
                
            
    def calcular_receita(self, sessao):
        '''
        Calcula a receita da sessão daquela sala de cinema

        Parameters
        ----------
        sessao : int
            Sessão da sala de cinema.

        Returns
        -------
        float
            Retorna o valor total da receita da sessão especificada.

        '''
        return sessao.ingressos_vendidos() * self.preco
            
    '''
    @assentos.setter
    def set_assentos(self, nro_assentos):
        self.assentos = []
        for i in range(0, self.nro_assentos):
            self.assentos.append(1)
    '''

