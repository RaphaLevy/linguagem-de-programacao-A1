from datetime import date, time, datetime, timedelta
from Filme import Filme

class Sessao:
    '''A classe Sessao define uma sessão por sua Data, Hora e Filme.'''
    def __init__(self, data, filme, nro_assentos):
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
        #self._hora = hora #'HH:MM:SS'
        self._filme = filme
        self.nro_assentos = nro_assentos
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
        
        self._data = datetime.fromisoformat(val)
    
    
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

    def ocupar_assento(self, numero):
        '''
        Função que verifica e ocupa o assento solicitado

        Parameters
        ----------
        numero : int
            Descreve o assento que vai ser ocupado.

        Returns
        -------
        int
            Retorna 1 caso esteja disponível, e retorna 0 caso esteja indisponível.

        '''
        if numero in self.assentos:
            self.assentos.remove(numero)
            print(f"Assento {numero} reservado com sucesso")
            return 1
        else:
            print(f"Assento {numero} não está disponível")
            return 0
        
    def to_str(self):
        '''
        Print das informações da sessão.

        Returns
        -------
        None.

        '''
        print(f" Filme: {self.filme.titulo}\n Data: {self.data}\n Duração: {self.filme.duracao}\n\n")
        
    def ingressos_vendidos(self):
        '''
        Função que retorna o número de ingressos vendidos

        Returns
        -------
        int
            Retorna a quantidade de assentos que foram vendidos.

        '''
        return self.nro_assentos - len(self.assentos)
    
    def calcular_termino(self):
        '''
        Calcula o término da sessão

        Returns
        -------
        datetime
            Retorna o horário que vai terminar a sessão.

        '''
        #print(self.filme.duracao)
        
        aux = self.filme.duracao/60
        aux = str(aux)
        horas, minutos = aux.split(".")
        horas = int(horas)
        minutos = int(minutos)
        minutos *= 6
        duracao = timedelta(hours = horas, minutes = minutos) #(minute = minutos, hour = horas)
        inicio = datetime.fromisoformat(self.data)
        return inicio + duracao
        
