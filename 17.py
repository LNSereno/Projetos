def filtrarStringsLongas(strings):
    return [s for s in strings if len(s) > 5]

lista_exemplo = ["cotoco", "cachorro", "melao", "pornografia", "mar", "verdiosa"]
resultado = filtrarStringsLongas(lista_exemplo)
print(resultado)