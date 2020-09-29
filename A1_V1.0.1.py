# -*- coding: utf-8 -*-

class Cinema():
  def __init__(self, regiao, empresa, preco_midgard, preco_asgard):  
    self.regiao = regiao
    self.empresa = empresa  
    self.preco_midgard = float(preco_midgard)
    self.preco_asgard = float(preco_asgard)

class Sala():
  def __init__(self, tipo, assentos_sala, lista):
    self.tipo = tipo
    self.assentos_sala = int(assentos_sala)
    self.lista = []
    
    @assentos_sala.setter  
    def assentos_sala(self, lista_assentos):
        self._assentos_sala = lista_assentos
        lista_assentos = []
        for numero in range (1, assentos_sala+1):
            lista_assentos.append(1)
            i = ""
            if lista_assentos[i - 1]:
                print("compra sucedida")
                "sala1.assentos[i-1] = 0"
            
        
    
class Filme():
  def __init__(self, titulo, classificacao, duracao): 
    self.titulo = titulo
    self.classificacao = int(classificacao)
    self.duracao = float(duracao)
      
class Sessao():
  def __init__(self, data, hora, tipo, numero_assentos):
    super().__init__(tipo, numero_assentos)
    self.data = data
    self.hora = hora
    
def Compra(self, tipo, assentos_sala):
      if self.tipo == "Midgard":
         while 60 <= self.assentos_sala <= 120:
             self.assentos_sala -= 1
         assentos_midgard = []
         for cada_numero in range (60,self.assentos_sala+1):
             assentos_midgard.append(cada_numero)    
      if self.tipo == "Asgard":
         while 15 <= self.assentos_sala <= 30:
             self.assentos_sala -= 1
         assentos_asgard = []
         for cada_numero in range (1,self.assentos_sala+1):
             assentos_asgard.append(cada_numero)    
         

