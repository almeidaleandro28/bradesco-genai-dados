def trancacao( enter ):

    if not isinstance(enter, str):
        raise TypeError(f"Entrada inválida: Esperava string, mas recebeu {type(enter).__name__}")
    if not enter.strip():
        raise ValueError("The paramenter cannot be empty.")

    try:
        list_clear = list( dict.fromkeys( enter.split() ) )
        return " ".join( list_clear )
    except Exception as e:
        return f"Error -- {e}"


    # lista = enter.split() 
    # list_limpa = []
    # lista_aux = set()

    # for values in lista:
    #     if values not in lista_aux:
    #         list_limpa.append( values )
    #         lista_aux.add( values )
    
    # return print( " ".join(list_limpa))
        

try:
#    print( trancacao( "TX1001 TX1002 TX1001 TX1003" ) )
#    print( trancacao( " " ) )
   print( trancacao( 12345) )
except Exception as  e:
    print(f"show err -- {e}")