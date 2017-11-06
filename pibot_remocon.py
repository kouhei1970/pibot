import pygame,sys
from time import sleep
import spidev
import RPi.GPIO as GPIO

Delay1=0.0000000001
Delay2=0.0000001
def Forward():
    spi.open(0,0)
    spi.max_speed_hz=1000000
    spi.xfer([0b01011001])
    spi.close()
    spi.open(0,1)
    spi.max_speed_hz=1000000 
    spi.xfer([0b01011000])
    spi.close()

    GPIO.output(29,True) 
    GPIO.output(31,True) 
    sleep(Delay1)
    GPIO.output(29,False) 
    GPIO.output(31,False) 

def Back():
    spi.open(0,0)
    spi.max_speed_hz=1000000
    spi.xfer([0b01011000])
    spi.close()
    spi.open(0,1)
    spi.max_speed_hz=1000000 
    spi.xfer([0b01011001])
    spi.close()

    GPIO.output(29,True) 
    GPIO.output(31,True) 
    sleep(Delay1)
    GPIO.output(29,False) 
    GPIO.output(31,False) 
    #sleep(0.000001) 
    
def PivotTurnRight():
    spi.open(0,0)
    spi.max_speed_hz=1000000
    spi.xfer([0b01011000])
    spi.close()
    spi.open(0,1)
    spi.max_speed_hz=1000000 
    spi.xfer([0b01011000])
    spi.close()

    GPIO.output(29,True) 
    GPIO.output(31,True) 
    sleep(Delay1)
    GPIO.output(29,False) 
    GPIO.output(31,False) 
    #sleep(0.000001) 

def PivotTurnLeft():
    spi.open(0,0)
    spi.max_speed_hz=1000000
    spi.xfer([0b01011001])
    spi.close()
    spi.open(0,1)
    spi.max_speed_hz=1000000 
    spi.xfer([0b01011001])
    spi.close()

    GPIO.output(29,True) 
    GPIO.output(31,True) 
    sleep(Delay1)
    GPIO.output(29,False) 
    GPIO.output(31,False) 
    #sleep(0.000001) 

def TurnRight():
    spi.open(0,1)
    spi.max_speed_hz=1000000 
    spi.xfer([0b01011000])
    spi.close()

    GPIO.output(31,True) 
    sleep(Delay2)
    GPIO.output(31,False) 
    #sleep(0.000001) 

def TurnLeft():
    spi.open(0,0)
    spi.max_speed_hz=1000000
    spi.xfer([0b01011001])
    spi.close()

    GPIO.output(29,True) 
    sleep(Delay2)
    GPIO.output(29,False) 
    #sleep(0.000001) 

def BackTurnRight():
    spi.open(0,1)
    spi.max_speed_hz=1000000 
    spi.xfer([0b01011001])
    spi.close()

    GPIO.output(31,True) 
    sleep(Delay2)
    GPIO.output(31,False) 
    #sleep(0.000001) 

def BackTurnLeft():
    spi.open(0,0)
    spi.max_speed_hz=1000000
    spi.xfer([0b01011000])
    spi.close()

    GPIO.output(29,True) 
    sleep(Delay2)
    GPIO.output(29,False) 
    #sleep(0.000001) 

#################################################################
pygame.init()
window = pygame.display.set_mode((200, 200), 0, 32)

# how many joysticks connected to computer?
joystick_count = pygame.joystick.get_count()
print ("There is " + str(joystick_count) + " joystick/s")

if joystick_count == 0:
    # if no joysticks, quit program safely
    print ("Error, I did not find any joysticks")
    pygame.quit()
    sys.exit()
else:
    # initialise joystick
    joystick = pygame.joystick.Joystick(0)
    joystick.init()

    axes = joystick.get_numaxes()
    buttons = joystick.get_numbuttons()
    hats = joystick.get_numhats()

    print ("There is " + str(axes) + " axes")
    print ("There is " + str(buttons) + " button/s")
    print ("There is " + str(hats) + " hat/s")

#GPIO Setup
GPIO.setmode(GPIO.BOARD) 
GPIO.setup(29,GPIO.OUT) 
GPIO.setup(31,GPIO.OUT) 

#SPI Motor Driver L6470 Setup
spi=spidev.SpiDev()
spi.open(0,0) 
spi.max_speed_hz=10000 
spi.xfer([0b11000000]) 
spi.xfer([0x16]) 
spi.xfer([7]) 
spi.xfer([0b01011000]) 
spi.close()

spi.open(0,1) 
spi.max_speed_hz=10000 
spi.xfer([0b11000000]) 
spi.xfer([0x16]) 
spi.xfer([7]) 
spi.xfer([0b01011000]) 
spi.close()

comid=0
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    if joystick.get_button(3):
        spi.open(0,0) 
        spi.xfer([0b11000000]) 
        spi.close()
        spi.open(0,1) 
        spi.xfer([0b11000000]) 
        spi.close() 
        GPIO.cleanup()
        pygame.quit()
        sys.exit()
    joylr=joystick.get_axis(0)
    joyfb=joystick.get_axis(1)
    #print(joylr,joyfb)
    if joyfb<-0.8 and -0.6<joylr<0.6:
        comid+=1
        print(comid,'Forward')
        Forward()
    elif joyfb>0.8 and -0.6<joylr<0.6:
        comid+=1
        print(comid,'Back')
        Back()
    elif -0.6<joyfb<0.6 and joylr>0.8:
        comid+=1
        print(comid,'PivotTurnRight')
        PivotTurnRight()
    elif -0.6<joyfb<0.6 and joylr<-0.8:
        comid+=1
        print(comid,'PivotTurnLeft')
        PivotTurnLeft()
    elif joyfb<-0.8 and joylr>0.8:
        comid+=1
        print(comid,'TurnRight')
        TurnRight()
    elif joyfb<-0.8 and joylr<-0.8:
        comid+=1
        print(comid,'TurnLeft')
        TurnLeft()
    elif joyfb>0.8 and joylr>0.8:
        comid+=1
        print(comid,'BackTurnRight')
        BackTurnRight()
    elif joyfb>0.8 and joylr<-0.8:
        comid+=1
        print(comid,'BackTurnLeft')
        BackTurnLeft()

    #sleep(0.1)
