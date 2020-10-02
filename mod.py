def comprar_ingresso(salas):
    mostrar_sessoes(salas)
    sala, sessao = selecionar_sessao()
    print(sessao.assento)
    assento = int(input("Selecione o assento:"))
    
    
    
        
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
    mostrar_sessoes(salas)
    i = int(input("favor, insira o número da sala:"))
    try:
        sala[i - 1].verificar_programacao()
        j = int(input("favor, insira o número da sessão:"))
        return sala[i - 1], sala[i - 1].sessoes[j - 1]
    except:
        print("Parece que a sala não existe, tente novamente")
