from flask import Flask, render_template, redirect, url_for, request
from py_classes.fireplace import Fireplace

red_pin = 12
green_pin = 13
blue_pin = 18
fireplace = Fireplace(red_pin, green_pin, blue_pin)

app = Flask(__name__)

# Defining the home page of our site
@app.route("/")  # this sets the route to this page
def index():
	# return "Hello! this is the main page <h1>HELLO</h1>"  # some basic inline html
    return render_template('index.html')


@app.route("/process_form", methods=['POST'])
def process_form():
    name = request.form['testName']
    testSlider = int(request.form['testSlider'])
    fireplace.start(
        red_duty_cycle=testSlider, 
        red_frequency=testSlider, 
        green_duty_cycle=testSlider, 
        green_frequency=testSlider, 
        blue_duty_cycle=testSlider, 
        blue_frequency=testSlider, 
        sleep_time=testSlider)
    # Create a Fireplace object with the three PWM pins
    
    return


if __name__ == "__main__":
    app.run(debug=True)