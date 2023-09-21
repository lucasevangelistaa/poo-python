from livro import Livro

livro1 = Livro("Java", "James Gosling", "new1", 213)
livro2 = Livro("Python", "Guido Van Rossum", "new2", 400)
livro3 = Livro("C++", "Bjarne Stroustrup", "new3", 500)
livro4 = Livro("Assembly", "Ken Thompson", "new4", 100)

print(f'O titulo do livro é {livro1.titulo}')
print(f'O autor do livro é {livro2.autor}')
print(f'A editora é {livro3.editora}')
print(f'Esse livro tem {livro4.qtde_paginas} páginas')

livro1.qtde_paginas = 400
livro2.autor = "Lucas"
print(livro2.autor)
print(livro1.qtde_paginas)

