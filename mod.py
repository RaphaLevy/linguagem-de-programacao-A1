def comprar_ingresso(salas):
    cont = 0
    for cada_sala in salas:
        for cada_sessao in cada_sala.sessoes:
            cont += 1
            pass