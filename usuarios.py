
class Usuario:
    def __init__(self, codigo, nome, tipo, login, senha):
        self.__codigo = codigo
        self.__nome = nome
        self.__tipo = tipo
        self.__login = login
        self.__senha = senha
        self.__tentativas_login = 0
        
    def setCodigo(self, codigo):
        self.__codigo = codigo    
    def getCodigo(self):
        return self.__codigo


    def setNome(self, nome):
        self.__nome = nome
    def getNome(self):
        return self.__nome

    
    def setTipo(self, tipo):
        self.__tipo = tipo
    def getTipo(self):
        return self.__tipo


    def setLogin(self, login):
        self.__login = login
    def getLogin(self):
        return self.__login


    def setSenha(self, senha):
        self.__senha = senha
    def getSenha(self):
        return self.__senha
    
    def setTentativasLogin(self, tentativas):
        self.__tentativas_login = tentativas

    def getTentativasLogin(self):
        return self.__tentativas_login


    def usuario_com_mesmo_codigo(self, codigo):
        with open("dados/usuarios.txt", "r") as file:
            for linha in file:
                dados_usuario = linha.strip().split(',')
                if dados_usuario[0] == codigo:
                    return True
        return False

    def usuario_com_mesmo_login(self, login):
        with open("dados/usuarios.txt", "r") as file:
            for linha in file:
                dados_usuario = linha.strip().split(',')
                # Verifica se a lista tem pelo menos 5 elementos antes de acessar o índice 3 (login)
                if len(dados_usuario) >= 5 and dados_usuario[3] == login:
                    return True
        return False

    def criar_usuario(self):       
        codigo = input("Informe o código do usuário: ")
        
        # Verifica se já existe um usuário com o mesmo código
        while self.usuario_com_mesmo_codigo(codigo):
            print("Já existe um usuário com este código. Por favor, escolha outro código.")
            codigo = input("Informe o código do usuário: ")
        self.setCodigo(codigo)
        nome = input("Informe o nome do usuário: ").capitalize()
        self.setNome(nome)
        tipo = input("Informe o tipo do usuário (Cliente ou Bibliotecario): ").capitalize()
        self.setTipo(tipo)
        
        login = input("Informe o login do usuário: ")
        
        # Verifica se já existe um usuário com o mesmo login
        while self.usuario_com_mesmo_login(login):
            print("Já existe um usuário com este login. Por favor, escolha outro login.")
            login = input("Informe o login do usuário: ")
        
        self.setLogin(login)
        senha = input("Informe a senha do usuário: ")
        self.setSenha(senha)
        
        

        novo_usuario = Usuario(codigo=self.getCodigo(), nome=self.getNome(), tipo=self.getTipo(), login=self.getLogin(), senha=self.getSenha())

        # Adiciona o novo usuário ao arquivo ou armazenamento adequado
        with open("dados/usuarios.txt", "a") as file:
            novo_usuario_info = f"{novo_usuario.__codigo},{novo_usuario.__nome},{novo_usuario.__tipo}," \
                                f"{novo_usuario.__login},{novo_usuario.__senha}\n"
            file.write(novo_usuario_info)

        print("Usuário criado com sucesso!")

    def fazer_login(self):
        login = input("Informe o login: ")
        senha = input("Informe a senha: ")
        
        with open("dados/usuarios.txt", "r") as file:
            for linha in file:
                dados_usuario = linha.strip().split(',')
                # Verifica se a lista tem pelo menos 5 elementos antes de acessar os índices 3 e 4 (login e senha)
                if len(dados_usuario) >= 5 and dados_usuario[3] == login and dados_usuario[4] == senha:
                    print("\nLogin bem-sucedido!")
                    self.setNome(dados_usuario[1])
                    print(f"Bem vindo, {self.getNome()}! :)")
                    self.setCodigo(dados_usuario[0])
                    
                    tipo_usuario = dados_usuario[2]
                    self.setTipo(tipo_usuario)
                    self.setTentativasLogin(0)  # Reinicia o contador após um login bem-sucedido
                    return self

        print("Login falhou. Verifique seu login e senha.")
        tentativas = self.getTentativasLogin() + 1  # Incrementa o contador de tentativas de login falhas
        self.setTentativasLogin(tentativas)
        #print(f"Tentativas restantes: {3 - tentativas}")
        
        return None
        
        
        
    def logout(self):
        self.__codigo = ""
        self.__nome = ""
        self.__tipo = ""
        self.__login = ""
        self.__senha = ""
        print("Logout realizado com sucesso.")
        
    
# Exemplo de uso

# novo_usuario.criar_usuario()

# # Chamando a função login com login e senha
# novo_usuario_login = Usuario(codigo=novo_usuario.getCodigo(), nome=novo_usuario.getNome(),
#                              tipo=novo_usuario.getTipo(), login=novo_usuario.getLogin(),
#                              senha=novo_usuario.getSenha())
# novo_usuario_login.login()
# novo_usuario_login.logout()



