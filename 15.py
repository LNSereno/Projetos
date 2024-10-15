def encontrarPalavraMaisLonga(s):
    palavras = s.split()
    palavra_mais_longa = max(palavras, key=len)
    return palavra_mais_longa

string_exemplo = 'Sera que o professor olha codigo por codigo ??'
resultado = encontrarPalavraMaisLonga(string_exemplo)
print(f"Palavra mais longa: {resultado}")