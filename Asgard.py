from Sala import Sala

class Asgard(Sala):
    ''' A classe Asgard define a sala de cinema Asgard por seu número de assentos e preço'''
    MAX_ASSENTOS = 30
    MIN_ASSENTOS = 15
    def __init__(self, nro_assentos, preco):
        '''
        Init da classe Asgard, um tipo de sala de cinema.

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
        Getter do número de assentos da sala Asgard

        Returns
        -------
        int
            Retorna o número da assentos da sala Asgard.

        '''
        return self._nro_assentos
    
    @nro_assentos.setter
    def set_nro_assentos(self, qtd_assentos):
        '''
        Setter do número de assentos

        Parameters
        ----------
        qtd_assentos : int
            Setter para definir o número de assentos da sala Asgard.

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
            
#Testes da classe
'''   
asg = Asgard(int(20), int(20))
print(asg.nro_assentos)

asg1 = Asgard(int(25), int(30))            
'''