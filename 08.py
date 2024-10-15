def contarDigitosParesImpares(numero):
    numero_str = str(numero)
    pares = 0
    impares = 0
    
    for c in numero_str:
        if int(c) % 2 == 0:
            pares += 1
        else:
            impares += 1
    
    return pares, impares

numero = 1234567890
pares, impares = contarDigitosParesImpares(numero)
print(f"Número de dígitos pares: {pares}")
print(f"Número de dígitos ímpares: {impares}")