import RPi.GPIO as GPIO
import time

# Set up the GPIO pins
RED_PIN = 12
GREEN_PIN = 13
BLUE_PIN = 18

frequency = 100

GPIO.setmode(GPIO.BCM)
GPIO.setup(RED_PIN, GPIO.OUT)
GPIO.setup(GREEN_PIN, GPIO.OUT)
GPIO.setup(BLUE_PIN, GPIO.OUT)

red_pwm = GPIO.PWM(RED_PIN, frequency)
green_pwm = GPIO.PWM(GREEN_PIN, frequency)
blue_pwm = GPIO.PWM(BLUE_PIN, frequency)

# Convert HSV to RGB
def hsv_to_rgb(hue, saturation, value):
    c = value * saturation
    x = c * (1 - abs((hue / 60) % 2 - 1))
    m = value - c

    if 0 <= hue < 60:
        r, g, b = c, x, 0
    elif 60 <= hue < 120:
        r, g, b = x, c, 0
    elif 120 <= hue < 180:
        r, g, b = 0, c, x
    elif 180 <= hue < 240:
        r, g, b = 0, x, c
    elif 240 <= hue < 300:
        r, g, b = x, 0, c
    elif 300 <= hue < 360:
        r, g, b = c, 0, x
    else:
        r, g, b = 0, 0, 0

    r = int((r + m) * 100)
    g = int((g + m) * 100)
    b = int((b + m) * 100)

    return r, g, b

# Rainbow effect
def rainbow_effect():
    duration = 120  # Duration of the effect in seconds
    steps = 100    # Number of hue steps
    interval = duration / steps

    for step in range(steps):
        hue = step * (360 / steps)
        r, g, b = hsv_to_rgb(hue, 1.0, 1.0)
        red_pwm.start(r)
        green_pwm.start(g)
        blue_pwm.start(b)
        time.sleep(interval)

# Run the rainbow effect
try:
    rainbow_effect()
except KeyboardInterrupt:
    pass
finally:
    red_pwm.stop()
    green_pwm.stop()
    blue_pwm.stop()
    GPIO.cleanup()
