# import RPi.GPIO as GPIO
# import random
# import time

# GPIO.setmode(GPIO.BCM)

# class LED:
#     def __init__(self, pin, time):
#         self.pin = pin
#         GPIO.setup(self.pin, GPIO.OUT)
#         self.pwm = GPIO.PWM(self.pin, 100)
#         self.pwm.start(0)

#     def set_duty_cycle(self, duty_cycle):
#         self.pwm.ChangeDutyCycle(duty_cycle)

#     def set_frequency(self, frequency):
#         self.pwm.ChangeFrequency(frequency)

#     def set_sleep(self, sleeptime):
#         self.time.sleep(sleeptime)

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
from led import LED

class Fireplace:
    def __init__(self, red_pin, green_pin, blue_pin):
        self.leds = [LED(red_pin), LED(green_pin), LED(blue_pin)]
        self.red_pin = red_pin
        self.green_pin = green_pin
        self.blue_pin = blue_pin

    def flicker(self):
        for led in self.leds:
            # Randomly generate duty cycle and frequency values for each LED
            if led.pin == self.red_pin:
                duty_cycle = random.uniform(20, 100)
                frequency = random.uniform(50, 100)
            elif led.pin == self.green_pin:
                duty_cycle = random.uniform(0, 3)
                frequency = random.uniform(90, 100)
            elif led.pin == self.blue_pin:
                duty_cycle = random.uniform(0, 1)
                frequency = random.uniform(90, 100)
            else:
                print("no led found")

            led.set_duty_cycle(duty_cycle)
            led.set_frequency(frequency)
            led.set_sleep(random.uniform(0.05, 0.05))

    def start(self):
        try:
            while True:
                self.flicker()
                # self.time.sleep(random.uniform(0.08, 0.15))
        except KeyboardInterrupt:
            for led in self.leds:
                led.pwm.stop()
            GPIO.cleanup()