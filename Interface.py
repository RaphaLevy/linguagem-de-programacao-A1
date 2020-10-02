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

salas[0].add_sessao(Sessao("2020-02-02 12:00:00", filmes[0], salas[0].nro_assentos))
salas[0].add_sessao(Sessao("2020-02-02 13:30:00", filmes[0], salas[0].nro_assentos))
#print(salas[0].verificar_programacao())
#print(datetime.fromisoformat("2020-02-02 12:00:00"))
