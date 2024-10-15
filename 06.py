def calcularImpostoRenda(salario_bruto):
    if salario_bruto <= 1903.98:
        imposto = 0
    elif salario_bruto <= 2826.65:
        imposto = salario_bruto * 0.075
    elif salario_bruto <= 3751.05:
        imposto = salario_bruto * 0.15
    elif salario_bruto <= 4664.68:
        imposto = salario_bruto * 0.225
    else :
        imposto = salario_bruto * 0.275
    return imposto


salario_bruto = 5000
imposto = calcularImpostoRenda(salario_bruto)
print(f"o valor do imposto de renda e {imposto}")