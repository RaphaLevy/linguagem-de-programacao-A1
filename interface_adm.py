from Filme import Filme
from Sala import Sala
from Asgard import Asgard
from Midgard import Midgard
from Sessao import Sessao
from Administrador import Administrador
from Guerreiro import Guerreiro

from datetime import date, time, datetime, timedelta
import mod

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

continua = True
while continua:
    opcao = input("""Selecione a opção
    1-verificar ingressos
    2-verificar programação
    3-adicionar sessão
    4-remover sessão
    5-encerrar sessão
    6-encerrar a execução do programa
opção: """)

    if opcao == "6":
        print("Programa encerrado")
        continua = False
    elif opcao == "5":
        mod.encerrar_sessao(salas)
    elif opcao == "4":
        sala, sessao = mod.selecionar_sala_sessao(salas)
        sala.rm_sessao(sessao)
    elif opcao == "3":
        i_sala = int(input("insira o número da sala na qual deseja adicionar a nova sessão:"))
        sala = salas[i_sala - 1]
        data = input("insira a data da sessão (YYYY-MM-DD HH:MM:SS):")
        cont = 0
        for filme in filmes:
            cont += 1
            print(str(cont) + "-" + filme.titulo)
        i_filme = int(input("insira o número do filme da nova sessão:"))
        filme = filmes[i_filme - 1]
        sala.add_sessao(Sessao(data, filme, sala.nro_assentos))
    elif opcao == "2":
        mod.mostrar_sessoes(salas)
    elif opcao == "1":
        sala, sessao = mod.selecionar_sala_sessao(salas)
        ingressos = sessao.ingressos_vendidos()
        print(f"Foram vendidos {ingressos} ingressos para a sessão")
    else:
        print("Opção inválida, poderia repetir por favor?")
