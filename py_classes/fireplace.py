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

# # Define the PWM pins for the red, green_pin, and blue_pin LEDs
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
# from py_classes.fade import Fading
# from py_classes.pulse import Pulsing

class Fireplace():
    def __init__(self, red_pin, green_pin, blue_pin):
        # self.leds = [LED(red_pin), LED(green_pin), LED(blue_pin)]
        # self.red_pin = red_pin
        # self.green_pin = green_pin
        # self.blue_pin = blue_pin

        # New
        # super().__init__(red_pin)
        self.red_pin = LED(red_pin)
        self.green_pin = LED(green_pin)
        self.blue_pin = LED(blue_pin)
        self.fireplace_running = False
        
        # self.red_fader = Fading(red_pin)
        # self.red_pulser = Pulsing(red_pin)
        
        # self.green_fader = Fading(green_pin)
        # self.green_pulser = Pulsing(green_pin)
        
        # self.blue_fader = Pulsing(blue_pin)
        # self.blue_pulser = Pulsing(blue_pin)


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
        
        red_duty_cycle = int(random.uniform(minBrightnessRed, maxBrightnessRed))
        red_frequency = int(random.uniform(minFreqRed, maxFreqRed))

        green_duty_cycle = int(random.uniform(minBrightnessGreen, maxBrightnessGreen))
        green_frequency = int(random.uniform(minFreqGreen, maxFreqGreen))

        blue_duty_cycle = int(random.uniform(minBrightnessBlue, maxBrightnessBlue))
        blue_frequency = int(random.uniform(minFreqBlue, maxFreqBlue))
        
        # Set dutycycle and frequency per led
        self.red_pin.set_duty_cycle(red_duty_cycle)
        # print("red", self.red_pin.get_duty_cycle())
        self.red_pin.set_frequency(red_frequency)

        self.green_pin.set_duty_cycle(green_duty_cycle)
        # print("green", self.green_pin.get_duty_cycle())
        self.green_pin.set_frequency(green_frequency)

        self.blue_pin.set_duty_cycle(blue_duty_cycle)
        # print("blue", self.blue_pin.get_duty_cycle())
        self.blue_pin.set_frequency(blue_frequency)

        # self.red_fader.fade_in(red_duty_cycle)
        # self.green_fader.fade_in(green_duty_cycle)
        # self.blue_pulser.pulse(blue_duty_cycle)

        # self.red_fader.fade_out(red_duty_cycle)
        # self.green_fader.fade_out(green_duty_cycle)
        

        sleep_time = random.uniform(minSleep, maxSleep)
        time.sleep(sleep_time)


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
        # try:
        self.fireplace_running = True
        while self.fireplace_running:
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
        # except KeyboardInterrupt:
        #     for led in self.leds:
        #         led.pwm.stop()
        #     GPIO.cleanup()

    # def turn_off(self):
    #     # Stop the PWM for each LED color
    #     self.red_pin.turn_off()
    #     self.green_pin.turn_off()
    #     self.blue_pin.turn_off()
    
    def turn_off(self):
        self.fireplace_running = False
        # self.thread.join()  # Wait for the thread to finish
        self.red_pin.turn_off()
        self.green_pin.turn_off()
        self.blue_pin.turn_off()

#################### Old class below ####################

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