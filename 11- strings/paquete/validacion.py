def validar_numero(numero: str)-> bool:

    '''
    '''

    if ord(numero) < 58 and ord(numero) > 47:
        return True
    else:
        return False