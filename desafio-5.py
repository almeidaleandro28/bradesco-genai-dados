def check(enter):

    if not isinstance(enter, str):
        raise TypeError(f"Entrada inválida: Esperava string, mas recebeu {type(enter).__name__}")
    if not enter.strip():
        raise ValueError("The paramenter cannot be empty.")

    try:
        price_open, price_close = map(int, enter.split())

        if price_open > price_close:
            return "ALTA"
        elif price_close < price_open:
            return "BAIXA"
        else:
            return "ESTAVEL"
            
    except ValueError:
        return "Erro: A string deve conter dois números inteiros separados por espaço."


try:
    # print(check("10 15"))  
    check("")
    # print(check(1015))    
except TypeError as e:
    print(e)
    



check( "10 15")