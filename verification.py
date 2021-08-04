user = "example23"
password = "1234"



def validate_user():
    user_to_validate = input("Digite seu usuário:")
    if user_to_validate != user:
        print("Usuário inválido!")
    else:
        validate_password()

def validate_password():
    password_to_validate = input("Digite sua senha:")
    if password_to_validate == password and password_to_validate.isdigit(): 
        print("Acesso permitido")
    else:
        print("Senha inválida ou incorreta!")
        stop()

def stop():
    print("="*22)
    print("1 - tentar novamente \n2 - desligar o sistema")
    print("="*22)
    option = input()
    if option == "1" or option == "2":
        if option == "1":
            validate_password()
        else:
            print("Sistema desligado")
    else:
        print("Opção Inválida!")
        stop()
        


validate_user()
