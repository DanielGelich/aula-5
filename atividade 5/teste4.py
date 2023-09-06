def test_adicionar_livro():
  biblioteca = []

  adicionar_livro(biblioteca, Livro("2001: Uma Odisseia no Espaço"))

  assert len(biblioteca) == 1
  assert biblioteca[0].titulo == "2001: Uma Odisseia no Espaço"


def test_remover_livro():
  biblioteca = []

  adicionar_livro(biblioteca, Livro("2001: Uma Odisseia no Espaço"))

  remover_livro(biblioteca, "2001: Uma Odisseia no Espaço")

  assert len(biblioteca) == 0


def test_listar_livros():
  biblioteca = []

  adicionar_livro(biblioteca, Livro("2001: Uma Odisseia no Espaço"))
  adicionar_livro(biblioteca, Livro("O Guia do Mochileiro das Galáxias"))
  adicionar_livro(biblioteca, Livro("A Fundação"))

  listar_livros(biblioteca)

  assert biblioteca == ["2001: Uma Odisseia no Espaço", "O Guia do Mochileiro das Galáxias", "A Fundação"]