def encontrarPessoaMaisVelha(pessoas):
    pessoa_mais_velha = max(pessoas, key=lambda pessoa: pessoa['idade'])
    return pessoa_mais_velha['nome']

pessoas_exemplo = [
    {"nome": "Lucas", "idade": 69},#69papai
    {"nome": "Rodolfo", "idade": 29},
    {"nome": "Petegronji", "idade": 17},
]
resultado = encontrarPessoaMaisVelha(pessoas_exemplo)
print(resultado)