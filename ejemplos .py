x = 1
print(x)
10%3
print(10%3)
print(5**3)
print(9/2)
print((9/2)*5)
primer_numero = 5
segundo_numero = 2
resultado = primer_numero + segundo_numero
numb= ( 1,"Pepe",2.5)
print(numb[0]) #esto es un comentario this is a comment 
print(3//4) 
lista = [2,3,"hola"]
print(lista[2])
lista.append("crack")
print(lista[3])
diccionario = {"calve_1":100,"clave_2":2};
print(diccionario["calve_1"]);
boolean = True;
print(boolean);
boolean = False;
print(boolean);
valor=1;
print(valor);
tupla = ("jose",1,1.5,False);#cannot add elements into a tupla 
print(tupla[:2]);
lista[1] = "pepe";
print(lista);
a = 1;
b = 1;
c = a + b;
lista.pop(2); # delete a specific variable with the position 
print(lista);
lista.insert(4,100); # (position/value) add an element 
print(lista);
lista.remove("pepe"); # delete a variable with the specific name of it
print(lista);
diccionario = {"ID1":1,"ID2":2};
print(diccionario) 
print(diccionario["ID1"]);
#///////////if//////////////////////////////////// 
if c == 3:
    print(c);
print("no te salio we ");
##############################################
#/////////RANGE////////////////////////////////////
numeros = list(range(2,5));# list create a new concatenate line of values 
print (numeros);
#/////////////FOR/////////////////////
valor = range(5);
for i in valor:
    print(i)
    for i in range(10):
        print("segunda vuelta")
    print("Se acabo la vuelta")
print("fin de ciclo");


vocales = ("a","e","i","o","u");
for i in vocales:
    print(i)
print("fin de codigo");

vocales = ("a","e","i","o","u");
for i in vocales:
    if i  == "z":
        print(i)
    else:
        print("no existe esa variable");
print("fin de codigo");