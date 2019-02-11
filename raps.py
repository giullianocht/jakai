import RPi.GPIO as gpio  	 # libreria para utilizar los puertos de entrada y salida
from time import sleep


motor_der1 = 18
motor_der2 = 19
motor_izq1 = 20
motor_izq2 = 21     					 #definimos los pines de GPIO a utilizar


gpio.setmode(gpio.BCM) 			# modo BCM de la raspberry pi (Broadcom SOC channel)

gpio.setup(motor_der1,gpio.OUT) # Se configura el motor Der 1
gpio.setup(motor_der2,gpio.OUT) # Se configura el motor Der 2
gpio.setup(motor_izq1,gpio.OUT) # Se configura el motor Izq 1
gpio.setup(motor_izq2,gpio.OUT) # Se configura el motor Izq 2
