import tkinter 
#···············································
def  val_user():
    usuario = textbox.get()
    if(len(usuario)>6 and len(usuario)<12 and usuario.isalnum()==True):
        ventana['bg'] = 'green'
        label1 = tkinter.Label(ventana, text="Usuario aceptado: "+usuario,bg="#DFD506",font="Helvetica 20") #labelº
        label1.pack(side=tkinter.TOP)
        new=str(usuario)
        lista.append(new)
        print(lista)
    elif(len(usuario)<6):
        ventana['bg'] = 'orange'
        label1 = tkinter.Label(ventana, text="Error. El usuario debe contener al menos 6 caracteres: "+usuario,bg="white",) #labelº
        label1.pack(side=tkinter.BOTTOM)
    elif(len(usuario)>12):
        ventana['bg'] = 'orange'
        label1 = tkinter.Label(ventana, text="Error. El usuario debe contener menos de 12 caracteres: "+usuario,bg="white",) #labelº
        label1.pack(side=tkinter.BOTTOM)
    elif(usuario.isalnum()==False):
        ventana['bg'] = 'orange'
        label1 = tkinter.Label(ventana, text="Error. El usuario debe contener numeros y caracteres solamente: "+usuario,bg="white",) #labelº
        label1.pack(side=tkinter.BOTTOM)
    else:
        ventana['bg'] = 'red'
        label1 = tkinter.Label(ventana, text="ERROR 404 Usuario no valido "+usuario,bg="white",) #labelº
        label1.pack(side=tkinter.BOTTOM)
    
#////////////WIDGETS////////////////
ventana = tkinter.Tk() #initialice the window
ventana.geometry("400x400") #size 
ventana.title("Practica.-1 Validacion usuario")
#/////////////////////////////////////////////////////
label = tkinter.Label(ventana, text="JJRR INTERFACES",bg="blue") #label
label.pack(side=tkinter.BOTTOM)#center the text 
#/////////////////////////////////////////////////////
textbox= tkinter.Entry(ventana,font="Helvetica 20") #textbox 
textbox.pack()#addd to the window
#/////////////////////////////////////////////////////
Button = tkinter.Button(ventana,text="Validar",command=logic,width=10,height=3,font="Helvetica 15",) #button 
Button.pack(side=tkinter.BOTTOM)
#/////////////////////////////////////////////////////
ventana.mainloop()#keeps the window running 


