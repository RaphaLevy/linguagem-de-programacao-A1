def comprar_ingresso(salas):
    sala, sessao = selecionar_sala_sessao(salas)
    print(sessao.assentos)
    assento = int(input("Selecione o assento:"))
    if sessao.ocupar_assento(assento):
        print("Compra finalizada")
    else:
        print("Erro ao efetuar compra")
    
    
    
        
def mostrar_sessoes(salas):
    cont = 0
    for cada_sala in salas:
        cont += 1
        print(f"---Sala{cont}---")
        cada_sala.verificar_programacao()
        print("-----------")

def iniciar():
    print("""
                   /^\\
          _.-`:   /   \\   :'-._
        ,`    :  |     |  :    '.
      ,`       \,|     |,/       '.
     /   BEM     `-...-`   VINDO  \\
    :              .'.              :
    |             . ' .             |
    |             ' AO'             |
    :              '.'              :
     \           ,-___-,           /
      `.       /'|     |'\       ,'
        `._   ;  |     |  ;   _,'
           `-.:  |     |  :,-'
                 |     |
        ____ _ _  _ ____ _  _ ____   
        |    | |\ | |___ |\/| |__|    
        |___ | | \| |___ |  | |  |     
    _  _ ____ _    _  _ ____ _    _    ____ 
    |  | |__| |    |__| |__| |    |    |__|    
     \/  |  | |___ |  | |  | |___ |___ |  |                                                                   
                
""")

def selecionar_sala_sessao(salas):
    try:
        mostrar_sessoes(salas)
        i = int(input("favor, insira o número da sala:"))
        print(i)
        salas[i - 1].verificar_programacao()
        j = int(input("favor, insira o número da sessão:"))
        print(j)
        return salas[i - 1], salas[i - 1].sessoes[j - 1]
    except IndexError:
        print("parece que a sessão ou a sala não existem, tente novamente")
    
