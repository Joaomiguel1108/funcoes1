a = float(input("Digite um número"))
b = float(input("Digite um número"))
c = float(input("Digite um número"))

def maior(a,b,c):
    if a > b and a > c:
        print(f"{a} é o maior número")
    elif b > a and b > c:
        print(f"{c} é o maior número")
    elif c > a and c >b:
        print(f"{c} é o maior número")
    elif a == b and a==c:
        print(f"os numero são iguais")
    elif a == b and a > c:
        print(f"{a} e {b} são os numeors maiores")
    elif c == b and a <  c:
        print(f"{c} e {b} são os numeors maiores")
    elif c == a and b <  c:
        print(f"{c} e {a} são os numeors maiores")
        
maior(a,b,c)
