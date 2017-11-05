import spidev 
import RPi.GPIO as GPIO 
import time 
 
GPIO.setmode(GPIO.BOARD) 
GPIO.setup(29,GPIO.OUT) 
GPIO.setup(31,GPIO.OUT) 
spi=spidev.SpiDev() 
#print('reset') 
#time.sleep(1) 
#print('Srart') 
 
spi.open(0,0) 
spi.max_speed_hz=10000 
spi.xfer([0b11000000]) 
spi.xfer([0x16]) 
spi.xfer([7]) 
spi.xfer([0b01011000]) 
 
spi.open(0,1) 
spi.max_speed_hz=10000 
spi.xfer([0b11000000]) 
spi.xfer([0x16]) 
spi.xfer([7]) 
spi.xfer([0b01011000]) 
 
for i in range(66958): 
    GPIO.output(29,True) 
    GPIO.output(31,True) 
    time.sleep(0.000001) 
    GPIO.output(29,False) 
    GPIO.output(31,False) 
    time.sleep(0.000001) 
    print(i/200) 
spi.open(0,0) 
spi.xfer([0b11000000]) 
spi.open(0,1) 
spi.xfer([0b11000000]) 
spi.close() 
GPIO.cleanup()
