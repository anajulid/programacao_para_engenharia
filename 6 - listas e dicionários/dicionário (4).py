livros = {}

for i in range(5):
    nome = input("digite o nome do livro: ")
    autor = input("digite o autor do livro: ")
    livros.update({nome:autor})

print("lista dos livros com nome e autor: ", livros)
