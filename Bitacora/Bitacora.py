from Lunes     import *
from Martes    import *
from Miercoles import *
from Jueves    import * 
from Viernes   import * 




menu="""
Escoja un dia
Lunes        1
Martes       2
Miercoles   3
Jueves       4
Viernes      5

"""

state = True  #Forzamos a entrar al ciclo
b=0           #Salida del ciclo

while( state == True ):
    try:
        opcion=int(input(menu))
    except ValueError:
        opcion=6

    a=0           #Indicador de opcion valida
    if (opcion==1):
        horario=Lunes()
        a=1
    if (opcion==2):
        horario=Martes()
        a=1
    if (opcion==3):
        horario=Miercoles()
        a=1
    if (opcion==4):
        horario=Jueves()
        a=1
    if (opcion==5):
        horario=Viernes()
        a=1
    if (a==0):
        print("\nIngrese una opcion valida :(\n")
    
    else:
        state1= True
        while(state1== True ): 
            try:    #intentamos obtener un valor
                hour=int(input("\nIngrese la hora que desea ver //24hrs//\n\n"))
            except ValueError:    #excepto cuando el valor especificado no es un número
                hour=35

            if(hour<24 and hour>0):
                state1= False
                if (opcion==1):
                    print("\nEl dia Lunes a la hora ",hour," usted tiene\n")
                    horario.horario(hour)

                if (opcion==2):
                    print("\nEl dia Martes a la hora ",hour," usted tiene\n")
                    horario.horario(hour)

                if (opcion==3):
                    print("\nEl dia Miercoles a la hora ",hour," usted tiene\n")
                    horario.horario(hour)

                if (opcion==4):
                    print("\nEl dia Jueves a la hora ",hour," usted tiene\n")
                    horario.horario(hour)

                if (opcion==5):
                    print("\nEl dia Viernes a la hora ",hour," usted tiene\n")
                    horario.horario(hour)
                    
                state2=True
                while(state2==True):
                    try:
                        b=int(input("\nSi desea checar otra hora ingrese un 1\n\nSi desea salir ingrese otro numero\n\n"))
                        state2=False
                    except ValueError:
                        state2=True
                        
                if (b==1):
                    state = True
                else:
                    state = False
            else:
                print("hora no valida")

print("\nFue un placer ayudarle, guapo\n")
