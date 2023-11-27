from usuarios import Usuario
from livros import Livros
from emprestimo import Emprestimo
from menus import Menu



def main():
    novo_usuario = Usuario(codigo="", nome="", tipo="", login="", senha="")
    emprestimo = Emprestimo(codigoEmprestimo="", codigoCliente="", codigoLivro="", dataEmprestimo="")
    
    
    print("****Bem-vindo(a) a BookStack Innovations!****\n")
    
    cl = input("Você já possui cadastro no nosso sistema? (s/n) ").lower()
    
    while cl != 's' and cl != 'n':
        print("\nPor favor, digite s (sim, se tiver cadastro) ou n (não, senão tiver cadastro)!")
        cl = input("Você já possui cadastro no nosso sistema? (s/n) ").lower()
        
    if cl == 's':
        tentativas_login = 0
        autenticado = False
        
        while tentativas_login < 3 and not autenticado:
            login_resultado = novo_usuario.fazer_login()
            
            if login_resultado:
                novo_usuario = login_resultado
            
            if novo_usuario and novo_usuario.getTipo() == 'Cliente':
                autenticado = True
                tentativas_login = 0
            else:
                print(f"\nTentativas {tentativas_login + 1} de 3:")
                tentativas_login += 1

        if not autenticado:
            print("\n****Número máximo de tentativas atingido. Considere criar um novo usuário.****")
            novo_usuario.criar_usuario()
            novo_usuario.fazer_login()
            
    else:
        novo_usuario.criar_usuario()
        novo_usuario.fazer_login()
        
    
    if isinstance(novo_usuario, Usuario) and   novo_usuario.getTipo() == 'Cliente':
       menu = Menu(usuario = novo_usuario)
       menu.menu_cliente(novo_usuario, emprestimo)
       
        
    else:
        print("Erro: novo_usuario não é do tipo cliente")
        
        
if __name__ == "__main__":
    main()
