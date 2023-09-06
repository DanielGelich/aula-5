class Livro:
  def __init__(self, titulo):
    self.titulo = titulo


def adicionar_livro(biblioteca, livro):
  biblioteca.append(livro)


def listar_livros(biblioteca):
  for livro in biblioteca:
    print(livro.titulo)


def main():
  biblioteca = []

  adicionar_livro(biblioteca, Livro("2001: Uma Odisseia no Espaço"))
  adicionar_livro(biblioteca, Livro("O Guia do Mochileiro das Galáxias"))
  adicionar_livro(biblioteca, Livro("A Fundação"))

  listar_livros(biblioteca)

if __name__ == "__main__":
  main()