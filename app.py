from flask import Flask, render_template, redirect, url_for, request
import threading
import time
from py_classes.fireplace import Fireplace # Lighting effect
from py_classes.rainbow import Rainbow # Lighting effect
from py_classes.colorpicker import Colorpicker # Lighting effect
from py_classes.thread import ThreadManager # Threading between lighting effects
from py_classes.ledcontroller import LEDController # Controlling threading and starting lighting effects

# Set pin numbers according to raspberry pi's pin layout 
red_pin = 12 # PWM0
green_pin = 13 # PWM1
blue_pin = 18 # PWM0

app = Flask(__name__)

# Object ledcontroller which starts lighting effects and checks value lists
led_controller = LEDController(red_pin, green_pin, blue_pin) 

@app.route("/")
def index(): # homepage
    return render_template('index.html')


@app.route("/process_turnoff", methods=['POST'])
def process_turnoff():    
    # dictionary of possible open threads
    thread_mapping = {
        'fireplace': led_controller.fireplace_thread,
        'rainbow': led_controller.rainbow_thread,
        'colorpicker': led_controller.colorpicker_thread
    }

    # loop through all threads, when one is not none (IE open), terminate it (join)
    for thread_name, thread in thread_mapping.items():
        if thread is not None: # Only turn off if current thread exists
            getattr(led_controller, thread_name).turn_off() # get object from current led_cntroller and call turn_off function
            thread.terminate() # terminate (join) thread
            setattr(led_controller, f"{thread_name}_thread", None) # clean up thread to consider it completed, continue on main

    return render_template('index.html')


@app.route("/process_fireplace", methods=['POST'])
def process_fireplace():    
    process_turnoff()
    
    # make a set form_fields (unordered, unchangeable, unindexed)
    form_fields = {
        'minBrightnessRed': 'min_brightness_red',
        'maxBrightnessRed': 'max_brightness_red',
        'minFreqRed': 'min_freq_red',
        'maxFreqRed': 'max_freq_red',
        'minBrightnessGreen': 'min_brightness_green',
        'maxBrightnessGreen': 'max_brightness_green',
        'minFreqGreen': 'min_freq_green',
        'maxFreqGreen': 'max_freq_green',
        'minBrightnessBlue': 'min_brightness_blue',
        'maxBrightnessBlue': 'max_brightness_blue',
        'minFreqBlue': 'min_freq_blue',
        'maxFreqBlue': 'max_freq_blue',
        'minSleep': 'min_sleep',
        'maxSleep': 'max_sleep',
    }

    values = led_controller.get_form_field_values(form_fields) # Get form fields from form_fields and 

    if led_controller.values_changed(values, led_controller.fireplace_values):
        print("values in fireplace have changed")
        led_controller.fireplace_values = values

        if led_controller.fireplace_thread is not None and led_controller.fireplace_thread.alive():
            led_controller.fireplace_thread.terminate()
            led_controller.fireplace_thread = None

        led_controller.fireplace_thread = ThreadManager(target=led_controller.start_fireplace, args=values)

    if not led_controller.fireplace_thread.alive():
        led_controller.fireplace_thread.start()
        print("Fireplace started")

    return render_template('index.html')


@app.route("/process_rainbow", methods=['POST'])
def process_rainbow():
    process_turnoff()
        
    led_controller.rainbow_thread = ThreadManager(target=led_controller.start_rainbow)
    
    if not led_controller.rainbow_thread.alive():
        led_controller.rainbow_thread.start()
        print("Rainbow started")
    
    return render_template('index.html')


@app.route("/process_colorpicker", methods=['POST'])
def process_colorpicker():
    process_turnoff() 
    hexcolor = request.form['favcolor']
    print("User wants color:", hexcolor)    

    led_controller.colorpicker_thread = ThreadManager(target=led_controller.start_colorpicker, args=(hexcolor,))
    
    if not led_controller.colorpicker_thread.alive():
        led_controller.colorpicker_thread.start()
        print("Colorpicker started")

    return render_template('index.html')


# finally start the server on 0.0.0.0 (whole local network)
if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
