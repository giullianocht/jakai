import time
import RPi.GPIO as gpio
class Robot:

    def __init__(self,un_nombre ="",der1,izq1,der2,izq2):
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
