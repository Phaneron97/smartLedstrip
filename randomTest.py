import RPi.GPIO as GPIO
import time

red_pin = 12
green_pin = 13
blue_pin = 18

GPIO.setmode(GPIO.BCM)
GPIO.setup(red_pin, GPIO.OUT)
GPIO.setup(green_pin, GPIO.OUT)
GPIO.setup(blue_pin, GPIO.OUT)

pause = 0.5

while True:
    GPIO.output(red_pin, GPIO.HIGH)    
    time.sleep(pause)
    GPIO.output(red_pin, GPIO.LOW)
    GPIO.output(green_pin, GPIO.HIGH)    
    time.sleep(pause)
    GPIO.output(green_pin, GPIO.LOW)
    GPIO.output(blue_pin, GPIO.HIGH)    
    time.sleep(pause)
    GPIO.output(blue_pin, GPIO.LOW)
    
