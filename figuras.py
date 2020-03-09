class circulo:     #clase circulo
    def __init__(self, radio,base,altura):  
        self.radio=radio        #se crea una variable self.radio que es propia del circulo y la variable radio es una variable cualquiera
        #self.base=base
        #self.altura=altura
    def area(self):             #self significa que pertenece a la calse, def es para los métodos
            area=3.1416*pow(self.radio,2)  #puede ser pow(self.radio,2) ó sqr(self.radio)
            print("El área del círculo es:\t",area) 

class rectangulo:
    def __init__(self, radio,base, altura):
        self.radio=radio
        self.base=base
        self.altura=altura
        
    def perimetro(self):
        perimetro=(2*self.base)+(2*self.altura)
        print("El perimetro del rectangulo es:\t",perimetro,"\n")
        
#    def area(self):
#       area=self.base*self.altura
#       print("El area del rectangulo es:\t",area,"\n")

class figura(rectangulo, circulo):
    def  valores_multi(self):
          global v
          v=self.radio*self.base*self.altura
          #print(v)
          return v
          
global v
