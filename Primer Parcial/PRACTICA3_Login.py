
lista = ""
user = (input("sacate las chichis: "))
lista1 = lista.split(',')
lista1.append(user)
print(lista1)
print(lista1[1])

menu = (input("Ingresa el comando: "))
if(menu == "a"):
    print("a")
elif(menu=="b"):
    print("b")
elif(menu=="c"):
    print("c")
elif(menu=="d"):
    print("d")
elif(menu=="e"):
    print("e")   
else: 
    print("No existte el comando")