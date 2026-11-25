class Livro:
    def __init__(self,titulo,autor,isbn,disponivel):
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn
        self.disponivel = disponivel

    def emprestar(self):
        if self.disponivel == True:
            self.disponivel = False
            print(f"O Livro {self.nome} foi emprestado!") 
        else: 
            print(f"O Livro {self.nome} esta indisponivel!")

    def devolver(self):
        if self.disponivel == False:
            self.disponivel = True
            print(f"O Livro {self.nome} foi Devolvido!")
        else:
            print(f"O Livro {self.nome} já foi Devolvido!")

    def descrição(self):
        print(f"Titulo: {self.nome}"
              f"Autor: {self.autor}"
              f"isbn: {self.isbn}"
              f"disponivel: {self.disponivel}")


