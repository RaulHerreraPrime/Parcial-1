#programa de una alarma que suena en el tiempo en minutos que le digan en el lapso que se le pida
#alumno Herrera Arroyo Raul Omar
import time

global seg_inicio
global duracion_seg


class alarma:
    def __init__(self,minu_inicio,duracion):
                   self.minu_inicio=minu_inicio    
                   self.duracion=duracion

    def conv_min_seg(self): #convertir minutos a segundos
            global seg_inicio
            global duracion_seg
            seg_inicio=self.minu_inicio*60
            duracion_seg=self.duracion*60

    def conteo_inicio (self):        #conteo para iniciar
            global seg_inicio
            while(seg_inicio>0):
                    print("la alarma se activará en ",seg_inicio," seg")
                    seg_inicio=seg_inicio-1
                    time.sleep(1)
                    if (seg_inicio==0):
                        print ("ALARMA ENCENDIDA")
 
    def conteo_duracion (self):     #conteo de duracion
            global duracion_seg
            while(duracion_seg>0):
                    print("piu-piu-piu    (sonido de alarma)  restan ", duracion_seg, " segundos")
                    duracion_seg=duracion_seg-1
                    time.sleep(1)
 
#instrucciones
print("programa de una alarma que suena en el tiempo en minutos que le digan ")
min_ini=float(input("ingresar en cuanto tiempo sonará la alarma (en minutos)  "))
min_dur=float(input("ingresar duracion de la alarma (en minutos) "))
alarma1=alarma(min_ini,min_dur)
alarma1.conv_min_seg()
alarma1.conteo_inicio()
alarma1.conteo_duracion()

print("fin de la alarma")
