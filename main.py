"""
     JAKAI - Proyecto Hackathon BootCamp Penguin Academy 2019
     Asunción - Paraguay
     Mentor : Williams Bobadilla
     Integrantes
     1) Giulliano Albrecht Instagram --> giulliano_cht
     2) Miguel Castiñeira Instagram --> miguel_castinheira
     3) Aldo Franco Instagram --> Aldo.franco1
     4) Ivan Ayala  Instagram --> ivanrayala

"""
import RPi.GPIO as gpio      # libreria para utilizar los puertos de entrada y salida
import pygame
import time

motor_der1 = 18
motor_der2 = 19
motor_izq1 = 20
motor_izq2 = 21                          #definimos los pines de GPIO a utilizar


gpio.setmode(gpio.BCM)          # modo BCM de la raspberry pi (Broadcom SOC channel)

gpio.setup(motor_der1,gpio.OUT) # Se configura el motor Der 1
gpio.setup(motor_der2,gpio.OUT) # Se configura el motor Der 2
gpio.setup(motor_izq1,gpio.OUT) # Se configura el motor Izq 1
gpio.setup(motor_izq2,gpio.OUT) # Se configura el motor Izq 2

class Robot:

    def __init__(self,un_nombre,der1,izq1,der2,izq2):
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
        time.sleep(0.1)
    def reversa(self):
        gpio.output(self.der1,False)
        gpio.output(self.izq1,False)
        gpio.output(self.der2,True)
        gpio.output(self.izq2,True)
        time.sleep(0.1)
    def izq(self):
        gpio.output(self.der1,True)
        gpio.output(self.izq1,False)
        gpio.output(self.der2,False)
        gpio.output(self.izq2,True)
        time.sleep(0.1)
    def der(self):
        gpio.output(self.der1,False)
        gpio.output(self.izq1,True)
        gpio.output(self.der2,True)
        gpio.output(self.izq2,False)
        time.sleep(0.1)
    def detener(self):
        gpio.output(self.der1,False)
        gpio.output(self.izq1,False)
        gpio.output(self.der2,False)
        gpio.output(self.izq2,False)
        time.sleep(0.1)

JAKAI = Robot("Jakai",motor_der1,motor_izq1,motor_der2,motor_izq2)

pygame.init()
pygame.joystick.init()


joystick = pygame.joystick.Joystick(0)
joystick.init()

joystick_count = pygame.joystick.get_count()
"""print("joystick_count")
print(joystick_count)
print("--------------")"""

numaxes = joystick.get_numaxes()
"""print("numaxes")
print(numaxes)
print("--------------")"""
numbuttons = joystick.get_numbuttons()
"""print("numbuttons")
print(numbuttons)
print("--------------")"""

loopQuit = False
while loopQuit == False:
    time.sleep(0.1)
    # test joystick axes
    for i in range(0,4):
        pygame.event.pump()
        axis = joystick.get_axis(i)
        if i == 0 and axis == 0:
            JAKAI.detener()
        if i == 0 and axis < 0:
            JAKAI.izq()
            #print("Izquierda")
        if i == 0 and axis > 0:
            #print("Derecha")
            JAKAI.der()
        #test controller buttons
    for i in range(0,numbuttons):
        pygame.event.pump()
        button = joystick.get_button(i)
        if i == 9 and button == 1:
            loopQuit = True
        if i == 8 and button == 1:
            JAKAI.detener()
        if i == 7 and button == 1:
            #print ("Apretaste R2")
            JAKAI.avanzar()
        if i == 6 and button == 1:
            #print ("Apretaste L2")
            JAKAI.reversa()
        if button == 0:
            JAKAI.detener()
        """if i == 0 and button == 1:
            #print ("Apretaste X")
        if i == 1 and button == 1:
            #print ("Apretaste Circulo")
        if i == 2 and button == 1:
            #print ("Apretaste Triangulo")
        if i == 3 and button == 1:
            #print ("Apretaste Cuadrado")"""

pygame.quit()
