from py_classes.fireplace import Fireplace
from py_classes.rainbow import Rainbow
from py_classes.colorpicker import Colorpicker

from flask import Flask, render_template, redirect, url_for, request

class LEDController:
    def __init__(self, red_pin, green_pin, blue_pin):
        self.red_pin = red_pin
        self.green_pin = green_pin
        self.blue_pin = blue_pin
        self.fireplace = Fireplace(self.red_pin, self.green_pin, self.blue_pin)
        self.rainbow = Rainbow(self.red_pin, self.green_pin, self.blue_pin)
        self.colorpicker = Colorpicker(self.red_pin, self.green_pin, self.blue_pin)
        self.fireplace_thread = None
        self.rainbow_thread = None
        self.colorpicker_thread = None

    def start_fireplace(self, *args):
        self.fireplace.start(*args)

    def start_rainbow(self):
        self.rainbow.start()
        
    def start_colorpicker(self, hexcolor):
        self.colorpicker.start(hexcolor)

    def get_form_field_values(self, form_fields):
        values = {} # Empty value list
        print("empty list values")
        for form_field, variable_name in form_fields.items():
            values[variable_name] = float(request.form.get(form_field))
        return [values[key] for key in form_fields.values()]
    
    
    def values_changed(self, new_values, old_values):
        if len(new_values) != len(old_values): # length of new_values != length of old_values
            return True # length is not the same, so the values have changed, return true

        for new_val, old_val in zip(new_values, old_values): # new and old values comparison in 1 tuple and loop through them
            if new_val != old_val: # if new values does not equal old value, so the values have changed, return true
                return True

        return False

