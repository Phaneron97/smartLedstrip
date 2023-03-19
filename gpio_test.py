import RPi.GPIO as GPIO

# Set the pin numbering scheme
GPIO.setmode(GPIO.BCM)

# Set up pin 12 as an output pin
GPIO.setup(12, GPIO.OUT)

# Turn on pin
def turn_on_pin(pinNo):
    GPIO.output(pinNo, GPIO.HIGH)

def turn_off_pin(pinNo):
    GPIO.output(pinNo, GPIO.LOW)