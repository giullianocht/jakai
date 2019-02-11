#En proceso
class Robot:

    def __init__(self,un_nombre ="",der1,izq1,der2,izq2):
        self.nombre = un_nombre

    def avanzar(self):

        gpio.output(der1,True)
        gpio.output(izq1,True)
        gpio.output(der2,False)
        gpio.output(izq2,False)

    def reversa(self):

        gpio.output(der1,False)
        gpio.output(izq1,False)
        gpio.output(der2,True)
        gpio.output(izq2,True)

    def izq(self):

        gpio.output(der1,True)
        gpio.output(izq1,False)
        gpio.output(der2,False)
        gpio.output(izq2,True)

    def der(self):
        #En breve
        gpio.output(der1,False)
        gpio.output(izq1,True)
        gpio.output(der2,True)
        gpio.output(izq2,False)
