import time     #importar libreria tiempo

global r     #variable global

class suma:
    def __init__(self ):    #cuando sirven al objeto
        #self.a=a
        #self.b=b
        pass  #es para dejar un metodo que no va a hacer nada

    def suma (self,a,b):    #cuando se ponen aqui son atributos del objeto que solo le sirven al método
        global r
        r=a+b
        print(r)
        
        
class resta:
    def __init__(self, a ,b ):
        self.a=a
        self.b=b

    def resta (self):
        global r
        r=self.a-self.b
        print(r)

class multi:
    def __init__(self, a ,b ):
        self.a=a
        self.b=b

    def multi (self):
        global r
        r=self.a*self.b
        print(r)

#instrucciones
o1=suma()
o2=resta(10,5)
o3=multi(10,5)
r=0
o1.suma(10,5)
time.sleep(.5)
print(r)
time.sleep(.5)
o2.resta()
time.sleep(.5)
print(r)
time.sleep(.5)
o3.multi()
time.sleep(.5)
print(r)

