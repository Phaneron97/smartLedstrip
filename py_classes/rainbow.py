import RPi.GPIO as GPIO
import time
import math
import os
from py_classes.led import LED
from py_classes.hsv import HSVtoRGB


###################### using HSV ####################
class Rainbow:
    def __init__(self, red_pin, green_pin, blue_pin):
        self.red_pin = LED(red_pin)
        self.green_pin = LED(green_pin)
        self.blue_pin = LED(blue_pin)
        self.hsv_to_rgb = HSVtoRGB()
        
    def start(self):
        current_hue = 0 # starting hue
        
        # set starting frequency of all leds
        self.red_pin.set_frequency(100)
        self.green_pin.set_frequency(100)
        self.blue_pin.set_frequency(100)
        
        while True:
            for hue in range(361):
                # Convert the current hue value to RGB using the HSVtoRGB converter
                red, green, blue = self.hsv_to_rgb.convert(current_hue)

                # self.pwm_red.set_duty_cycle(red)
                self.red_pin.set_duty_cycle(red)
                self.green_pin.set_duty_cycle(green)
                self.blue_pin.set_duty_cycle(blue)

                # hue resolution of 360
                current_hue = (current_hue + 1) % 360

                # time in seconds to wait between each color change
                # self.set_sleep(0.01)
                time.sleep(0.01)

    def stop(self):
        # Stop the PWM for each LED color
        self.red_pin.turn_off()
        self.green_pin.turn_off()
        self.blue_pin.turn_off()

        # Clean up the GPIO pins
        GPIO.cleanup()




######################## end class ##################

# class Rainbow(LED):
#     def __init__(self, red_pin, green_pin, blue_pin, colors):
#         super().__init__(red_pin)
#         self.green_led = LED(green_pin)
#         self.blue_led = LED(blue_pin)
#         self.colors = colors

#     def start(self, duration=1):
#         start_time = time.time()
#         while True:
#             for i in range(len(self.colors)):
#                 current_color = self.colors[i]
#                 next_color = self.colors[(i+1) % len(self.colors)]
#                 for j in range(100):
#                     t = j/100 # normalize the time from 0 to 1
#                     # Calculate the duty cycle for each LED based on a sinusoidal waveform
#                     red_duty_cycle = ((1 + math.sin(2*math.pi*t + math.pi))*0.5) * current_color[0] + ((1 - math.sin(2*math.pi*t + math.pi))*0.5) * next_color[0]
#                     green_duty_cycle = ((1 + math.sin(2*math.pi*t))*0.5) * current_color[1] + ((1 - math.sin(2*math.pi*t))*0.5) * next_color[1]
#                     blue_duty_cycle = ((1 + math.sin(2*math.pi*t))*0.5) * current_color[2] + ((1 - math.sin(2*math.pi*t))*0.5) * next_color[2]

#                     # Set the duty cycle of each LED
#                     self.set_duty_cycle(red_duty_cycle)
#                     self.green_led.set_duty_cycle(green_duty_cycle)
#                     self.blue_led.set_duty_cycle(blue_duty_cycle)

#                     # Wait a short amount of time to gradually change the duty cycle
#                     time.sleep(0.01)

#                 # Wait a short amount of time between colors
#                 time.sleep(0.1)

#             # Reset the loop and start over from the beginning of the list
#             i = 0


################ new class #######################

# class Rainbow:
#     def __init__(self, red_pin, green_pin, blue_pin, colors, position=0, speed=1):
#         self.leds = [LED(red_pin), LED(green_pin), LED(blue_pin)]
#         self.colors = colors
#         self.position = position
#         self.speed = speed
#         self.brightness_steps = 300  # adjust as needed

#     def start(self):
#         try:
#             while True:
#                 for i in range(len(self.leds)):
#                     color_index = (i + self.position) % len(self.colors)
#                     next_color_index = (i + self.position + 1) % len(self.colors)
#                     color = self.colors[color_index]
#                     next_color = self.colors[next_color_index]
#                     r1, g1, b1 = color
#                     r2, g2, b2 = next_color
#                     brightness = 100.0
#                     transition_time = abs(next_color_index - color_index) / self.speed
#                     brightness_step_size = (brightness / self.brightness_steps)
#                     for j in range(self.brightness_steps):
#                         t = j / float(self.brightness_steps - 1)
#                         r = int(r1 + (r2 - r1) * t)
#                         g = int(g1 + (g2 - g1) * t)
#                         b = int(b1 + (b2 - b1) * t)
#                         brightness_value = brightness * (math.sin(math.pi * t) ** 2)
#                         blend_factor = (math.sin(math.pi * t) ** 2)
#                         self.leds[i].set_duty_cycle((r / 100.0 * brightness_value) + (blend_factor * brightness_step_size))
#                         self.leds[(i + 1) % len(self.leds)].set_duty_cycle((g / 100.0 * brightness_value) + (blend_factor * brightness_step_size))
#                         self.leds[(i + 2) % len(self.leds)].set_duty_cycle((b / 100.0 * brightness_value) + (blend_factor * brightness_step_size))
#                         self.leds[i].set_frequency(50)
#                         self.leds[(i + 1) % len(self.leds)].set_frequency(50)
#                         self.leds[(i + 2) % len(self.leds)].set_frequency(50)
#                         self.leds[i].set_sleep(transition_time / self.brightness_steps)
#                         brightness -= brightness_step_size
#                         if brightness < 0:
#                             brightness = 0
#         except KeyboardInterrupt:
#             for led in self.leds:
#                 led.pwm.stop()
#             GPIO.cleanup()

################# new class ########################

# class Rainbow:
#     def __init__(self, red_pin, green_pin, blue_pin, colors, position=0, speed=1):
#         self.leds = [LED(red_pin), LED(green_pin), LED(blue_pin)]
#         self.colors = colors
#         self.position = position
#         self.speed = speed
#         self.brightness_steps = 10  # adjust as needed

#     def start(self):
#         try:
#             while True:
#                 for i in range(len(self.leds)):
#                     color_index = (i + self.position) % len(self.colors)
#                     next_color_index = (i + self.position + 1) % len(self.colors)
#                     color = self.colors[color_index]
#                     next_color = self.colors[next_color_index]
#                     r1, g1, b1 = color
#                     r2, g2, b2 = next_color
#                     brightness = 100.0
#                     transition_time = abs(next_color_index - color_index) / self.speed
#                     brightness_step_size = (brightness / self.brightness_steps)
#                     start_time = time.time()
#                     while True:
#                         elapsed_time = time.time() - start_time
#                         if elapsed_time >= transition_time:
#                             break
#                         t = elapsed_time / transition_time
#                         r = int(r1 + (r2 - r1) * t)
#                         g = int(g1 + (g2 - g1) * t)
#                         b = int(b1 + (b2 - b1) * t)
#                         brightness_value = brightness * (math.sin(math.pi * t) ** 2)
#                         blend_factor = (math.sin(math.pi * t) + 1) / 2
#                         r_duty_cycle = (r / 100.0 * brightness_value) + (blend_factor * brightness_step_size)
#                         g_duty_cycle = (g / 100.0 * brightness_value) + (blend_factor * brightness_step_size)
#                         b_duty_cycle = (b / 100.0 * brightness_value) + (blend_factor * brightness_step_size)
#                         self.leds[i].set_duty_cycle(r_duty_cycle)
#                         self.leds[(i + 1) % len(self.leds)].set_duty_cycle(g_duty_cycle)
#                         self.leds[(i + 2) % len(self.leds)].set_duty_cycle(b_duty_cycle)
#         except KeyboardInterrupt:
#             for led in self.leds:
#                 led.pwm.stop()
#             GPIO.cleanup()


############### class with functions #######################

# class Rainbow:
#     def __init__(self, red_pin, green_pin, blue_pin, colors, position=0, speed=0.5):
#         # initialize LED objects and set instance variables
#         self.leds = [LED(red_pin), LED(green_pin), LED(blue_pin)]
#         self.colors = colors
#         self.position = position
#         self.speed = speed
#         self.brightness_steps = 50  # adjust as needed

#     def start(self):
#         try:
#             while True:
#                 for i in range(len(self.leds)):
#                     # get current and next colors
#                     color_index = (i + self.position) % len(self.colors)
#                     next_color_index = (i + self.position + 1) % len(self.colors)
#                     color = self.colors[color_index]
#                     next_color = self.colors[next_color_index]

#                     # get color transition time and brightness step size
#                     r1, g1, b1 = color
#                     r2, g2, b2 = next_color
#                     brightness = 100.0
#                     transition_time = abs(next_color_index - color_index) / self.speed
#                     brightness_step_size = (brightness / self.brightness_steps)

#                     # start color transition loop
#                     start_time = time.time()
#                     while True:
#                         elapsed_time = time.time() - start_time
#                         if elapsed_time >= transition_time:
#                             break

#                         # calculate duty cycles for each color and set LED brightness
#                         t = elapsed_time / transition_time
#                         r = int(r1 + (r2 - r1) * t)
#                         g = int(g1 + (g2 - g1) * t)
#                         b = int(b1 + (b2 - b1) * t)
#                         brightness_value = brightness * (math.sin(math.pi * t) ** 2)
#                         blend_factor = (math.sin(math.pi * t) + 1) / 2
#                         r_duty_cycle, g_duty_cycle, b_duty_cycle = self.get_duty_cycles(r, g, b, brightness_value, blend_factor, brightness_step_size)
#                         self.set_led_brightness(i, r_duty_cycle, g_duty_cycle, b_duty_cycle)

#         except KeyboardInterrupt:
#             # clean up GPIO pins and PWM
#             for led in self.leds:
#                 led.pwm.stop()
#             GPIO.cleanup()

#     def get_duty_cycles(self, r, g, b, brightness_value, blend_factor, brightness_step_size):
#         # calculate duty cycle for each color based on brightness and blend factor
#         r_duty_cycle = (r / 100.0 * brightness_value) + (blend_factor * brightness_step_size)
#         g_duty_cycle = (g / 100.0 * brightness_value) + (blend_factor * brightness_step_size)
#         b_duty_cycle = (b / 100.0 * brightness_value) + (blend_factor * brightness_step_size)
#         return r_duty_cycle, g_duty_cycle, b_duty_cycle

#     def set_led_brightness(self, i, r_duty_cycle, g_duty_cycle, b_duty_cycle):
#         # set duty cycle for each color on corresponding LED
#         self.leds[i].set_duty_cycle(r_duty_cycle)
#         self.leds[(i + 1) % len(self.leds)].set_duty_cycle(g_duty_cycle)
#         self.leds[(i + 2) % len(self.leds)].set_duty_cycle(b_duty_cycle)