import desafio6 

try:
    text = desafio6.to_uppercase("leandro")
    print(f"Name with upper case : {text}")
except Exception as e:
    print(f'Error processing - {e}')