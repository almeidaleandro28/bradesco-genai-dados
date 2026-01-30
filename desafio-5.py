def check( enter ):
    
    values = enter.split(" ")

    abertura = int( values[0] )
    fechamento = int( values[1] )

    if ( fechamento > abertura ):
        print( "ALTA" )
    elif ( fechamento < abertura):
        print( "BAIXA")
    else: 
        print("ESTAVEL")
        

check( "10 15")