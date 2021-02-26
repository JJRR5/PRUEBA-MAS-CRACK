#Principal methods of the string object 
cadena = "cadena de texto"
resultado = 5
print(cadena)

#CAPITALIZE() only one string
print(cadena.capitalize())

#LOWER() only one string
print(cadena.lower())

#UPPER() all the strings 
print(cadena.upper())

#swapcase() lower case = capital letter 
print(cadena.swapcase()) 

#title() turns into a capital letter the first letter of each word
print(cadena.title())

#center() this could be useful for pull apart the results 
print(cadena.center(50,'-'))
print(str(resultado).center(50,'/'))
#rjust() right
print(cadena.rjust(50,'-'))

#ljust() left
print(cadena.ljust(50,'-'))

#zfill() zero fill 
print(cadena.zfill(50))

#//////////////////////////////SEARCH METHODS//////////////////////////////
#count()// looks for a specific letter inside of a line of characters 
print (cadena.count('t'))

#find()// looks for the position of a letter 
print("count:",str(cadena.find('e')))
print(cadena.find('texto',1,15))

#////////////////////////////Validation methods////////////////////////////

#startswith()
print(cadena.startswith('t',10))

#endswith()
print(cadena.endswith('o'))

#isalnum()
num = '2'
print(num.isalnum())

#isalpha
print(num.isalpha())
print(num.isdigit())

#islower
print(cadena.islower())

#isupper
print(cadena.isupper())
hola = "que pasa perro".upper()
print(hola)

#istitle()
print(cadena.istitle())

#///////////////////////////Substitution methods/////////////////////////////

#replace()
ori = "------hola-------"
print(ori.replace(ori,"pepe"))
#strip() //Delete useful strings
print(ori.strip('-'))
#lstrip()
print(ori.lstrip('-'))
#rstrip()
print(ori.rstrip('-'))

#/////////////////////union and split methods /////////////////////
#split()
variables = "altura: 5m,temperatura: 39,peso: 5kg"
print(variables)
lista = variables.split(', ')
print(lista)

#partition()
tupla = variables.partition(": ")
print(tupla)

#add one element at the end of the list 
lista.append("oxigenacion: 95%")
print(lista)

#add another list at the end of the first list 
#EXTEND()
lista.extend(["edad: 54, sexo: M"])
print(lista)

#insert()
lista.insert(3,"crack: yo")
print(lista)

#pop() //delete an element
lista.pop(0)
print(lista)

#delete an element with the specific value 
#remove()
lista.remove("crack: yo")
print(lista)

#reverse()
lista.reverse()
print(lista)

#sort() ASCII
lista.sort()
print(lista)

gg = ['a','b','c','D']
gg.sort()
print(gg)

gg.sort(reverse = True)
print(gg)

#count()
pedro  = "hola"
print(pedro.count(pedro))


#index()
print(gg.index('D'))
cadena = ("hola perro ")
print (cadena.count(' '))
cadena = "Auepasa"
print(cadena.islower())
print(cadena.isupper())

