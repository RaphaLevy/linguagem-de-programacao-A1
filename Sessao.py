from datetime import date, time
from Filme import Filme

class Sessao:
    '''A classe Sessao define uma sessão por sua Data, Hora e Filme.'''
    def __init__(self, data, hora, filme, nro_assentos):
        """
        Descrição da função init

        Parametros
        ----------
        data : date
            Data da sessão.
        hora : time
            Hora da sessão.
        filme : string
            Filme da sessão.
        Returns
        -------
        None.

        """
        
        self._data = data #'AAAA-MM-DD'
        self._hora = hora #'HH:MM:SS'
        self._filme = filme
        self.assentos = []
        for i in range(nro_assentos):
            self.assentos.append(i + 1)
            
    @property
    def data(self):
        '''
        Descrição da função data

        Returns
        -------
        string
            Getter que retorna a data da sessão.

        '''
        
        return self._data
    
    @data.setter
    def set_data(self, val):
        '''
        Setter da data da sessão

        Parameters
        ----------
        val : str
            Valor da data da sessão.

        Returns
        -------
        None.

        '''
        
        self._data = date.fromisoformat(val)
    
    @property 
    def hora(self):
        '''
        Getter da hora da sessão

        Returns
        -------
        str
            Getter que retorna a hora da sessão.

        '''
        
        return self._hora
    
    @hora.setter
    def set_hora(self, tempo):
        '''
        Setter da hora da sessão.

        Parameters
        ----------
        tempo : time
            Hora da sessão.

        Returns
        -------
        None.

        '''
        
        self._hora = time.fromisoformat(tempo)
    
    @property
    def filme(self):
        '''
        Getter do filme

        Returns
        -------
        string
            Getter que retorna o nome do filme da sessão.

        '''
        
        return self._filme
    
    @filme.setter
    def set_filme(self, ver):
        '''
        Setter do filme

        Parameters
        ----------
        ver : FILME
            Objeto do tipo FILME.

        Returns
        -------
        None.

        '''
        
        self.filme = ver

    def ocupar_acento(self, numero):
        if numero in self.assentos:
            aux = self.assentos.pop(numero - 1)
            print(f"Assento {aux} {numero} {aux + 1} {numero - 1} reservado com sucesso")
            return 1
        else:
            print("Assento {numero} não está disponível")
            return 0
        
    def to_str(self):
        print(f""" Filme: {self.filme.titulo}\n Data: {self.data} às {self.hora}\n Duração: {self.filme.duracao}""")
'''    
f = Filme("Mingau", 18, 60)
s = Sessao("2020-02-02", "20:00:00", f, 30)

print(s.hora)
print(s.data)
print(s.assentos)

print(s.ocupar_acento(3))
print(s.assentos)
print(s.ocupar_acento(3))
print(s.to_str())
'''