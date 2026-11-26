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
            return True 
        else: 
            print(f"O Livro {self.titulo} esta indisponivel!")
            return False

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
L2 = Livro("Livro2","Autor1",2,True)
L3 = Livro("Livro3","Autor3",3,True)
L4 = Livro("Livro4","Autor2",4,True)
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
                    if i.emprestar():
                        self.emprestados.append(i)
                        break
            else:
                print(f"O Livro {livro} não foi encontrado!")

    def devolver_livro(self):
        if len(self.emprestados) == 0:
            print("Nao tem")
        else:
            livro = input("Digite o nome do livro que deseja devolver: ")
            for i in biblioteca:
                if i.titulo == livro:
                    if i.disponivel == False:
                        self.emprestados.remove(i)
                        i.disponivel = True
                        print("Livro Devolvido!")
                    else:
                        print("O livro ja está Devolvido!")
    

class Aluno(Usuario):
    def __init__(self, nome, matricula):
        super().__init__(nome, matricula)
        self.limite = 2

    def pegar_livro(self):
        if len(self.emprestados) < self.limite:
            return super().pegar_livro()
        else:
            print(f"O aluno {self.nome} Já atingiu o limite de livros emprestados!")
    

class Professor(Usuario):
    def __init__(self, nome, matricula):
        super().__init__(nome, matricula)
        self.limite = 5

    def pegar_livro(self):
        if len(self.emprestados) < self.limite:
            return super().pegar_livro()
        else:
            print(f"O Professor {self.nome} Já atingiu o limite de livros emprestados!")

A1 = Aluno("Rian",67)
P1 = Professor("Guilherme",55)

A1.pegar_livro()
A1.devolver_livro()
P1.pegar_livro()
P1.devolver_livro()