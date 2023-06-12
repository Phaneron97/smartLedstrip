import RPi.GPIO as GPIO
import time

# Set GPIO mode
GPIO.setmode(GPIO.BCM)

# Define LED pins
red_pin = 12
green_pin = 13
blue_pin = 18

GPIO.setup(red_pin, GPIO.OUT)
GPIO.setup(green_pin, GPIO.OUT)
GPIO.setup(blue_pin, GPIO.OUT)

# setup
while True:
    # GPIO.output(red_pin, GPIO.HIGH)
    # GPIO.output(green_pin, GPIO.HIGH)
    GPIO.output(blue_pin, GPIO.HIGH)
    
    time.sleep(1)
    
    # GPIO.output(red_pin, GPIO.LOW)
    # GPIO.output(green_pin, GPIO.LOW)
    GPIO.output(blue_pin, GPIO.LOW)

    time.sleep(1)

GPIO.cleanup()
