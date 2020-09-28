# -*- coding: utf-8 -*-

class Cinema():
  def __init__(self, regiao, empresa, preco_midgard, preco_asgard):  
    self.regiao = regiao
    self.empresa = empresa  
    self.preco_midgard = float(preco_midgard)
    self.preco_asgard = float(preco_asgard)

class Sala():
  def __init__(self, tipo, numero_assentos, lista):
    self.tipo = tipo
    self.numero_assentos = int(numero_assentos)
    self.lista = []
    
    
    
    
    
    
    
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
    
def Compra(self, tipo, numero_assentos):
      if self.tipo == "Midgard":
         while 60 <= self.numero_assentos <= 120:
             self.numero_assentos -= 1
         assentos_midgard = []
         for cada_numero in range (60,self.numero_assentos+1):
             assentos_midgard.append(cada_numero)    
      if self.tipo == "Asgard":
         while 15 <= self.numero_assentos <= 30:
             self.numero_assentos -= 1
         assentos_asgard = []
         for cada_numero in range (1,self.numero_assentos+1):
             assentos_asgard.append(cada_numero)    
         

