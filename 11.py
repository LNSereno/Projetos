numero = int(input("voce quer a tabuada de que numero ? "))

def gerarTabuada(numero):
    for c in range(1, 11):
        print(f"{numero} x {c} = {numero * c}")
gerarTabuada(numero)