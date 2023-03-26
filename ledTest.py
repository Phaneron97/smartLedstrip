import RPi.GPIO as GPIO
import time

Red = 12
Green = 13
Blue = 18

GPIO.setmode(GPIO.BCM) # Set the pin numbering scheme
GPIO.setup(Red, GPIO.OUT) # Set up pin 12 as an output pin
GPIO.setup(Green, GPIO.OUT) # Set up pin 12 as an output pin
GPIO.setup(Blue, GPIO.OUT) # Set up pin 12 as an output pin


for i in range(3):
    GPIO.output(Red, GPIO.HIGH)
    print("Red ", Red, "ON")
    time.sleep(1)    
    GPIO.output(Red, GPIO.LOW)
    print("Red ", Red, "Off")
    time.sleep(1)   

    GPIO.output(Green, GPIO.HIGH)
    print("Green ", Green, "ON")
    time.sleep(1)    
    GPIO.output(Green, GPIO.LOW)
    print("Green ", Green, "Off")
    time.sleep(1)   

    GPIO.output(Blue, GPIO.HIGH)
    print("Blue ", Blue, "ON")
    time.sleep(1)    
    GPIO.output(Blue, GPIO.LOW)
    print("Blue ", Blue, "Off")
    time.sleep(1)   


GPIO.output(Red, GPIO.LOW)
GPIO.output(Green, GPIO.LOW)
GPIO.output(Blue, GPIO.LOW)
GPIO.cleanup()





