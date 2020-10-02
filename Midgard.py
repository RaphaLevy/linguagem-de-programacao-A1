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
            
            
#Testes da classe            
'''
mid = Midgard(int(90), int(20))
#print(mid.nro_assentos)

mid1 = Midgard(int(50), int(30))

f = Filme("Mingau", 18, 60)
s = Sessao("2020-02-02", "20:00:00", f, 30)
f1 = Filme("Abacate", 10, 120)
s2 = Sessao("2020-02-02", "21:00:00", f1, 30)
s3 = Sessao("2020-02-02", "23:00:00", f1, 30)

mid.sessoes.append(s)
mid.sessoes.append(s2)
mid.sessoes.append(s3)


#print(mid.verificar_programacao())

mid.rm_sessao(s2)

#print(mid.verificar_programacao())



f = Filme("Mingau", 18, 60)
s = Sessao("2020-02-02", "20:00:00", f, 30)

#print(s.hora)
#print(s.data)
#print(s.assentos)

for i in range(10):
    s.ocupar_assento(i)
    
print(s.ingressos_vendidos())
print(s.assentos)
print(mid.calcular_receita(s))
'''