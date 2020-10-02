def comprar_ingresso(salas):
    mostrar_sessoes(salas)
    input("favor, insira o número da sala:")
    
    
        
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
        