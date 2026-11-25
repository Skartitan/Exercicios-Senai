class Livro:
    def __init__(self,titulo,autor,isbn,disponivel):
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn
        self.disponivel = disponivel

    def emprestar(self):
        if self.disponivel == True:
            self.disponivel = False
            print(f"O Livro {self.titulo} foi emprestado!") 
        else: 
            print(f"O Livro {self.titulo} esta indisponivel!")

    def devolver(self):
        if self.disponivel == False:
            self.disponivel = True
            print(f"O Livro {self.titulo} foi Devolvido!")
        else:
            print(f"O Livro {self.titulo} já foi Devolvido!")

    def descrição(self):
        print(f"Titulo: {self.titulo}\n"
              f"Autor: {self.autor}\n"
              f"isbn: {self.isbn}\n"
              f"disponivel: {self.disponivel}")


L1 = Livro("Livro1","Autor1",1,True)
L2 = Livro("Livro2","Autor1",2,False)
L3 = Livro("Livro3","Autor3",3,True)
L4 = Livro("Livro4","Autor2",4,False)
L5 = Livro("Livro5","Autor2",5,True)

biblioteca = [L1,L2,L3,L4,L5]

print("=" * 80)
L1.descrição()
print("=" * 80)
L2.descrição()
print("=" * 80)
L3.descrição()
print("=" * 80)
L4.descrição()
print("=" * 80)
L5.descrição()
print("=" * 80)


class Usuario():
    def __init__(self,nome,matricula):
        self.nome = nome
        self.matricula = matricula
        self.emprestados = []
        self.limite = 1

    def pegar_livro(self):
        if len(self.emprestados) < self.limite:
           livro = input("Digite o nome do livro que deseja: ")
           for i in biblioteca:
               if i.titulo == livro:
                   self.emprestados.append(i)
                   i.disponivel = False
                      

U1 = Usuario("Rian",67)

U1.pegar_livro()