import RPi.GPIO as GPIO
import time
import math

# Define the pins for the RGB LED
red_pin = 12
green_pin = 13
blue_pin = 18

class LED:
    def __init__(self, pin):
        self.pin = pin
        GPIO.setup(self.pin, GPIO.OUT)
        self.pwm = GPIO.PWM(self.pin, 100)
        self.pwm.start(0)

    def set_duty_cycle(self, duty_cycle):
        self.pwm.ChangeDutyCycle(duty_cycle)

    def set_frequency(self, frequency):
        self.pwm.ChangeFrequency(frequency)

class Rainbow:
    def __init__(self, red_pin, green_pin, blue_pin):
        self.leds = [LED(red_pin), LED(green_pin), LED(blue_pin)]

    def set_rgb(self, r, g, b):
        # Set the duty cycle and frequency for each LED to produce the specified RGB values
        self.leds[0].set_duty_cycle(r)
        self.leds[0].set_frequency(100)
        self.leds[1].set_duty_cycle(g)
        self.leds[1].set_frequency(100)
        self.leds[2].set_duty_cycle(b)
        self.leds[2].set_frequency(100)

    def rainbow_cycle(self, delay):
        # Cycle through the colors of the rainbow
        for i in range(0, 255):
            # Calculate the RGB values for the current position in the color spectrum
            # r = int(math.sin(i * math.pi / 255) * 255)
            r = max(min(int(math.sin(i * math.pi / 255) * 255), 100), 0)
            print(r)
            g = max(min(int(math.sin((i + 85) * math.pi / 255) * 255), 100), 0)
            print(g)
            # b = int(math.sin((i + 170) * math.pi / 255) * 255)
            b = max(min(int(math.sin((i + 170) * math.pi / 255) * 255), 100), 0)
            print(b)
            # Set the RGB values on the LED
            self.set_rgb(r, g, b)
            time.sleep(delay)

# Set up the GPIO pins
GPIO.setmode(GPIO.BCM)
GPIO.setup(red_pin, GPIO.OUT)
GPIO.setup(green_pin, GPIO.OUT)
GPIO.setup(blue_pin, GPIO.OUT)

# Create a Rainbow object and run the rainbow effect
rainbow = Rainbow(red_pin, green_pin, blue_pin)
rainbow.rainbow_cycle(0.01)

# Clean up the GPIO pins on exit
GPIO.cleanup()
