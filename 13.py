def verificarPropriedade(objeto, propriedade):
    return hasattr(objeto, propriedade)

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

pessoa = Pessoa("João", 30)

print(verificarPropriedade(pessoa, "nome"))
print(verificarPropriedade(pessoa, "idade"))
print(verificarPropriedade(pessoa, "endereco"))