import random

def advinheNumero():
    numero_secreto = random.randint(1, 100)
    tentativas = 0
    acertou = False
    
    print("Tente adivinhar o número entre 1 e 100!")
    
    while not acertou:
        tentativa = int(input("Digite sua tentativa: "))
        tentativas += 1        
        if tentativa < numero_secreto:
            print("O número correto é maior.")
        elif tentativa > numero_secreto:
            print("O número correto é menor.")
        else:
            acertou = True
            print(f"Você adivinhou o número {numero_secreto} em {tentativas} tentativas.")
advinheNumero()