def calcularPrecoProduto(valor_custo, margem_lucro, valor_frete):
    valor_lucro = valor_custo * (margem_lucro / 100)
    preco_venda = valor_custo + valor_lucro + valor_frete    
    return preco_venda

valor_custo = 100.00 
margem_lucro = 20    
valor_frete = 10.00  

preco_venda = calcularPrecoProduto(valor_custo, margem_lucro, valor_frete)
print(f"O preço de venda do produto é: R$ {preco_venda:.2f}")