from tkinter import *
raiz=Tk()
raiz.title("Calculadora")
miFrame=Frame(raiz)
miFrame.pack()

photo= PhotoImage(file="C:\Curso Python\calculadora\gato.PNG")
labelphoto= Label(raiz, image = photo)
labelphoto.pack()

#++++++++++++++++++++++++VARIABLES++++++++++++++++++++++++++

operacion=""
var1=0
lista=[]
contador=0

#++++++++++++++++++++++PANTALLA++++++++++++++++++++++++++++++++++

cuadro1=StringVar()
cuadro2=StringVar()
cuadro3=StringVar()

cuadroTexto=Entry(miFrame, textvariable=cuadro1)
cuadroTexto.grid(row=0, column=0, pady=10, padx=0, columnspan=4)
cuadroTexto.config(fg="black", justify="right")

cuadroTexto2=Entry(miFrame, textvariable=cuadro2)
cuadroTexto2.grid(row=6, column=0, pady=10, padx=0, columnspan=4)
cuadroTexto2.config(fg="black", justify="right")

cuadroTexto2=Entry(miFrame, textvariable=cuadro3)
cuadroTexto2.grid(row=5, column=0, pady=10, padx=0, columnspan=4)
cuadroTexto2.config(fg="black", justify="right")

#++++++++++++++++++++++FUNCIONES BOTONES++++++++++++++++++++++++++++++++

def codigo(num):
    global operacion    
    if operacion!="":
        cuadro1.set(num)
        operacion=""             
    else:
        cuadro1.set(cuadro1.get()+num)

def suma(Get):
    global operacion
    global var1
          
    operacion="suma"    
    var1=int(Get)+var1  #var1=int(numero.get())+var1  
    cuadro2.set(var1)       
    #print(var1+1-1)
    proceso()    

def enter():
    global var1   
    global lista 

    cuadro2.set(var1+int(cuadro1.get()))
    var1=int(cuadro2.get())

    lista.append(cuadro1.get())
    cuadro3.set(lista)  

def proceso():
    global var1
    global lista
    global contador
    
    if contador==0:
        lista.append(str(var1)+"+")
        cuadro3.set(lista)
        contador+=1
    else:
        lista.append(str(cuadro1.get())+"+")
        cuadro3.set(lista)      
      
#++++++++++++++++++++++++++++++++++BOTONES GUI++++++++++++++++++++++++++++++

botonEnter=Button(miFrame, text="Enter", width=3, command=lambda:enter())
botonEnter.grid(row=4, column=2, pady=5, padx=5)
botonSuma=Button(miFrame, text="+", width=3, command=lambda:suma(cuadro1.get()))
botonSuma.grid(row=1, column=3, pady=5, padx=5)

boton1=Button(miFrame, text="1", width=3, command=lambda:codigo("1"))
boton1.grid(row=1, column=0, pady=5, padx=5)
boton2=Button(miFrame, text="2", width=3, command=lambda:codigo("2"))
boton2.grid(row=1, column=1, pady=5, padx=5)
boton3=Button(miFrame, text="3", width=3, command=lambda:codigo("3"))
boton3.grid(row=1, column=2, pady=5, padx=5)
boton4=Button(miFrame, text="4", width=3, command=lambda:codigo("4"))
boton4.grid(row=2, column=0, pady=5, padx=5)
boton5=Button(miFrame, text="5", width=3, command=lambda:codigo("5"))
boton5.grid(row=2, column=1, pady=5, padx=5)
boton6=Button(miFrame, text="6", width=3, command=lambda:codigo("6"))
boton6.grid(row=2, column=2, pady=5, padx=5)
boton7=Button(miFrame, text="7", width=3, command=lambda:codigo("7"))
boton7.grid(row=3, column=0, pady=5, padx=5)
boton8=Button(miFrame, text="8", width=3, command=lambda:codigo("8"))
boton8.grid(row=3, column=1, pady=5, padx=5)
boton9=Button(miFrame, text="9", width=3, command=lambda:codigo("9"))
boton9.grid(row=3, column=2, pady=5, padx=5)
botonPunto=Button(miFrame, text=".", width=3, command=lambda:codigo("."))
botonPunto.grid(row=4, column=0, pady=5, padx=5)
boton0=Button(miFrame, text="0", width=3, command=lambda:codigo("0"))
boton0.grid(row=4, column=1,  pady=5, padx=5)

"""
botonResta=Button(miFrame, text="-", width=3)
botonResta.grid(row=2, column=3, pady=5, padx=5)
botonMult=Button(miFrame, text="x", width=3)
botonMult.grid(row=3, column=3, pady=5, padx=5)
botonDiv=Button(miFrame, text="/", width=3)
botonDiv.grid(row=4, column=3, pady=5, padx=5)
"""
raiz.mainloop()