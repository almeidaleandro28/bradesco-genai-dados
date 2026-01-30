def to_uppercase( name: str  ) -> str:
     
    if not isinstance( name, str):
        raise TypeError("The paramenter 'name' must be a string")
    if not name.strip():
        raise ValueError("The paramenter cannot be empty.")

    return name.upper()

# print( to_uppercase( 'leandro'))


# if __name__ ==  "__main__":

#     try:
#         text = to_uppercase("leandro")
#         print(f"Name with upper case : {text}")
#     except Exception as e:
#         print(f'Error processing - {e}')