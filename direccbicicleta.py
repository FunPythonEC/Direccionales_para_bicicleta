"""
Programado en la versión 1.9 de MicroPython
"""
from machine import Pin
import machine, neopixel
import time

switch_derecha= Pin(5, Pin.IN) #derecha cable VERDE
switch_izquierda= Pin(4, Pin.IN) #izquierda cable AZUL

num_leds=19
pin_salida=12
np = neopixel.NeoPixel(machine.Pin(pin_salida), num_leds)

def derecha():
    for led in range(0,num_leds - 9,1):
        np[led]=(255,035,001)
        np.write()
        time.sleep_ms(50)
        print ('derecha')
    apagar()
    
    
def izquierda():
    for led in range(0,num_leds - 9,1):
        np[9-led]=(255,035,001)
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
