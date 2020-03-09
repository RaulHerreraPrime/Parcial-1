
import time   #importamos la libreria tiempo

class caja:
    def __init__(self):
        pass

    def terminal(self):
        a=0
        b=0
        while(b !=3):
            while(a!=1):
                try:
                    a=int(input("SELECIONA:\n\t0 == No entró una caja\n\t1 == Entró una caja\n\t3 == salir\n\t")) #preguntamos si hay una caja
                except ValueError:
                    a=0
            
            if(a>-1 and a<2):
                a=0
                state=True
                b=0
                time.sleep(1)
                print("moviendose por la banda")
                time.sleep(1)
                print("llegando a terminal")
                time.sleep(1)
                while(state==True):
                    try:
                        c=int(input("SELECCIONA:\n\t0 == caja chica\n\t1 == caja mediana\n\t2 ==caja grande\n\t"))
                    except ValueError:
                        c=4
                        state==True
                    if(c>-1 and c<3):
                        contador(c)
                        time.sleep(1)
                        print("moviendose por la banda")
                        time.sleep(1)
                        state=False
            else:
                b=3
                
            

caja1=caja()
caja1.terminal()