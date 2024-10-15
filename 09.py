def calcularMediaAlunos(alunos):
    soma_notas = 0
    for aluno in alunos:
        soma_notas += aluno['nota']
    
    media = soma_notas / len(alunos)
    return media
alunos = [
    {'nome': 'Alice', 'nota': 8.5},
    {'nome': 'Bob', 'nota': 7.0},
    {'nome': 'Charlie', 'nota': 9.0},
    {'nome': 'Diana', 'nota': 6.5}
]
media = calcularMediaAlunos(alunos)
print(f"A média das notas dos alunos é: {media}")