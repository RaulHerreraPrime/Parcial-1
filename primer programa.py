from figuras import *
global v


#ordenes
circulo1=circulo(10,0,0)        #se agrupa por acomodo, mientras no esté a la izquierda del anterior, pertenece a lo mismo, si está a la izquierda,es otro proceso
circulo1.area()                     #se le da la orden de hacer el area
rectangulo1=rectangulo(0,10,5)
rectangulo2=rectangulo(0,20,4)
rectangulo1.perimetro()      #se le da la orden de sacar el perimetro
#rectangulo2.area()
#circulo1.radio           #son para acceder a los parametros del objeto
#rectangulo2.altura    #son para acceder a los parametros del objeto
f1=figura (5,10,20)
v=f1.valores_multi()
print (v)
