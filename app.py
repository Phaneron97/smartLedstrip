# from flask import Flask, render_template, redirect, url_for, request
# import threading
# import time
# from py_classes.fireplace import Fireplace
# from py_classes.rainbow import Rainbow
# from py_classes.thread import ThreadManager

# red_pin = 12
# green_pin = 13
# blue_pin = 18

# # colors = [
# #     (100, 1, 100),  # Violet
# #     (50, 1, 50),  # Indigo
# #     (1, 1, 100),  # Blue
# #     (1, 100, 1),  # Green
# #     (100, 100, 1),  # Yellow
# #     (100, 50, 1),  # Orange
# #     (100, 1, 1)  # Red
# # ]


# # List to store active threads
# # active_threads = []

# # def create_thread():
# #     for thread in active_threads:
# #         thread.join()        


# fireplace = Fireplace(red_pin, green_pin, blue_pin)
# rainbow = Rainbow(red_pin, green_pin, blue_pin) # ,colors (extra parameter without HSV)
# # threadmanager = ThreadManager()

# # Initialize the thread instances
# # thread = threading.Thread()

# fireplace_thread = None
# rainbow_thread = None

# # Initialize the thread instance
# # thread = Thread()

# app = Flask(__name__)


# def get_form_field_values(form_fields):
#     values = {}
#     for form_field, variable_name in form_fields.items():
#         values[variable_name] = float(request.form.get(form_field))
#     return [values[key] for key in form_fields.values()]


# def start_rainbow():
#     rainbow.start()

# # def start_fireplace(
# #     minBrightnessRed, 
# #     maxBrightnessRed,
# #     minFreqRed,
# #     maxFreqRed,
# #     minBrightnessGreen,
# #     maxBrightnessGreen,
# #     minFreqGreen,
# #     maxFreqGreen,
# #     minBrightnessBlue,
# #     maxBrightnessBlue,
# #     minFreqBlue,
# #     maxFreqBlue,
# #     minSleep,
# #     maxSleep):
# #     # Create a Fireplace object with the three PWM pins
# #     fireplace.start(
# #         minBrightnessRed = minBrightnessRed, 
# #         maxBrightnessRed = maxBrightnessRed,
# #         minFreqRed = minFreqRed,
# #         maxFreqRed = maxFreqRed,
# #         minBrightnessGreen = minBrightnessGreen,
# #         maxBrightnessGreen = maxBrightnessGreen,
# #         minFreqGreen = minFreqGreen,
# #         maxFreqGreen = maxFreqGreen,
# #         minBrightnessBlue = minBrightnessBlue,
# #         maxBrightnessBlue = maxBrightnessBlue,
# #         minFreqBlue = minFreqBlue,
# #         maxFreqBlue = maxFreqBlue,
# #         minSleep = minSleep,
# #         maxSleep = maxSleep)

# def start_fireplace(*args):
#     fireplace.start(*args)

# # Defining the home page of our site
# @app.route("/")  # this sets the route to this page
# def index():
# 	# return "Hello! this is the main page <h1>HELLO</h1>"  # some basic inline html
#     return render_template('index.html')


# @app.route("/process_turnoff", methods=['POST'])
# def process_turnoff():
#     global fireplace_thread, rainbow_thread
    
#     print("turning leds and all open threads off")

#     if fireplace_thread is not None:
#         fireplace.turn_off()
#         fireplace_thread.join()
#         fireplace_thread = None        

#     if rainbow_thread is not None:
#         rainbow.turn_off()
#         rainbow_thread.join()
#         rainbow_thread = None

#     return render_template('index.html')


# @app.route("/process_fireplace", methods=['POST'])
# def process_fireplace():
#     global fireplace_thread, rainbow_thread
    
#     # if fireplace_thread is not None:
#     #     print("Fireplace turning off")
#     #     fireplace.turn_off()
#     #     fireplace_thread.join()
#     # if thread.is_alive():
#     #     if fireplace.is_running():
#     #         fireplace.turn_off()
#     #     if rainbow.is_running():
#     #         rainbow.stop()
#     #     thread.stop()
#     #     thread.join()
    
#     # if thread.is_alive():
#     #     thread.join()
        

#     # # Red
#     # minBrightnessRed = float(request.form.get('minBrightnessRed'))
#     # maxBrightnessRed = float(request.form.get('maxBrightnessRed'))
#     # minFreqRed = float(request.form.get('minFreqRed'))
#     # maxFreqRed = float(request.form.get('maxFreqRed'))

#     # # Green 
#     # minBrightnessGreen = float(request.form.get('minBrightnessGreen'))
#     # maxBrightnessGreen = float(request.form.get('maxBrightnessGreen'))
#     # minFreqGreen = float(request.form.get('minFreqGreen'))
#     # maxFreqGreen = float(request.form.get('maxFreqGreen'))

#     # # Blue
#     # minBrightnessBlue = float(request.form.get('minBrightnessBlue'))
#     # maxBrightnessBlue = float(request.form.get('maxBrightnessBlue'))
#     # minFreqBlue = float(request.form.get('minFreqBlue'))
#     # maxFreqBlue = float(request.form.get('maxFreqBlue'))

#     # # Sleep
#     # minSleep = float(request.form.get('minSleep'))
#     # maxSleep = float(request.form.get('maxSleep'))
    
#     form_fields = {
#     'minBrightnessRed': 'min_brightness_red',
#     'maxBrightnessRed': 'max_brightness_red',
#     'minFreqRed': 'min_freq_red',
#     'maxFreqRed': 'max_freq_red',
#     'minBrightnessGreen': 'min_brightness_green',
#     'maxBrightnessGreen': 'max_brightness_green',
#     'minFreqGreen': 'min_freq_green',
#     'maxFreqGreen': 'max_freq_green',
#     'minBrightnessBlue': 'min_brightness_blue',
#     'maxBrightnessBlue': 'max_brightness_blue',
#     'minFreqBlue': 'min_freq_blue',
#     'maxFreqBlue': 'max_freq_blue',
#     'minSleep': 'min_sleep',
#     'maxSleep': 'max_sleep',
#     }

#     values = {}
#     for form_field, variable_name in form_fields.items():
#         values[variable_name] = float(request.form.get(form_field))
#     # print(values)
    
    
#     if fireplace_thread is None:   
#         if rainbow_thread is not None: # Check if other thread is already running, if so, turn that one off
#             rainbow.turn_off()
#             rainbow_thread.terminate()
#             rainbow_thread = None
        
#         # args = [
#         #     minBrightnessRed, 
#         #     maxBrightnessRed,
#         #     minFreqRed,
#         #     maxFreqRed,
#         #     minBrightnessGreen,
#         #     maxBrightnessGreen,
#         #     minFreqGreen,
#         #     maxFreqGreen,
#         #     minBrightnessBlue,
#         #     maxBrightnessBlue,
#         #     minFreqBlue,
#         #     maxFreqBlue,
#         #     minSleep,
#         #     maxSleep
#         # ]
#         # args = [values[key] for key in form_fields.values()]
#         values = get_form_field_values(form_fields)
#         fireplace_thread = ThreadManager(target=start_fireplace, args=values)
    
#     if not fireplace_thread.alive():
#         fireplace_thread.start() # start current thread
#         print("fireplace started")
#     # create_thread()
            
#     return render_template('index.html')


# @app.route("/process_rainbow", methods=['POST'])
# def process_rainbow():
#     # rainbow_thread = threading.Thread(target=start_rainbow)
    
#     # active_threads.append(rainbow_thread) # append to list of active threads    
#     # rainbow_thread.start() # start current thread
#     # create_thread()
    
#     global fireplace_thread, rainbow_thread

#     # if rainbow_thread is not None:
#     #     print("Rainbow turning off")
#     #     rainbow.turn_off()
#     #     rainbow_thread.join()

#     if rainbow_thread is None:
#         if fireplace_thread is not None:
#             fireplace.turn_off()
#             fireplace_thread.terminate()
#             fireplace_thread = None     
#         # rainbow_thread = threading.Thread(target=start_rainbow)
#         rainbow_thread = ThreadManager(target=start_rainbow)
    
#     if not rainbow_thread.alive():
#         rainbow_thread.start()        
#         # print(rainbow_thread.is_alive())
#         print("rainbow started")
    
#     return render_template('index.html')


# if __name__ == "__main__":
#     app.run(debug=True)

from flask import Flask, render_template, redirect, url_for, request
import threading
import time
from py_classes.fireplace import Fireplace # Lighting effect
from py_classes.rainbow import Rainbow # Lighting effect
from py_classes.colorpicker import Colorpicker # Lighting effect
from py_classes.thread import ThreadManager # Threading between lighting effects
from py_classes.ledcontroller import LEDController # Controlling threading and starting lighting effects

red_pin = 12
green_pin = 13
blue_pin = 18

app = Flask(__name__)
led_controller = LEDController(red_pin, green_pin, blue_pin)

@app.route("/")
def index():
    return render_template('index.html')


@app.route("/process_turnoff", methods=['POST'])
# def process_turnoff():
#     if led_controller.fireplace_thread is not None:
#         led_controller.fireplace.turn_off()
#         led_controller.fireplace_thread.join()
#         led_controller.fireplace_thread = None

#     if led_controller.rainbow_thread is not None:
#         led_controller.rainbow.turn_off()
#         led_controller.rainbow_thread.join()
#         led_controller.rainbow_thread = None
        
#     if led_controller.colorpicker_thread is not None:
#         led_controller.colorpicker.turn_off()
#         led_controller.colorpicker_thread.join()
#         led_controller.colorpicker_thread = None

#     return render_template('index.html')

def process_turnoff():    
    # dictionary of possible open threads
    thread_mapping = {
        'fireplace': led_controller.fireplace_thread,
        'rainbow': led_controller.rainbow_thread,
        'colorpicker': led_controller.colorpicker_thread
    }

    # loop through all threads, when one is not none (IE open), terminate it (join)
    for thread_name, thread in thread_mapping.items():
        if thread is not None:
            getattr(led_controller, thread_name).turn_off() # get object from current led_cntroller and call turn_off function
            thread.terminate() # terminate (join) thread
            setattr(led_controller, f"{thread_name}_thread", None) # clean up thread to consider it completed, continue on main

    return render_template('index.html')


@app.route("/process_fireplace", methods=['POST'])
def process_fireplace():    
    process_turnoff()
    
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

    values = led_controller.get_form_field_values(form_fields)

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



# finally start the server
if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
