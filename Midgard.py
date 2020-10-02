from Sala import Sala
from Filme import Filme
from Sessao import Sessao

class Midgard(Sala):
    ''' A classe Midgard define a sala de cinema Midgard por seu número de assentos e preço'''
    MAX_ASSENTOS = 120
    MIN_ASSENTOS = 60
    def __init__(self, nro_assentos, preco):
        '''
        Init da classe Midgard, um tipo de sala de cinema

        Parameters
        ----------
        nro_assentos : int
            Delimita o número de assentos da sala Midgard.
        preco : float
            Delimita o preço dos ingressos dos assentos na sala Midgard.

        Returns
        -------
        None.

        '''
        super().__init__(nro_assentos, preco)
        self.sessoes = []

        
    @property
    def nro_assentos(self):
        '''
        Getter do número de assentos da sala Midgard

        Returns
        -------
        MIDGARD
            Getter do número de assentos da sala Midgard.

        '''
        return self._nro_assentos
        
    @nro_assentos.setter
    def set_nro_assentos(self, qtd_assentos):
        '''
        Setter do número de assentos da sala Midgard

        Parameters
        ----------
        qtd_assentos : int
            Setter para definir o número de assentos da sala Midgard.

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
            
 