def filtrarCarrosPorAno(carros, ano_especifico):
    return [carro for carro in carros if carro['ano'] > ano_especifico]

carros_exemplo = [
    {"marca": "bugatti", "modelo": "golfeveron", "ano": 2010},
    {"marca": "momonas", "modelo": "bahiacruzada", "ano": 1996},
    {"marca": "charlie", "modelo": "Chorao", "ano": 2013},
]
resultado = filtrarCarrosPorAno(carros_exemplo, 1996)
print(resultado)