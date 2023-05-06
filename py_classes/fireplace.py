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

class Fireplace(LED):
    def __init__(self, red_pin, green_pin, blue_pin):
        # self.leds = [LED(red_pin), LED(green_pin), LED(blue_pin)]
        # self.red_pin = red_pin
        # self.green_pin = green_pin
        # self.blue_pin = blue_pin

        # New
        super().__init__(red_pin)
        self.green_led = LED(green_pin)
        self.blue_led = LED(blue_pin)


    def flicker(self, 
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
        red_duty_cycle = random.uniform(random.uniform(minBrightnessRed-5, minBrightnessRed+5), random.uniform(maxBrightnessRed-5, maxBrightnessRed))
        red_frequency = random.uniform(minFreqRed, maxFreqRed)

        green_duty_cycle = random.uniform(random.uniform(minBrightnessGreen-5, minBrightnessGreen+5), random.uniform(maxBrightnessGreen-5, maxBrightnessGreen))
        green_frequency = random.uniform(minFreqGreen, maxFreqGreen)

        blue_duty_cycle = random.uniform(random.uniform(minBrightnessBlue-5, minBrightnessBlue+5), random.uniform(maxBrightnessBlue-5, maxBrightnessBlue))
        blue_frequency = random.uniform(minFreqBlue, maxFreqBlue)

        # Set dutycycle and frequency per led
        self.set_duty_cycle(red_duty_cycle)
        self.set_frequency(red_frequency)

        self.green_led.set_duty_cycle(green_duty_cycle)
        self.green_led.set_frequency(green_frequency)

        self.blue_led.set_duty_cycle(blue_duty_cycle)
        self.blue_led.set_frequency(blue_frequency)


        print("red duty", self.get_duty_cycle())
        print("red freq", self.get_frequency())
        print()
        print("green duty", self.green_led.get_duty_cycle())
        print("green freq", self.green_led.get_frequency())
        print()
        print("blue duty", self.blue_led.get_duty_cycle())
        print("blue freq", self.blue_led.get_frequency())
        print("-----------")

        # for led in self.leds:
        #     # Randomly generate duty cycle and frequency values for each LED
        #     if led.pin == self.red_pin:
        #         led.set_duty_cycle(random.uniform(random.uniform(minBrightnessRed-5, minBrightnessRed+5), random.uniform(maxBrightnessRed-5, maxBrightnessRed)))
        #         print("red duty cycle", led.get_duty_cycle())
        #         led.set_frequency(random.uniform(minFreqRed, maxFreqRed))
        #     elif led.pin == self.green_pin:
        #         led.set_duty_cycle(random.uniform(random.uniform(minBrightnessGreen-5, minBrightnessGreen+5), random.uniform(maxBrightnessGreen-5, maxBrightnessGreen)))
        #         print("green duty cycle", led.get_duty_cycle())
        #         led.set_frequency(random.uniform(minFreqGreen, maxFreqGreen))
        #     elif led.pin == self.blue_pin:
        #         led.set_duty_cycle(random.uniform(random.uniform(minBrightnessBlue-5, minBrightnessBlue+5), random.uniform(maxBrightnessBlue-5, maxBrightnessBlue)))
        #         print("blue duty cycle", led.get_duty_cycle())
        #         led.set_frequency(random.uniform(minFreqBlue, maxFreqBlue))
        #     else:
        #         print("no led found in fireplace")

            # led.set_duty_cycle(duty_cycle)
            # led.set_frequency(frequency)
        # led.set_sleep(random.uniform(minSleep, maxSleep))
        self.set_sleep(random.uniform(minSleep, maxSleep))
        self.green_led.set_sleep(random.uniform(minSleep, maxSleep))
        self.blue_led.set_sleep(random.uniform(minSleep, maxSleep))


    def start(
        self, 
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
        try:
            while True:
                self.flicker(
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
                    maxSleep)
                # self.time.sleep(random.uniform(0.08, 0.15))
        except KeyboardInterrupt:
            for led in self.leds:
                led.pwm.stop()
            GPIO.cleanup()


# class Fireplace:
#     def __init__(self, red_pin, green_pin, blue_pin):
#         self.leds = [LED(red_pin), LED(green_pin), LED(blue_pin)]

#     def flicker(self, led_settings, sleep_range):
#         for led in self.leds:
#             if led.pin in led_settings:
#                 settings = led_settings[led.pin]
#                 led.set_duty_cycle(random.uniform(settings["min_brightness"], settings["max_brightness"]))
#                 led.set_frequency(random.uniform(settings["min_frequency"], settings["max_frequency"]))
#             else:
#                 print(f"No settings found for LED pin {led.pin}")
#             led.set_sleep(random.uniform(sleep_range[0], sleep_range[1]))

#     def start(self, settings):
#         try:
#             while True:
#                 self.flicker(settings["leds"], settings["sleep_range"])
#         except KeyboardInterrupt:
#             for led in self.leds:
#                 led.pwm.stop()
#             GPIO.cleanup()