from flask import Flask, render_template, redirect, url_for, request
import threading
from py_classes.fireplace import Fireplace

red_pin = 12
green_pin = 13
blue_pin = 18
fireplace = Fireplace(red_pin, green_pin, blue_pin)

app = Flask(__name__)

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


@app.route("/process_form", methods=['POST'])
def process_form():
    # Requet results from HTML form
    minBrightnessRed = int(request.form.get('minBrightnessRed'))
    maxBrightnessRed = int(request.form.get('maxBrightnessRed'))
    minFreqRed = int(request.form.get('minFreqRed'))
    maxFreqRed = int(request.form.get('maxFreqRed'))

    minBrightnessGreen = int(request.form.get('minBrightnessGreen'))
    maxBrightnessGreen = int(request.form.get('maxBrightnessGreen'))
    minFreqGreen = int(request.form.get('minFreqGreen'))
    maxFreqGreen = int(request.form.get('maxFreqGreen'))

    minBrightnessBlue = int(request.form.get('minBrightnessBlue'))
    maxBrightnessBlue = int(request.form.get('maxBrightnessBlue'))
    minFreqBlue = int(request.form.get('minFreqBlue'))
    maxFreqBlue = int(request.form.get('maxFreqBlue'))

    minSleep = 0.4
    maxSleep = 0.7

    # minSleep = request.form.get('minSleep')
    # maxSleep = request.form.get('maxSleep')




    # testSlider = int(request.form['testSlider'])
    # fireplace_list = request.form.get('sliderValues')
    # fireplace_values = fireplace_list.split(',')
    # red_duty_cycle_min = int(fireplace_values[0])
    # red_duty_cycle_max = int(fireplace_values[1])
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


if __name__ == "__main__":
    app.run(debug=True)