#calculadora
class suma:
    def __init__(self):
        pass

    def suma(self,a,b):
        print("la suma es: \t ", a+b,"\n")

class resta:
     def __init__(self):
         pass

     def resta(self,a,b):
        print("la resta de a - b es: \t", a-b,"\n")

class multiplicacion:
     def __init__(self):
         pass

     def multiplicacion(self,a,b):
        print("la multiplicacion de a*b es: \t", a*b,"\n")

class division:
     def __init__(self):
         pass

     def division (self,a,b):
         try:
             r=a/b
             print(" la division es: \t",r,"\n")
         except ZeroDivisionError:
             print("math ERROR")

class calculadora (suma, resta, multiplicacion, division):
    def encendido(self):
        o="e"
        while(o != "u"):
            o=input("selecciona: \n\ts\t=\tsuma\n\tr\t=\tresta\n\tm\t=\tmultiplicacion\n\td\t=\tdivision\n\tq\t=\tsalir\n")
            
            if(o=="q"):
                o="u"
                print("CASIO")
                
            else:
                a=int(input("ingresa primer numero \n"))
                b=int(input("ingresa segundo numero \n"))

                if(o=="s"):
                    self.suma(a,b)
                    
                if(o=="r"):
                    self.resta(a,b)

                if(o=="m"):
                    self.multiplicacion(a,b)

                if(o=="d"):
                    self.division(a,b)

           

#instrucciones
calculadora1=calculadora()
calculadora1.encendido()
                  
