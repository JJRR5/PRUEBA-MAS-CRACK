import tkinter

#ROOT//////////////////
root = tkinter.Tk() #window
root.title("Login") #title
#root.resizable(5,5) #boolean
root.iconbitmap("face.ico")
root.geometry("400x400") #sizeW
root.config(bg="#079FF0")#background
root.config(relief="groove")
root.config(bd=35)
#root.config(cursor="hand2") this is gonna be for buttons
#//////////////////////////////
#---------FUNCIONES---------------------
#----------------------------------------
#FRAME/////////////////////////
frame = tkinter.Frame()
frame.pack() 
#frame.config(relief="groove",cursor="hand2")
frame.config(bd=5)
#/////////////////////////
#LABEL#######################
#imagen=tkinter.PhotoImage(file="error.gif")
label =tkinter.Label(root, text="User",fg="black",font=("Comic Sans MS",18))
label.place(x=133,y=2)
#label.grid(row=0,column=1)
label1 =tkinter.Label(root, text="Password",fg="black",font=("Comic Sans MS",18))
label1.place(x=109,y=110)
#ENTRY
textbox= tkinter.Entry(root,fg="black",font=("Comic Sans MS",10))
textbox.place(x=80,y=160)
textbox.config(show='*')
textbox2= tkinter.Entry(root,fg="black",font=("Comic Sans MS",10))
textbox2.place(x=80,y=50)
#BUTTON
button=tkinter.Button(root,text="Ingresar",fg="black",font=("Comic Sans MS",20),cursor="hand2",bg="#E8EC0B")
button.place(x=100,y=200)

#/////////////////////////////

root.mainloop() #main loop

