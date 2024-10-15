from datetime import datetime

def calcularIdade(ano_nascimento):
    ano_atual = datetime.now().year
    idade = ano_atual - ano_nascimento
    return idade
ano_nascimento = 2006
idade = calcularIdade(ano_nascimento)
print(f"A minha idade e {idade} anos")