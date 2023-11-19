from usuarios import Usuario
from emprestimo import Emprestimo

class Menu:
    
    def __init__(self, usuario=None, emprestimo=None):
        self.__usuario = usuario
        self.__emprestimo = emprestimo

    def setUsuario(self, usuario):
        self.__usuario = usuario

    def getUsuario(self):
        return self.__usuario

    def setEmprestimo(self, emprestimo):
        self.__emprestimo = emprestimo

    def getEmprestimo(self):
        return self.__emprestimo

    def menu_cliente(self, usuario, emprestimo):
        o = 0
        while o != 4:
            print("\nMenu do Cliente:")
            print("1 - Visualizar Empréstimos")
            print("2 - Visualizar Livros")
            print("3 - Sobre")
            print("4 - Sair")

            entrada_usuario = input("O que você deseja fazer?\n")

            if entrada_usuario.isdigit():
                o = int(entrada_usuario)

                if o == 1:
                    emprestimo.emprestimos_do_cliente(usuario)
                elif o == 2:
                    
                    emprestimo.realizar_emprestimo(usuario)
                    
                elif o == 3:
                    print("\n****Sobre a BookStack Innovations\n     A BookStack Innovations surgiu da paixão por conectividade e informação. Seus fundadores, Lucas, Vitor, Camillo, Otávio e Lennon, eram ávidos frequentadores de bibliotecas, mas notaram que algumas delas enfrentavam desafios tecnológicos para gerenciar seu acervo e interagir com os leitores de maneira eficaz. Com formação em engenharia de software, começaram a desenvolver um software inovador que pudesse modernizar e simplificar a gestão das bibliotecas.\n    Após anos de pesquisa, desenvolvimento e testes, criaram um sistema abrangente que revolucionou a experiência bibliotecária. BookStack Innovations oferece um software intuitivo, capaz de catalogar o acervo, gerenciar empréstimos, e conectar leitores a recomendações personalizadas, tudo com uma interface amigável e adaptável a diferentes tipos de bibliotecas\n    Com a missão de promover a acessibilidade à informação e o amor pela leitura, a BookStack Innovations tem conquistado bibliotecas ao redor do mundo, proporcionando eficiência e inovação para instituições que compartilham a paixão pela disseminação do conhecimento.")
                elif o == 4:
                    lo = input("Você deseja sair da sua conta? (s/n): ").lower()
                    while lo != 's' and lo != 'n':
                        print("\nPor favor, digite s (sim, se quiser realizar logout) ou n (não, senão quiser realizar o logout)!")
                        lo = input("Você deseja sair da sua conta? (s/n): ").lower()

                    if lo == 's':
                        usuario.logout()
                        print("Saindo da conta. Até logo!")
                    elif lo == 'n':
                        print("Retornando ao menu do cliente.")
                        self.menu_cliente(usuario,emprestimo)
                    else:
                        print("Opção inválida.")
                else:
                    print("Opção inválida. Tente Novamente.")
            else:
                print("Por favor, digite um número válido")
