#_*_ coding: utf-8 _*_
"""
            JAKAI - Proyecto Hackathon BootCamp Penguin Academy 2019

                        Asunción - Paraguay

                Proyecto de codigo abierto con license GNU

            --------> https://github.com/albrecht99/Jakai <--------

     Mentor : Williams Bobadilla

     Integrantes

     1) Giulliano Albrecht --> Instagram --> giulliano_cht
     2) Miguel Castiñeira  --> Instagram --> miguel_castinheira
     3) Aldo Franco  --> Instagram --> Aldo.franco1
     4) Ivan Ayala   --> Instagram --> ivanrayala

"""
import RPi.GPIO as gpio      # libreria para utilizar los puertos de entrada y salida
import pygame                # libreira para utilizar el control de PS3
import time

# Se define los puerto de la raspberry

motor_der1 = 18
motor_der2 = 19
motor_izq1 = 20
motor_izq2 = 21                          #definimos los pines de GPIO a utilizar


gpio.setmode(gpio.BCM)          # modo BCM de la raspberry pi (Broadcom SOC channel)

gpio.setup(motor_der1,gpio.OUT) # Se configura el motor Der 1
gpio.setup(motor_der2,gpio.OUT) # Se configura el motor Der 2
gpio.setup(motor_izq1,gpio.OUT) # Se configura el motor Izq 1
gpio.setup(motor_izq2,gpio.OUT) # Se configura el motor Izq 2



# Se crea la clase Robot

class Robot:

    def __init__(self,un_nombre,der1,izq1,der2,izq2): #La clase recibe un nombre y los motores
        self.nombre = un_nombre
        self.der1 = der1
        self.izq1 = izq1
        self.der2 = der2
        self.izq2 = izq2
    def avanzar(self):
        gpio.output(self.der1,True)
        gpio.output(self.izq1,True)
        gpio.output(self.der2,False)
        gpio.output(self.izq2,False)
    def reversa(self):
        gpio.output(self.der1,False)
        gpio.output(self.izq1,False)
        gpio.output(self.der2,True)
        gpio.output(self.izq2,True)
    def izq(self):
        gpio.output(self.der1,True)
        gpio.output(self.izq1,False)
        gpio.output(self.der2,False)
        gpio.output(self.izq2,True)
    def der(self):
        gpio.output(self.der1,False)
        gpio.output(self.izq1,True)
        gpio.output(self.der2,True)
        gpio.output(self.izq2,False)
    def detener(self):
        gpio.output(self.der1,False)
        gpio.output(self.izq1,False)
        gpio.output(self.der2,False)
        gpio.output(self.izq2,False)

# Se inicializa JAKAI y se le pasa los motores a utilizar

JAKAI = Robot("Jakai",motor_der1,motor_izq1,motor_der2,motor_izq2)

# Se inicializa la libreria PYGAME y se inicia la busqueda de un Joystick en nuestro caso
# un control de play station 3
pygame.init()
pygame.joystick.init()


joystick = pygame.joystick.Joystick(0) # Se carga el control encontrado en la variable joystick
joystick.init() # se inicializa el joystick ya cargado

joystick_count = pygame.joystick.get_count()# la variable joystick_count guarda la cantidad de joystick que tenemos
"""print("joystick_count")
print(joystick_count)
print("--------------")"""

numaxes = joystick.get_numaxes() # numaxes guarda la cantidad de ejes "Axes" de nuestro control
"""print("numaxes")
print(numaxes)
print("--------------")"""
numbuttons = joystick.get_numbuttons() # numbuttons guarda la cantidad de botones de nuestro control
"""print("numbuttons")
print(numbuttons)
print("--------------")"""

loopQuit = False
while loopQuit == False: # Se inicializa un ciclo con time sleep de 0.1
    time.sleep(0.1)
    # test joystick axes
    for i in range(0,4):
        pygame.event.pump()
        axis = joystick.get_axis(i) # axis recibe si los ejes se estan moviendo
        if i == 0 and axis < 0:
            JAKAI.izq()
            #print("Izquierda")
        if i == 0 and axis > 0:
            #print("Derecha")
            JAKAI.der()
        #test controller buttons
    for i in range(0,numbuttons):
        pygame.event.pump()
        button = joystick.get_button(i) #button recibe si se esta presionando o no un boton
        if i == 9 and button == 1: # Si se presiona el boton 9 "start" se termina el ciclo
            loopQuit = True
        if i == 8 and button == 1:  #Si se presiona el boton 8 "select" los 4 motores se detienen
            JAKAI.detener()
        if i == 7 and button == 1: #Si se presiona el boton 7 "R2" se avanza
            JAKAI.avanzar()
        if i == 6 and button == 1: #Si se presiona el boton 6 "L2" se pone en reversa
            #print ("Apretaste L2")
            JAKAI.reversa()
#Al salir del ciclo se finaliza la libreia PYGAME
pygame.quit()




                                "MUCHAS GRACIAS"
