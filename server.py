from flask import Flask, render_template, redirect, url_for, request
import threading
import time
from py_classes.fireplace import Fireplace
from py_classes.rainbow import Rainbow
# from py_classes.thread import Thread

red_pin = 12
green_pin = 13
blue_pin = 18

# colors = [
#     (100, 1, 100),  # Violet
#     (50, 1, 50),  # Indigo
#     (1, 1, 100),  # Blue
#     (1, 100, 1),  # Green
#     (100, 100, 1),  # Yellow
#     (100, 50, 1),  # Orange
#     (100, 1, 1)  # Red
# ]


# List to store active threads
# active_threads = []

# def create_thread():
#     for thread in active_threads:
#         thread.join()        


fireplace = Fireplace(red_pin, green_pin, blue_pin)
rainbow = Rainbow(red_pin, green_pin, blue_pin) # ,colors (extra parameter without HSV)

# Initialize the thread instances
# thread = threading.Thread()

fireplace_thread = None
rainbow_thread = None

# Initialize the thread instance
# thread = Thread()

app = Flask(__name__)

def start_rainbow():
    rainbow.start()

def start_fireplace(
    minBrightnessRed, 
    maxBrightnessRed,
    minFreqRed,
    maxFreqRed,
    minBrightnessGreen,
    maxBrightnessGreen,
    minFreqGreen,
    maxFreqGreen,
    minBrightnessBlue,
    maxBrightnessBlue,
    minFreqBlue,
    maxFreqBlue,
    minSleep,
    maxSleep):
    # Create a Fireplace object with the three PWM pins
    fireplace.start(
        minBrightnessRed = minBrightnessRed, 
        maxBrightnessRed = maxBrightnessRed,
        minFreqRed = minFreqRed,
        maxFreqRed = maxFreqRed,
        minBrightnessGreen = minBrightnessGreen,
        maxBrightnessGreen = maxBrightnessGreen,
        minFreqGreen = minFreqGreen,
        maxFreqGreen = maxFreqGreen,
        minBrightnessBlue = minBrightnessBlue,
        maxBrightnessBlue = maxBrightnessBlue,
        minFreqBlue = minFreqBlue,
        maxFreqBlue = maxFreqBlue,
        minSleep = minSleep,
        maxSleep = maxSleep)

# Defining the home page of our site
@app.route("/")  # this sets the route to this page
def index():
	# return "Hello! this is the main page <h1>HELLO</h1>"  # some basic inline html
    return render_template('index.html')


@app.route("/process_turnoff", methods=['POST'])
def process_turnoff():
    global fireplace_thread, rainbow_thread

    if fireplace_thread is not None:
        fireplace.turn_off()
        fireplace_thread.join()
        fireplace_thread = None        

    if rainbow_thread is not None:
        rainbow.turn_off()
        rainbow_thread.join()
        rainbow_thread = None

    return render_template('index.html')


@app.route("/process_fireplace", methods=['POST'])
def process_fireplace():
    global fireplace_thread, rainbow_thread
    
    # if fireplace_thread is not None:
    #     print("Fireplace turning off")
    #     fireplace.turn_off()
    #     fireplace_thread.join()
    # if thread.is_alive():
    #     if fireplace.is_running():
    #         fireplace.turn_off()
    #     if rainbow.is_running():
    #         rainbow.stop()
    #     thread.stop()
    #     thread.join()
    
    # if thread.is_alive():
    #     thread.join()
        

    # Red
    minBrightnessRed = float(request.form.get('minBrightnessRed'))
    maxBrightnessRed = float(request.form.get('maxBrightnessRed'))
    minFreqRed = float(request.form.get('minFreqRed'))
    maxFreqRed = float(request.form.get('maxFreqRed'))

    # Green 
    minBrightnessGreen = float(request.form.get('minBrightnessGreen'))
    maxBrightnessGreen = float(request.form.get('maxBrightnessGreen'))
    minFreqGreen = float(request.form.get('minFreqGreen'))
    maxFreqGreen = float(request.form.get('maxFreqGreen'))

    # Blue
    minBrightnessBlue = float(request.form.get('minBrightnessBlue'))
    maxBrightnessBlue = float(request.form.get('maxBrightnessBlue'))
    minFreqBlue = float(request.form.get('minFreqBlue'))
    maxFreqBlue = float(request.form.get('maxFreqBlue'))

    # Sleep
    minSleep = float(request.form.get('minSleep'))
    maxSleep = float(request.form.get('maxSleep'))

    # minSleep = request.form.get('minSleep')
    # maxSleep = request.form.get('maxSleep')

    # testSlider = int(request.form['testSlider'])
    # fireplace_list = request.form.get('sliderValues')
    # fireplace_values = fireplace_list.split(',')
    # red_duty_cycle_min = int(fireplace_values[0])
    # red_duty_cycle_max = int(fireplace_values[1])
    if fireplace_thread is None:   
        if rainbow_thread is not None: # Check if other thread is already running, if so, turn that one off
            rainbow.turn_off()
            rainbow_thread.join()
            rainbow_thread = None
        fireplace_thread = threading.Thread(
            target=start_fireplace, 
            args=(
                minBrightnessRed, 
                maxBrightnessRed,
                minFreqRed,
                maxFreqRed,
                minBrightnessGreen,
                maxBrightnessGreen,
                minFreqGreen,
                maxFreqGreen,
                minBrightnessBlue,
                maxBrightnessBlue,
                minFreqBlue,
                maxFreqBlue,
                minSleep,
                maxSleep))
    
    # active_threads.append(fireplace_thread) # append to list of active threads    
    
    if not fireplace_thread.is_alive():
        fireplace_thread.start() # start current thread
        print("fireplace started")
    # create_thread()
            
    return render_template('index.html')


@app.route("/process_rainbow", methods=['POST'])
def process_rainbow():
    # rainbow_thread = threading.Thread(target=start_rainbow)
    
    # active_threads.append(rainbow_thread) # append to list of active threads    
    # rainbow_thread.start() # start current thread
    # create_thread()
    
    global fireplace_thread, rainbow_thread

    # if rainbow_thread is not None:
    #     print("Rainbow turning off")
    #     rainbow.turn_off()
    #     rainbow_thread.join()

    if rainbow_thread is None:
        if fireplace_thread is not None:
            fireplace.turn_off()
            fireplace_thread.join()
            fireplace_thread = None     
        rainbow_thread = threading.Thread(target=start_rainbow)
    
    if not rainbow_thread.is_alive():
        rainbow_thread.start()        
        # print(rainbow_thread.is_alive())
        print("rainbow started")
    
    return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True)

# from flask import Flask, render_template, redirect, url_for, request
# import threading
# from py_classes.fireplace import Fireplace

# app = Flask(__name__)

# # Define the settings for the Fireplace object
# settings = {
#     "leds": {
#         12: {"min_brightness": 0, "max_brightness": 255, "min_frequency": 1, "max_frequency": 5},
#         13: {"min_brightness": 0, "max_brightness": 255, "min_frequency": 1, "max_frequency": 5},
#         18: {"min_brightness": 0, "max_brightness": 255, "min_frequency": 1, "max_frequency": 5}
#     },
#     "sleep_range": (0.4, 0.7)
# }

# # Create a Fireplace object with the settings
# fireplace = Fireplace(settings)

# # Define the home page of our site
# @app.route("/")
# def index():
#     return render_template('index.html')

# # Process the form data and start the Fireplace object in a separate thread
# @app.route("/process_form", methods=['POST'])
# def process_form():
#     # Get the form data
#     form_data = request.form.to_dict()

#     # Update the settings dictionary with the form data
#     for led_pin, led_settings in settings['leds'].items():
#         for setting_name in led_settings.keys():
#             form_key = f"{led_pin}_{setting_name}"
#             if form_key in form_data:
#                 form_value = float(form_data[form_key])
#                 settings['leds'][led_pin][setting_name] = form_value

#     # Start the Fireplace object in a separate thread
#     thread = threading.Thread(target=fireplace.start)
#     thread.start()

#     return redirect(url_for('index'))

# if __name__ == "__main__":
#     app.run(debug=True)
