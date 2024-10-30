def par():
    numero = int(input("Digite um numero"))
    if numero %2 != 0:
        return True
    else:
        return False

resultado = par()
print(resultado)
