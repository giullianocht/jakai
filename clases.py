#En proceso
class Robot:
    def __init__(self,un_nombre=""):
        self.nombre = un_nombre
    def avanzar(self):
        #En breve
        gpio.output(motor_der1,True)
        gpio.output(motor_izq1,True)
        gpio.output(motor_der1,False)
        gpio.output(motor_izq1,False)
    def reversa(self):
        #En breve
    def izq(self):
        #En breve
    def der(self):
        #En breve
