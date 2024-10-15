nome_carro = input("qual nome do carro ? ")
preco_carro = float(input("qual e o preco que voce gostaria de pagar pelo carro ? "))

print(f"O usuário gostaria de saber se o carro {nome_carro} está disponível e gostaria de pagar {preco_carro} reais nesse carro.")


nomes_carros = [
    "corola", "golf", "solado", "coco", "valorant",
    "burro", "solamento", "amasso", "caita", "jaules",
    "supra", "sopre", "fort", "boost", "valeuboi",
    "cocota", "marofa", "subote", "marculo", "equino"
]


for c in range (1):
    if nome_carro in nomes_carros:
        print("carro encontrado")
    else:
        print("carro nao encontrado")
        

if preco_carro < 10000:
    print("mal estado")
elif preco_carro < 30000:
    print("conservado")
elif preco_carro < 60000:
    print("seminovo")
else :
    print("novo")
    
def procurar_carro(nome_carro):
    carro_encontrado = False
    for carro in nomes_carros:
        if carro == nome_carro:
            carro_encontrado = True
            break
    if carro_encontrado:
        return "Carro encontrado"
    else:
        return "Carro não encontrado!"

resultado_procura = procurar_carro(nome_carro)
print(resultado_procura)

def avaliacao_carro(preco_carro):
    if preco_carro < 10000:
        return "mal estado"
    elif preco_carro < 30000:
        return "conservado"
    elif preco_carro < 60000:
        return "seminovo"
    else:
        return "novo"

resultado_avaliacao = avaliacao_carro(preco_carro)
print(resultado_avaliacao)

if resultado_procura == "Carro encontrado":
    qualidade_carro = avaliacao_carro(preco_carro)
    print(f"O usuário gostaria de um carro {nome_carro} na qualidade de {qualidade_carro}")

continuar = True
while continuar :
    nome_carro = input("Digite o nome do carro que deseja comprar: ")
    preco_carro = float(input("Digite o preço do carro que deseja conhecer: "))

    resultado_procura = procurar_carro(nome_carro)
    if resultado_procura == "Carro encontrado":
        qualidade_carro = avaliacao_carro(preco_carro)
        print(f"O usuário gostaria de um carro {nome_carro} na qualidade de {qualidade_carro}. O valor do {nome_carro} é o mesmo recebido anteriormente.")

    resposta = input("Deseja continuar? (sim/não): ")
    if resposta.lower() != "sim":
        continuar = False
        
    
    
    

        

        