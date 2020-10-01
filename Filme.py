class Filme:
    def __init__(self, titulo, classificacao, duracao): 
        self._titulo = titulo
        self._classificacao = classificacao
        self._duracao = duracao
        
    @property
    def titulo(self):
        return self._titulo
            
    @titulo.setter
    def set_titulo(self, nome):
         self._titulo = nome
         
    @property
    def classificacao(self):
        return self._classificacao
    
    @classificacao.setter
    def set_classificacao(self, idade):
         self._classificacao = int(idade)
         
    @property
    def duracao(self):
        return self._duracao
    
    @duracao.setter
    def set_duracao(self, tempo):
         self._duracao = int(tempo)       
        
"""   
#TESTES DA CLASSE         

filme01 = Filme("Thor", 12, 120)
print(filme01.classificacao)

filme01._duracao = 90
filme01._classificacao = 0
print(filme01.duracao, filme01.classificacao)
"""