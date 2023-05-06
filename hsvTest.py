import time
import RPi.GPIO as GPIO

# Set the pins for the RGB LEDs
led_pin_red = 12
led_pin_green = 13
led_pin_blue = 18

# Set the mode for GPIO pins
GPIO.setmode(GPIO.BCM)

# Set up the GPIO pins for output
GPIO.setup(led_pin_red, GPIO.OUT)
GPIO.setup(led_pin_green, GPIO.OUT)
GPIO.setup(led_pin_blue, GPIO.OUT)

# Set up the PWM for each LED color
pwm_red = GPIO.PWM(led_pin_red, 100)
pwm_green = GPIO.PWM(led_pin_green, 100)
pwm_blue = GPIO.PWM(led_pin_blue, 100)

# Start the PWM for each LED color
pwm_red.start(0)
pwm_green.start(0)
pwm_blue.start(0)

# Loop through all the possible hue values (0-360 degrees) and set the color of the LEDs accordingly
while True:
    for hue in range(361):
        # Convert the hue value to RGB manually using HSV values
        saturation = 1.0
        value = 1.0
        c = value * saturation
        x = c * (1 - abs((hue/60) % 2 - 1))
        m = value - c
        hue_index = hue // 60
        r, g, b = (0, 0, 0)
        if hue_index == 0:
            r, g, b = c, x, 0
        elif hue_index == 1:
            r, g, b = x, c, 0
        elif hue_index == 2:
            r, g, b = 0, c, x
        elif hue_index == 3:
            r, g, b = 0, x, c
        elif hue_index == 4:
            r, g, b = x, 0, c
        elif hue_index == 5:
            r, g, b = c, 0, x
        red = int((r + m) * 100)
        green = int((g + m) * 100)
        blue = int((b + m) * 100)
        
        # Set the duty cycle of each PWM channel
        pwm_red.ChangeDutyCycle(red)
        pwm_green.ChangeDutyCycle(green)
        pwm_blue.ChangeDutyCycle(blue)
        
        # Wait a short time before updating the color again
        time.sleep(0.01)

# Stop the PWM for each LED color
pwm_red.stop()
pwm_green.stop()
pwm_blue.stop()

# Clean up the GPIO pins
GPIO.cleanup()