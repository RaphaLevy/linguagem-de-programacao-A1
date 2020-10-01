class Filme:
    def __init__(self, titulo, classificacao, duracao): 
        self.titulo = titulo
        self.classificacao = int(classificacao)
        self.duracao = float(duracao)
        
    @property
    def titulo(self):
      return self.titulo
            
    @titulo.setter
    def set_titulo(self, titulo):
         self.titulo = titulo
         
    @property
    def classificacao(self):
        return self.classificacao
    
    @classificacao.setter
    def set_classificacao(self, classificacao):
         self.classificacao = int(classificacao)
         
    @property
    def duracao(self):
        return self.duracao
    
    @duracao.setter
    def set_duracao(self, duracao):
         self.duracao = int(duracao)       
        