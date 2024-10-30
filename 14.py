def positivo():
    numero = int(input("Digite um numero"))
    if numero > 0:
        return True
    else:
        return False

conta = positivo()

print(conta)
