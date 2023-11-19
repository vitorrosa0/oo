from datetime import datetime, timedelta

class Livros:
    def __init__(self, codigoLivro, nomeLivro, nomeAutor):
        self.__codigoLivro = codigoLivro
        self.__nomeLivro = nomeLivro
        self.__nomeAutor = nomeAutor
    

    def setCodigoLivro(self, codigoLivro):
        self.__codigoLivro = codigoLivro    
    def getCodigoLivro(self):
        return self.__codigoLivro
    
    
    def setNomeLivro(self, nomeLivro):
        self.__nomeLivro = nomeLivro    
    def getNomeLivro(self):
        return self.__nomeLivro


    def setNomeAutor(self, nomeAutor):
        self.__nomeAutor = nomeAutor    
    def getNomeAutor(self):
        return self.__nomeAutor


    # Modifique a função ler_livros da classe Livros conforme abaixo
    def ler_livros(self):
    # Ler informações dos livros do arquivo livros.txt
        livros = []

        # Obtém os códigos dos livros que estão atualmente emprestados
        livros_emprestados = set()
        with open("dados/emprestimos.txt", "r") as emprestimos_file:
            for emprestimo_line in emprestimos_file:
                if emprestimo_line.strip():  # Verifica se a linha não está vazia
                    parts = emprestimo_line.strip().split(",")
                    if len(parts) >= 3:  # Verifica se há pelo menos três elementos
                        codigo_emprestado = parts[2]
                        livros_emprestados.add(codigo_emprestado)
                    else:
                        print(f"A linha de empréstimo não possui informações suficientes: {emprestimo_line}")

        # Lê as informações dos livros e verifica se estão emprestados
        with open("dados/livros.txt", "r") as file:
            for line in file:
                if line.strip():  # Verifica se a linha não está vazia
                    parts = line.strip().split(",")
                    if len(parts) >= 3:  # Verifica se há pelo menos três elementos
                        codigo, titulo, autor = parts[:3]
                        disponivel = codigo not in livros_emprestados
                        livros.append((codigo, titulo, autor, disponivel))
                    else:
                        print(f"A linha de livro não possui informações suficientes: {line}")

        return livros


    def atualizar_status_livro(self, codigo_livro, disponivel):
        # Atualizar o status de disponibilidade do livro no arquivo livros.txt
        livros = self.ler_livros()
        with open("dados/livros.txt", "w") as file:
            for livro in livros:
                if livro[0] == codigo_livro:
                    file.write(f"{livro[0]},{livro[1]},{livro[2]},{disponivel}\n")
                else:
                    file.write(f"{livro[0]},{livro[1]},{livro[2]},{livro[3]}\n")


    