class livro:
    def __init__(self, titulo,autor, paginas, disponivel):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas
        self.disponivel = disponivel

    def descrição(self):
        print(f"Titulo: {self.titulo}")
        print(f"Autor: {self.autor}")
        print(f"paginas: {self.paginas}")
        print(f"disponivel: {self.disponivel}")

    def emprestar(self):
        if self.disponivel == True:
         self.disponivel = False
        else:
            print("Livro Emprestado!")

    def devolver(self):
        if self.disponivel == False:
            print("Livro Devolvido!")
            self.disponivel = True
        else:
            print("O livro já foi devolvido!")

l1 = livro("Robinson Crusoe","Daniel Defoe",368,False)

l1.emprestar()
l1.descrição()
print("="*70)
l1.devolver()
l1.descrição()