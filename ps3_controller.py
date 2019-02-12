import pygame
import time

pygame.init()
pygame.joystick.init()

joystick = pygame.joystick.Joystick(0)
joystick.init()

#print 'Initialised Joystick : %s' % joystick.get_name()
#print 'Press ESC to stop'

#screen = pygame.display.set_mode((100,100))

# get count of joysticks=1, axes=27, buttons=19 for DualShock 3

joystick_count = pygame.joystick.get_count()
print("joystick_count")
print(joystick_count)
print("--------------")

numaxes = joystick.get_numaxes()
print("numaxes")
print(numaxes)
print("--------------")

numbuttons = joystick.get_numbuttons()
print("numbuttons")
print(numbuttons)
print("--------------")
loopQuit = False
while loopQuit == False:
    time.sleep(0.5)
# test joystick axes
    for i in range(0,4):
        pygame.event.pump()
        axis = joystick.get_axis(i)
        print("Axis " + str(i) + " = " + str(axis))
    print("--------------")

    #test controller buttons
    for i in range(0,numbuttons):
        pygame.event.pump()
        button = joystick.get_button(i)
        if i == 9 and button == 1:
            loopQuit = True
        if i == 0 and button == 1:
            print ("Apretaste X")
        if i == 1 and button == 1:
            print ("Apretaste Circulo")
        if i == 2 and button == 1:
            print ("Apretaste Triangulo")
        if i == 3 and button == 1:
            print ("Apretaste Cuadrado")

pygame.quit()
