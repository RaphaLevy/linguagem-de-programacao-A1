from Filme import Filme
from Sala import Sala
from Asgard import Asgard
from Midgard import Midgard
from Sessao import Sessao
from Administrador import Administrador
from Guerreiro import Guerreiro

import mod
from datetime import date, time, datetime, timedelta

filmes = [Filme("Rei Leão", 0, 90), Filme("Jurassic Park", 14, 90), Filme("Vida de Inseto", 0, 60), Filme("Godzilla", 12, 120)] 
salas = [Midgard(100, 10), Midgard(90, 15), Asgard(25, 40), Asgard(20, 50)]
salas[0].sessoes = [Sessao("2020-02-02 12:00", filmes[0], salas[0].nro_assentos), Sessao("2020-02-02 14:00", filmes[0], salas[0].nro_assentos)]
salas[2].sessoes = [Sessao("2020-02-02 12:00", filmes[1], salas[2].nro_assentos)]

#aqui é só para ele gerar uma receita na hora de testar
salas[0].sessoes[0].assentos.remove(1)
salas[0].sessoes[0].assentos.remove(3)
salas[0].sessoes[0].assentos.remove(10)
salas[0].sessoes[1].assentos.remove(1)
salas[2].sessoes[0].assentos.remove(5)

'''
salas[0].add_sessao(Sessao("2020-02-02 12:00:00", filmes[0], salas[0].nro_assentos))
salas[0].add_sessao(Sessao("2020-02-02 13:30:00", filmes[0], salas[0].nro_assentos))
#print(salas[0].verificar_programacao())
#print(datetime.fromisoformat("2020-02-02 12:00:00"))
'''

mod.iniciar()

print()
continuar =  True
while continuar:
    opcao = input("""Bom dia caro Guerreiro, o que deseja fazer?
    1- Comprar um ingresso
    2- Ver filmes disponíveis
    3- Comprar pipoca
    4- Encerrar programa
    
opção: """)
    if opcao == "1":
        mod.comprar_ingresso(salas)
    elif opcao == "2":
        mod.mostrar_sessoes(salas)
    elif opcao == "4":
        print("Bom filme!")
        continuar = False
    elif opcao == "3":
        mod.comprar_pipoca()
    else:
        print("Opção inválida, poderia repetir por favor?")
    