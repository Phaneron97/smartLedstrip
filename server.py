from flask import Flask, render_template, redirect, url_for, request
import threading
from py_classes.fireplace import Fireplace
from py_classes.rainbow import Rainbow
from py_classes.thread import Thread

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

fireplace = Fireplace(red_pin, green_pin, blue_pin)
rainbow = Rainbow(red_pin, green_pin, blue_pin) # , colors

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
    rainbow.stop()
    # fireplace.turn_off()
    return render_template('index.html')
    

@app.route("/process_fireplace", methods=['POST'])
def process_fireplace():
    # Requet results from HTML form

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

    running = threading.Event()
    running.set()
    thread = threading.Thread(
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
    thread.start()
    return render_template('index.html')


@app.route("/process_rainbow", methods=['POST'])
def process_rainbow():
    thread = threading.Thread(
        target=start_rainbow
    )
    thread.start()
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
