from datetime import datetime
from livros import Livros
from usuarios import Usuario
import random
import string
class Emprestimo:
    
    contador_emprestimo = 1
    
    def __init__(self, codigoEmprestimo, codigoCliente, codigoLivro, dataEmprestimo):
        self.__codigoEmprestimo = codigoEmprestimo
        self.__codigoCliente = codigoCliente
        self.__codigoLivro = codigoLivro
        self.__dataEmprestimo = dataEmprestimo

    def setCodigoEmprestimo(self, codigoEmprestimo):
        self.__codigoEmprestimo = codigoEmprestimo    
    def getCodigoEmprestimo(self):
        return self.__codigoEmprestimo


    def setCodigoCliente(self, codigoCliente):
        self.__codigoCliente = codigoCliente   
    def getCodigoCliente(self):
        return self.__codigoCliente
    

    def setDataEmprestimo(self, dataEmprestimo):
        self.__dataEmprestimo = dataEmprestimo
    def getDataEmprestimo(self):
        return self.__dataEmprestimo


    def setCodigoLivro(self, codigoLivro):
        self.__codigoLivro = codigoLivro    
    def getCodigoLivro(self):
        return self.__codigoLivro

    def setUsuario(self, usuario):
        self.__usuario = usuario

    def getUsuario(self):
        return self.__usuario

    def realizar_emprestimo(self, usuario):
        livros = Livros(codigoLivro="", nomeLivro="", nomeAutor="")
        livros_info = livros.ler_livros()  # Usamos apenas a lista de livros

        codigo_cliente = usuario.getCodigo()
        usuario_emprestimo = Usuario(codigo="", nome="", tipo="", login="", senha="")
        usuario_emprestimo.setCodigo(codigo_cliente)
        self.setUsuario(usuario_emprestimo)

        if not livros_info:
            print("Não há livros disponíveis para empréstimo.")
            return

        emprestimo_realizado = False

        while not emprestimo_realizado:
            print("Livros Disponíveis:")
            for livro in livros_info:
                disponibilidade = "Disponível" if livro[3] else "Indisponível"
                print(f"Código: {livro[0]}, Título: {livro[1]}, Autor: {livro[2]}, Disponibilidade: {disponibilidade}")

            codigo_livro = input("Informe o código do livro que deseja emprestar: ")

            # Substitua a chamada da função original pela nova função
            status_livro = self.verificar_livro_ja_emprestado(codigo_cliente, codigo_livro)

            if not self.verificar_livro_disponivel(codigo_cliente, codigo_livro):
                print("Livro não disponível para empréstimo.")
                escolha = input("Deseja escolher outro livro? (s/n): ").lower()
                emprestimo_realizado = escolha != 's'

            elif status_livro == "alugado_por_outro_usuario":
                print("Livro já emprestado para outra pessoa.")
                emprestimo_realizado = True

            elif status_livro == "alugado_por_usuario_atual":
                print("Você já possui este livro emprestado.")
                emprestimo_realizado = True

            else:
                # Verifica se o livro está disponível antes de realizar o empréstimo
                livro_disponivel = False
                for livro_info in livros_info:
                    if livro_info[0] == codigo_livro and livro_info[3]:  # Verifica se o livro está disponível
                        livro_disponivel = True
                        break

                if livro_disponivel:
                    data_emprestimo = datetime.now().strftime("%Y-%m-%d")
                    emprestimo = f"{self.gerar_codigo_emprestimo()},{codigo_cliente},{codigo_livro},{data_emprestimo}\n"

                    with open("dados/emprestimos.txt", "a") as file:
                        file.write(emprestimo)

                    print("Empréstimo realizado com sucesso!")

                    # Atualiza o arquivo livros.txt após o empréstimo
                    with open("dados/livros.txt", "w") as livros_file:
                        for livro_info in livros_info:
                            if livro_info[0] == codigo_livro:
                                livros_file.write(f"{livro_info[0]},{livro_info[1]},{livro_info[2]},{False}\n")
                            else:
                                livros_file.write(f"{livro_info[0]},{livro_info[1]},{livro_info[2]},{livro_info[3]}\n")

                    emprestimo_realizado = True
                else:
                    print("Livro não disponível para empréstimo.")
                    escolha = input("Deseja escolher outro livro? (s/n): ").lower()
                    emprestimo_realizado = escolha != 's'
    
    def verificar_livro_disponivel(self, codigo_cliente, codigo_livro):
        status_livro = self.verificar_livro_ja_emprestado(codigo_cliente, codigo_livro)

        if status_livro == "livre":
            return True
        elif status_livro == "alugado_por_usuario_atual":
            print("Você já possui este livro emprestado.")
            return False
        elif status_livro == "alugado_por_outro_usuario":
            print("Livro já emprestado para outra pessoa.")
            return False
        else:
            print("Ocorreu um erro ao verificar a disponibilidade do livro.")
            return False

    

    def verificar_livro_ja_emprestado(self, codigo_cliente, codigo_livro):
        try:
            with open("dados/emprestimos.txt", "r") as emprestimos_file:
                for line in emprestimos_file:
                    if line.strip():
                        _, codigo_livro_existente, codigo_cliente_existente, _ = line.strip().split(",")
                        if codigo_livro_existente == codigo_livro and codigo_cliente_existente == codigo_cliente:
                            # O livro está emprestado para o cliente atual
                            return "alugado_por_usuario_atual"
                        elif codigo_livro_existente == codigo_livro:
                            # O livro está emprestado, mas não para o cliente atual
                            return "alugado_por_outro_usuario"
                # Se chegou aqui, o livro não foi alugado por nenhum cliente
                return "livre"
        except FileNotFoundError:
            print("O arquivo de empréstimos não foi encontrado.")
        except Exception as e:
            print(f"Ocorreu um erro ao processar os empréstimos: {e}")

        return "erro"
            


    def verificar_emprestimo_existente(self, codigo_cliente, codigo_livro):
        try:
            with open("dados/emprestimos.txt", "r") as emprestimos_file:
                for line in emprestimos_file:
                    parts = line.strip().split(",")
                    if len(parts) >= 3:
                        _, codigo_cliente_existente, codigo_livro_existente, _ = parts
                        if codigo_cliente_existente == codigo_cliente and codigo_livro_existente == codigo_livro:
                            return True
                    else:
                        print(f"A linha de empréstimo não possui informações suficientes ou não está no formato esperado: {line.strip()}")
                        print(f"Conteúdo da linha dividido: {parts}")
        except FileNotFoundError:
            print("O arquivo de empréstimos não foi encontrado.")
        

        return False

    @staticmethod
    def gerar_codigo_emprestimo(tamanho=8):
        parte_alfanumerica = ''.join(random.choices(string.ascii_uppercase + string.digits, k=tamanho))
        codigo_emprestimo = f"EMPRESTIMO-{parte_alfanumerica}"
        return codigo_emprestimo


    def emprestimos_do_cliente(self, usuario):
        codigo_cliente = usuario.getCodigo()
        emprestimos_cliente = []

        try:
            with open("dados/emprestimos.txt", "r") as file:
                for line in file:
                    if line.strip():  
                        try:
                            codigo_emprestimo, codigo_cliente_existente, codigo_livro_existente, data_emprestimo = line.strip().split(",")
                            if codigo_cliente_existente == codigo_cliente:
                                emprestimo_info = {
                                    'codigo_emprestimo': codigo_emprestimo,
                                    'codigo_cliente': codigo_cliente_existente,
                                    'codigo_livro': codigo_livro_existente,
                                    'data_emprestimo': data_emprestimo
                                }
                                emprestimos_cliente.append(emprestimo_info)
                        except ValueError as ve:
                            print(f"A linha de empréstimo está mal formatada: {line.strip()}. Erro: {ve}")
        except FileNotFoundError:
            print("O arquivo de empréstimos não foi encontrado.")
        except Exception as e:
            print(f"Ocorreu um erro ao processar os empréstimos: {e}")

        if emprestimos_cliente:
            print()
            print(f"Empréstimos do cliente {codigo_cliente}:")
            for emprestimo_info in emprestimos_cliente:
                print(f"Código do Empréstimo: {emprestimo_info['codigo_emprestimo']}")
                print(f"Código do Livro: {emprestimo_info['codigo_livro']}")
                print(f"Data do Empréstimo: {emprestimo_info['data_emprestimo']}")
                print("--------")
        else:
            print(f"O cliente {codigo_cliente} não possui empréstimos.")

        return emprestimos_cliente




