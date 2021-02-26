
def  val_password(usuario):
    mayuscula = False
    minuscula = False
    numero = False
    caracter = False
    for letra in usuario:
        print(letra)
        if (letra.isupper()==True):
            mayuscula = True
        if (letra.islower()==True):
            minuscula=True
        if(letra.isdigit()==True):
            numero=True
        if(letra.isalnum()==False):
            caracter = True
    if (numero ==True and mayuscula==True and minuscula == True and caracter == True):
        return print("True")
    else:
        return False
    if(function(usuario)==True and usuario.count(' ')==False and len(usuario)>7):
        return print("Contraseña aceptada")
    elif(function(usuario)==False and len(usuario)<7 ):
        return print("contraseña debil")
    elif(usuario.count(' ')== True):
        return print("La contraseña no puede tener espacios ")

val_password(input("Escribe un usuario: "))
