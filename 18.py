a = float(input("Digite um número"))
b = float(input("Digite um número"))


def menor(a,b):
    if a > b:
        print(f"{b} é o menor número")
    elif a < b: 
        print(f"{a} é o menor número")
    elif a == b:
        print(f"os numero são iguais")
        
menor(a,b)
