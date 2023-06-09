import RPi.GPIO as GPIO
import time
import math
import os
import threading
from py_classes.led import LED


class Colorpicker:
    def __init__(self, red_pin, green_pin, blue_pin):
        self.red_pin = LED(red_pin)
        self.green_pin = LED(green_pin)
        self.blue_pin = LED(blue_pin)
        self.colorpicker_running = False
        
    def hex_to_rgb(self, hex_code): # Get hexcode from frontend (template/index.html)
        if hex_code.startswith('#'): # Check if hexcode starts with #
            hex_code = hex_code[1:]
        else:
            raise ValueError("Invalid hex code. It should start with '#' symbol.")
        
        if len(hex_code) != 6: # Check if hexcode is 6 chars long
            raise ValueError("Invalid hex code. It should have exactly six characters.")
    
        red = int(hex_code[0:2], 16) # Hex to Dec
        green = int(hex_code[2:4], 16)
        blue = int(hex_code[4:6], 16)
        
        return (red, green, blue) # Return final RGB values as a tuple
        
    def start(self, hexcolor):
        
        starting_frequency = 100 # Hz
        
        # set starting frequency of all leds
        self.red_pin.set_frequency(starting_frequency)
        self.green_pin.set_frequency(starting_frequency)
        self.blue_pin.set_frequency(starting_frequency)
        
        red, green, blue = self.hex_to_rgb(hexcolor)
        
        self.colorpicker_running = True
        
        while self.colorpicker_running: # Keep dutycycle constant
            self.red_pin.set_dutycycle(red)
            self.green_pin.set_dutycycle(green)
            self.blue_pin.set_dutycycle(blue)

    def turn_off(self):
        # Set the flag variable to False to break out of the while loop in the thread
        self.colorpicker_running = False

        # Stop the PWM for each LED color
        self.red_pin.turn_off()
        self.green_pin.turn_off()
        self.blue_pin.turn_off()