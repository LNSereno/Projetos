def imprimirQuadro(strings):
    max_length = max(len(s) for s in strings)
    border = '*' * (max_length + 4)
    
    print(border)
    for s in strings:
        print(f"* {s.ljust(max_length)} *")
    print(border)

lista_exemplo = ["Hello", "World", "in", "a", "frame"]
imprimirQuadro(lista_exemplo)