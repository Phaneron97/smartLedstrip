from py_classes.fireplace import Fireplace
from py_classes.rainbow import Rainbow
from flask import Flask, render_template, redirect, url_for, request

class LEDController:
    def __init__(self):
        self.red_pin = 12
        self.green_pin = 13
        self.blue_pin = 18
        self.fireplace = Fireplace(self.red_pin, self.green_pin, self.blue_pin)
        self.rainbow = Rainbow(self.red_pin, self.green_pin, self.blue_pin)
        self.fireplace_thread = None
        self.rainbow_thread = None

    def start_fireplace(self, *args):
        self.fireplace.start(*args)

    def start_rainbow(self):
        self.rainbow.start()

    def get_form_field_values(self, form_fields):
        values = {}
        print("empty list values")
        for form_field, variable_name in form_fields.items():
            # print(values[variable_name])
            values[variable_name] = float(request.form.get(form_field))
        return [values[key] for key in form_fields.values()]
