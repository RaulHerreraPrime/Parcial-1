from tkinter import*

def suma():
    a=int(input("igresa el primer numero\t"))
    b=int(input("igresa el segundo numero\t"))
    lsuma=Label(ventana,text=a+b).grid(column=4,row=0)

def resta():
    a=int(input("igresa el primer numero\t"))
    b=int(input("igresa el segundo numero\t"))
    lresta=Label(ventana,text=a-b).grid(column=4,row=0)

def multi():
    a=int(input("igresa el primer numero\t"))
    b=int(input("igresa el segundo numero\t"))
    lmulti=Label(ventana,text=a*b).grid(column=4,row=0)

def division():
    a=int(input("igresa el primer numero\t"))
    b=int(input("igresa el segundo numero\t"))
    try:
        ldivision=Label(ventana,text=a/b).grid(column=4,row=0)
    except ZeroDivisionError:
        ldivision=Label(ventana,text="MATH ERROR").grid(column=4,row=0)

ventana=Tk()
b1= Button(ventana,text="suma",command=suma).grid(column=0, row=0)
b2= Button(ventana,text="resta",command=resta).grid(column=1, row=0)
b3= Button(ventana,text="multiplicacion",command=multi).grid(column=2, row=0)
b4= Button(ventana,text="division",command=division).grid(column=3, row=0)

ventana.mainloop()
