from tkinter import *
import sqlite3
miConexion=sqlite3.connect("LibretaBD")
miCursor=miConexion.cursor()

root=Tk()
root.title("Libreta")
root.geometry("300x400+700+100")
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
edadCuadro.config(show="*") #muestra en el el cuadro *** pero se guarda el valor real en la bd
edadEtiqueta=Label(miFrame, text="Ingresa edad")
edadEtiqueta.grid(row=2, column=0)


selectCuadro=Listbox(miFrame, width=30, height=7, selectmode= MULTIPLE)
selectCuadro.grid(row=8, columnspan=3, pady=15, padx=5)
scrollVert=Scrollbar(miFrame, command=selectCuadro.yview)
scrollVert.grid(row=8, column=2, sticky="nsew")
selectCuadro.config(yscrollcommand=scrollVert.set)
#*********BBDD*****************

lista=[]
miCursor.execute("CREATE TABLE IF NOT EXISTS POSTULANTES (ID INTEGER PRIMARY KEY AUTOINCREMENT, NOMBRE VARCHAR (50), APELLIDO VARCHAR (50), EDAD INTEGER (20))")

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
    etiqueta2.grid(row=7, columnspan=3)
    lista.append((nombre, apellido, edad))
    #print(lista)
 
def limpiar():
    global nombre
    global etiqueta2
    global nombreCuadro
        
    nombre=""
    etiqueta2["text"]=nombre
    cuadro1.set(nombre)
    cuadro2.set(nombre)
    cuadro3.set(nombre)
    nombreCuadro.focus() #permite colocar el cursor en el entry que uno quiera

#selectCuadro.config(state="disabled")
def guardar():
    #selectCuadro.config(state="normal")
    selectCuadro.delete(0, 10000)
    miCursor.executemany("INSERT INTO POSTULANTES VALUES(NULL,?,?,?)", lista)
    miCursor.execute("SELECT * FROM POSTULANTES")
    listadoCompleto=miCursor.fetchall()
    N=1
    for x in listadoCompleto:
        selectCuadro.insert(N, x)
        N+=1
        #print(x)
    #selectCuadro.config(state="disabled")
    
def delete(): 
    pinchados= selectCuadro.curselection()
    #print(selectCuadro.get(pinchados))
    for x in pinchados:
        y=selectCuadro.get(x)
        z=y[0]
        texto="DELETE FROM POSTULANTES WHERE ID= :pin"
        miCursor.execute(texto, {'pin':z})
    
#****************BOTONES**********************

boton1=Button(miFrame, text="Enter", width=20, command=guardar_nombre)
boton1.grid(row=3, columnspan=3, pady=5, padx=5)
boton2=Button(miFrame, text="Limpiar", width=20, command=limpiar)
boton2.grid(row=4, columnspan=3, pady=5, padx=5)
boton3=Button(miFrame, text="Guardar", width=20, command=guardar)
boton3.grid(row=5, columnspan=3, pady=5, padx=5)
boton4=Button(miFrame, text="Delete", width=20, command=delete)
boton4.grid(row=6, columnspan=3, pady=5, padx=5)

root.mainloop()
miConexion.commit()
miConexion.close()