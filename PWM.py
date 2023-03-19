# import RPi.GPIO as GPIO
# import time

# GPIO.setmode(GPIO.BCM) # Use BCM numbering scheme for GPIO pins
# GPIO.setup(12, GPIO.OUT) # Set GPIO pin 12 as an output
# GPIO.setup(13, GPIO.OUT) # Set GPIO pin 13 as an output
# GPIO.setup(18, GPIO.OUT) # Set GPIO pin 18 as an output

# # Create PWM objects on GPIO pins 12, 13, and 18 with different frequencies and duty cycles
# pwm0 = GPIO.PWM(12, 45) # 50 Hz frequency for LED 1
# pwm1 = GPIO.PWM(13, 100) # 100 Hz frequency for LED 2
# pwm2 = GPIO.PWM(18, 1000) # 200 Hz frequency for LED 3

# # Start PWM with a duty cycle of 0% (LEDs are off)
# pwm0.start(0)
# pwm1.start(0)
# pwm2.start(0)


# while 1:

#     for dutyCycle in range (0, 101, 5): # start at 0, end at 101, increment with 10 each loop
#         pwm0.ChangeDutyCycle(dutyCycle)
#         pwm1.ChangeDutyCycle(dutyCycle) # Duty cycle for LED 2
#         pwm2.ChangeDutyCycle(dutyCycle) # Duty cycle for LED 3

#         time.sleep(0.1)

# pwm0.stop()
# pwm1.stop()
# pwm2.stop()
# GPIO.cleanup()

################# Fade and colors example #########

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM) # Use BCM numbering scheme for GPIO pins

# Set up PWM pins for red, green, and blue LEDs
GPIO.setup(12, GPIO.OUT) # Red LED on GPIO pin 12
GPIO.setup(13, GPIO.OUT) # Green LED on GPIO pin 13
GPIO.setup(18, GPIO.OUT) # Blue LED on GPIO pin 18

# Create PWM objects for each LED with a frequency of 100 Hz and a duty cycle of 0%
red_pwm = GPIO.PWM(12, 50)
green_pwm = GPIO.PWM(13, 50)
blue_pwm = GPIO.PWM(18, 50)
red_pwm.start(0)
green_pwm.start(0)
blue_pwm.start(0)

# Define some common colors
colors = {
    "red": (100, 0, 0),
    "green": (0, 100, 0),
    "blue": (0, 0, 100),
    "yellow": (100, 100, 0),
    "cyan": (0, 100, 100),
    "purple": (100, 0, 100),
    "white": (100, 100, 100),
}

# Define a function to set the color of the LEDs
def set_color(color):
    red_pwm.ChangeDutyCycle(color[0])
    green_pwm.ChangeDutyCycle(color[1])
    blue_pwm.ChangeDutyCycle(color[2])

# Define a function to fade the LEDs between two colors
def fade(from_color, to_color, duration):
    steps = 50 # Number of steps to take during the fade
    delay = duration / steps # Time to wait between steps
    r_step = (to_color[0] - from_color[0]) / steps # Red channel step size
    g_step = (to_color[1] - from_color[1]) / steps # Green channel step size
    b_step = (to_color[2] - from_color[2]) / steps # Blue channel step size
    for i in range(steps):
        r = from_color[0] + (i * r_step)
        g = from_color[1] + (i * g_step)
        b = from_color[2] + (i * b_step)
        set_color((r, g, b))
        time.sleep(delay)

# Set the initial color to white
set_color(colors["white"])

# Fade between some different colors
fade(colors["white"], colors["red"], 1)
fade(colors["red"], colors["green"], 1)
fade(colors["green"], colors["blue"], 1)
fade(colors["blue"], colors["purple"], 1)
fade(colors["purple"], colors["yellow"], 1)
fade(colors["yellow"], colors["cyan"], 1)
fade(colors["cyan"], colors["white"], 1)

# Clean up GPIO resources when done
red_pwm.stop()
green_pwm.stop()
blue_pwm.stop()
GPIO.cleanup()