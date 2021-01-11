
user = "caiovictor023"
password = "2391"
a = int

def stop(a):
    print("1 - tentar novamente \n2 - desligar o sistema")
    a = int(input())
    if a == 1:
        validate_password(password)
    elif a == 2:
        print("Sistema desligado")
    else:
       print("1 - tentar novamente \n2 - desligar o sistema")
       stop(a)


def validate_user(user):
    user_to_validate = input("Digite seu usuário:")
    if user_to_validate != user:
        print("Usuário inválido!")
    else:
        validate_password(password)

def validate_password(password):
    password_to_validate = input("Digite sua senha:")
    if password_to_validate == password:
        print("Acesso permitido")
    else:
        print("Senha incorreta!")
        stop(a)
        
validate_user(user)

    


