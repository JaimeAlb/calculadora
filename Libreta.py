from tkinter import *
import sqlite3
miConexion=sqlite3.connect("LibretaBD")
miCursor=miConexion.cursor()

root=Tk()
root.title("Libreta")
root.geometry("250x200+700+100")
miFrame=Frame(root)
miFrame.pack()

#****************CUADROS DE TEXTO****************

cuadro1=StringVar()
nombreCuadro=Entry(miFrame, textvariable=cuadro1)
nombreCuadro.grid(row=0, column=1, pady=5, padx=5)
nombreEtiqueta=Label(miFrame, text="Ingresa nombre")
nombreEtiqueta.grid(row=0, column=0)

cuadro2=StringVar()
apellidoCuadro=Entry(miFrame, textvariable=cuadro2)
apellidoCuadro.grid(row=1, column=1, pady=5, padx=5)
apellidoEtiqueta=Label(miFrame, text="Ingresa apellido")
apellidoEtiqueta.grid(row=1, column=0)

cuadro3=StringVar()
edadCuadro=Entry(miFrame, textvariable=cuadro3)
edadCuadro.grid(row=2, column=1, pady=5, padx=5)
edadEtiqueta=Label(miFrame, text="Ingresa edad")
edadEtiqueta.grid(row=2, column=0)
#*********BBDD*****************
lista=[]
#miCursor.execute("CREATE TABLE POSTULANTES (ID INTEGER PRIMARY KEY AUTOINCREMENT, NOMBRE VARCHAR (50), APELLIDO VARCHAR (50), EDAD INTEGER (20))")

#***********FUNCIONES*****************
nombre="asd"
etiqueta2="asdd"

def guardar_nombre():
    global nombre
    global etiqueta2

    nombre=nombreCuadro.get()
    apellido=apellidoCuadro.get()
    edad=edadCuadro.get()

    textoParaMostrar= "Ingresado " + nombre + " "+ apellido + " edad " + edad
    etiqueta2=Label(miFrame)
    etiqueta2["text"]=textoParaMostrar #permite mostrar contenido de texto de una variable en un label
    etiqueta2.grid(row=8, columnspan=3)
    lista.append((nombre, apellido, edad))
    print(lista)
 
def borrar():
    global nombre
    global etiqueta2
    global nombreCuadro
        
    nombre=""
    etiqueta2["text"]=nombre
    cuadro1.set(nombre)
    cuadro2.set(nombre)
    cuadro3.set(nombre)
    nombreCuadro.focus() #permite colocar el cursor en el entry que uno quiera

def guardar():
    miCursor.executemany("INSERT INTO POSTULANTES VALUES(NULL,?,?,?)", lista)
    
#miCursor.executemany("INSERT INTO POSTULANTES VALUES(?,?,?)", lista)
#****************BOTONES**********************

boton1=Button(miFrame, text="Enter", width=20, command=guardar_nombre)
boton1.grid(row=5, columnspan=3, pady=5, padx=5)
boton2=Button(miFrame, text="Borrar", width=20, command=borrar)
boton2.grid(row=6, columnspan=3, pady=5, padx=5)
boton3=Button(miFrame, text="Guardar", width=20, command=guardar)
boton3.grid(row=7, columnspan=3, pady=5, padx=5)

root.mainloop()
miConexion.commit()
miConexion.close()