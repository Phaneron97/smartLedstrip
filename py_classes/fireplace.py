# import RPi.GPIO as GPIO
# import random
# import time

# GPIO.setmode(GPIO.BCM)

# class Fireplace:
#     def __init__(self, red_pin, green_pin, blue_pin):
#         self.leds = [LED(red_pin), LED(green_pin), LED(blue_pin)]

#     def flicker(self):
#         for led in self.leds:
#             # Randomly generate duty cycle and frequency values for each LED
#             if led.pin == red_pin:
#                 duty_cycle = random.uniform(20, 100)
#                 frequency = random.uniform(50, 100)
#             elif led.pin == green_pin:
#                 duty_cycle = random.uniform(0, 3)
#                 frequency = random.uniform(90, 100)
#             elif led.pin == blue_pin:
#                 duty_cycle = random.uniform(0, 1)
#                 frequency = random.uniform(90, 100)
#             else:
#                 print("no led found")

#             led.set_duty_cycle(duty_cycle)
#             led.set_frequency(frequency)
#             led.set_sleep(sleeptime)

#     def start(self):
#         try:
#             while True:
#                 self.flicker()
#                 time.sleep(random.uniform(0.08, 0.15))
#         except KeyboardInterrupt:
#             for led in self.leds:
#                 led.pwm.stop()
#             GPIO.cleanup()

# # Define the PWM pins for the red, green, and blue LEDs
# red_pin = 12
# green_pin = 13
# blue_pin = 18

# # Create a Fireplace object with the three PWM pins
# fireplace = Fireplace(red_pin, green_pin, blue_pin)

# # Start the fireplace effect
# fireplace.start()

import random
import time
from py_classes.led import LED

class Fireplace:
    def __init__(self, red_pin, green_pin, blue_pin):
        self.leds = [LED(red_pin), LED(green_pin), LED(blue_pin)]
        self.red_pin = red_pin
        self.green_pin = green_pin
        self.blue_pin = blue_pin

    def flicker(self, red_duty_cycle, red_frequency, green_duty_cycle, green_frequency, blue_duty_cycle, blue_frequency, sleep_time):
        for led in self.leds:
            # Randomly generate duty cycle and frequency values for each LED
            if led.pin == self.red_pin:
                led.set_duty_cycle(red_duty_cycle)
                led.set_frequency(red_frequency)
            elif led.pin == self.green_pin:
                led.set_duty_cycle(green_duty_cycle)
                led.set_frequency(green_frequency)
            elif led.pin == self.blue_pin:
                led.set_duty_cycle(blue_duty_cycle)
                led.set_frequency(blue_frequency)
            else:
                print("no led found")

            # led.set_duty_cycle(duty_cycle)
            # led.set_frequency(frequency)
            led.set_sleep(sleep_time)

    def start(self, red_duty_cycle, red_frequency, green_duty_cycle, green_frequency, blue_duty_cycle, blue_frequency, sleep_time):
        try:
            while True:
                self.flicker(red_duty_cycle, red_frequency, green_duty_cycle, green_frequency, blue_duty_cycle, blue_frequency, sleep_time)
                # self.time.sleep(random.uniform(0.08, 0.15))
        except KeyboardInterrupt:
            for led in self.leds:
                led.pwm.stop()
            GPIO.cleanup()