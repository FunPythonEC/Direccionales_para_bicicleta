"""
Programado en la versión 1.9 de MicroPython
Tener en cuenta de que si se usa otra versión de MicroPython
es posible de que se tenga que modificar cierta función.
Además de que el código puede variar dependiendo del largo de la tira led.
"""

#importamos neopixel ya que es la que sirve para poder manejar los leds.
from machine import Pin
import machine, neopixel
import time

switch_derecha= Pin(5, Pin.IN) #se define los pines para poder detectar cuando el pulsador es aplastado.
switch_izquierda= Pin(4, Pin.IN)

num_leds=19 #numero de leds de la tira usada, para asegurarnos que usamos todos los leds.
pin_salida=12 #el pin de salida puede cambiar dependiendo de cada persona.
np = neopixel.NeoPixel(machine.Pin(pin_salida), num_leds)

#función para poder hacer el patron hacia la derecha en los leds.
def derecha():
    for led in range(0,num_leds - 9,1):
        np[led]=(255,35,1)
        np.write()
        time.sleep_ms(50)
        print ('derecha')
    apagar()
    
#patrón hacia la izquierda en los leds
def izquierda():
    for led in range(0,num_leds - 9,1):
        np[9-led]=(255,35,1)
        np.write()
        time.sleep_ms(50)
        print ('izquierda')
    apagar()
    
def policia():
    for led in range(0,5,1):
        np[2*led]=(255,0,0)
        #print("rojo")
        np[2*led+1]=(0,0,255)
        #print("azul")
    np.write()
    time.sleep_ms(200)
       
    for led in range(0,5,1):
        np[2*led]=(0,0,255)
       # print("azul")
        np[2*led+1]=(255,0,0)
        #print("rojo")
    np.write()
    time.sleep_ms(200)
    print('poli')
    
def apagar():
    for led in range(0,num_leds,1):
        np[led]=(0,0,0)
    
    np.write()
    time.sleep_ms(100)  
    #print("apagado")

def prueba():
    apagar()    
    derecha()    
    izquierda()    
    for i in range(1):
        policia()
    apagar()

while True:
    estado_derecha= switch_derecha.value()
    estado_izquierda= switch_izquierda.value()
    
    
    if estado_derecha == 1:
        derecha()
        time.sleep_ms(5)
    elif estado_izquierda == 1:
        izquierda()
        time.sleep_ms(5)
    else:
policia()
