from Autor import Autor
from Livro import Livro
from PilhaLivros import PilhaLivros

pilha = PilhaLivros()
pilha.imprimir()

# Criando autores
autor1 = Autor("Machado de Assis", 1839)
autor2 = Autor("Clarice Lispector", 1920)
autor3 = Autor("Machado de Assis", 1839)

# Criando livros
livro1 = Livro("Dom Casmurro", 256, autor1)
livro2 = Livro("A Hora da Estrela", 88, autor2)
livro3 = Livro("Memórias Póstumas de Brás Cubas", 208, autor3)

# Adicionando livros na pilha
pilha.add(livro1)
pilha.add(livro2)
pilha.add(livro3)

# Removendo o livro do topo
pilha.remover()

# Consultando livros de um autor
pilha.contar_por_autor("Machado de Assis")
pilha.contar_por_autor("Clarice Lispector")
pilha.contar_por_autor("Jorge Amado")
