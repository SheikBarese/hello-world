user = "example23"
password = "1234"
option = int

def validate_user(user):
    user_to_validate = input("Digite seu usuário:")
    if user_to_validate != user:
        print("Usuário inválido!")
    else:
        validate_password(password)

def validate_password(password):
    password_to_validate = input("Digite sua senha:")
    if password_to_validate == password and password_to_validate.isnumeric(): #se a senha que escolher contiver letras+números, mudar o "isnumeric" para "isdigit"
        print("Acesso permitido")
    else:
        print("Senha inválida ou incorreta!")
        stop(option)

def stop(option):
    print("1 - tentar novamente \n2 - desligar o sistema")
    option = int(input())
    if option == 1:
        validate_password(password)
    elif option == 2:
        print("Sistema desligado")
    else:
       print("1 - tentar novamente \n2 - desligar o sistema")
       stop(option)

validate_user(user)
