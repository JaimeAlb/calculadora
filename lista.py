

lista=[]

v1=1

def asd():
    global v1
    
    for i in range(1,6):
        lista.append(v1)
        v1+=1


asd()

print(lista)

myGlobal = 5

def func1():
    global myGlobal
    myGlobal = 42
    print(myGlobal)

def func2():
    print (myGlobal)

func1()
func2()