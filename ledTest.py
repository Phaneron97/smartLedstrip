import RPi.GPIO as GPIO
import time

ledPin = 12

GPIO.setmode(GPIO.BCM) # Set the pin numbering scheme
GPIO.setup(ledPin, GPIO.OUT) # Set up pin 12 as an output pin


while 1:
    GPIO.output(ledPin, GPIO.HIGH)
    print("GPIO", ledPin, "ON")
    time.sleep(1)
    GPIO.output(ledPin, GPIO.LOW)
    print("Led OFF")
    time.sleep(1)


