from Filme import Filme
from Sala import Sala
from Asgard import Asgard
from Midgard import Midgard
from Sessao import Sessao
from Administrador import Administrador
from Guerreiro import Guerreiro

import mod
from datetime import date, time, datetime, timedelta

continua = True
while continua:
    opcao = input("""Selecione a opção
    1-verificar ingressos
    2-verificar programação
    3-adicionar sessão
    4-remover sessão
    5-encerrar
          """)

    if opcao == "5":
        print("Programa encerrado")
        continua = False
    elif opcao == "4":
        
        
