import RPi.GPIO as GPIO
import time
import math
import os
import threading
from py_classes.led import LED
from py_classes.hsv import HSVtoRGB


###################### using HSV ####################
class Rainbow:
    def __init__(self, red_pin, green_pin, blue_pin):
        self.red_pin = LED(red_pin)
        self.green_pin = LED(green_pin)
        self.blue_pin = LED(blue_pin)
        self.hsv_to_rgb = HSVtoRGB()
        self.rainbow_running = False
        
    def start(self):
        current_hue = 0 # starting hue
        starting_frequency = 100 # Hz
        
        # set starting frequency of all leds
        self.red_pin.set_frequency(starting_frequency)
        self.green_pin.set_frequency(starting_frequency)
        self.blue_pin.set_frequency(starting_frequency)
        
        self.rainbow_running = True
        while self.rainbow_running:
            for hue in range(361): # Range of hue              
                red, green, blue = self.hsv_to_rgb.convert(current_hue) # Convert the current hue value to RGB using the HSVtoRGB converter

                if self.rainbow_running == True: # Check if rainbow effect is turned on, if not: break immediatly
                    self.red_pin.set_duty_cycle(red)
                    self.green_pin.set_duty_cycle(green)
                    self.blue_pin.set_duty_cycle(blue)
                else:
                    break

                # hue resolution of 360
                current_hue = (current_hue + 1) % 360

                # time in seconds to wait between each color change
                time.sleep(0.01)
                

    def turn_off(self):
        # Set the flag variable to False to break out of the while loop in the thread
        self.rainbow_running = False

        # Stop the PWM for each LED color
        self.red_pin.turn_off()
        self.green_pin.turn_off()
        self.blue_pin.turn_off()