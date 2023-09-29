from livro import Livro

#Objetos da Classe Livro
livro1 = Livro("Java", "James Gosling", "new1", 213)
livro2 = Livro("Python", "Guido Van Rossum", "new2", 400)
livro3 = Livro("C++", "Bjarne Stroustrup", "new3", 500)
livro4 = Livro("Assembly", "Ken Thompson", "new4", 100)

#Mostra os dados sobre o livro1
print(f'Título: {livro1.titulo}')
print(f'Nome do autor: {livro1.autor}')
print(f'Editora: {livro1.editora}')
print(f'Esse livro tem {livro1.qtde_paginas} páginas')

#Altera a quantidade de páginas do livro1
livro1.qtde_paginas = 400

#Mostra os dados atualizados
print(f'Título: {livro1.titulo}')
print(f'Nome do autor: {livro1.autor}')
print(f'Editora: {livro1.editora}')
print(f'Esse livro tem {livro1.qtde_paginas} páginas')