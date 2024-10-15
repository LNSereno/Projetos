def filtrarLivrosPorAutor(livros, autor_desejado):
    return [livro for livro in livros if livro['autor'] == autor_desejado]

livros_exemplo = [
    {"Livro A","Autor 1", 2020},
    {"Livro B","Autor 2", 2021},
    {"Livro C","Autor 1", 2022},
]
resultado = filtrarLivrosPorAutor(livros_exemplo, "Autor 1")
print(resultado)