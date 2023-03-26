import RPi.GPIO as GPIO
import time
import math
from py_classes.led import LED

# class Rainbow:
#     def __init__(self, red_pin, green_pin, blue_pin, colors, delay):
#         self.leds = [LED(red_pin), LED(green_pin), LED(blue_pin)]
#         self.colors = colors
#         self.delay = delay
#         self.color_index = 0
#         self.current_color = [0, 0, 0]
#         self.next_color = self.colors[self.color_index]

    # def __init__(self, red_pin, green_pin, blue_pin, colors):
    #     self.leds = [LED(red_pin), LED(green_pin), LED(blue_pin)]
    #     self.colors = colors

    # def start(self, duration=10):
    #     try:
    #         start_time = time.time()
    #         while True:
    #             # Loop through each color in the list
    #             for i in range(len(self.colors)):
    #                 # Get the next color in the list
    #                 color = self.colors[i]

    #                 # Gradually change the duty cycle of each LED over time to smoothly transition between colors
    #                 for j in range(100):
    #                     # Calculate the duty cycle for each LED based on the current color's RGB values
    #                     red_duty_cycle = color[0] * (j / 100)
    #                     green_duty_cycle = color[1] * (j / 100)
    #                     blue_duty_cycle = color[2] * (j / 100)

    #                     # Set the duty cycle of each LED
    #                     self.leds[0].set_duty_cycle(red_duty_cycle)
    #                     self.leds[1].set_duty_cycle(green_duty_cycle)
    #                     self.leds[2].set_duty_cycle(blue_duty_cycle)

    #                     # Wait a short amount of time to gradually change the duty cycle
    #                     time.sleep(duration / 100)

    #                 # Wait a longer amount of time between colors
    #                 time.sleep(duration)

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
#         self.brightness_steps = 5  # adjust as needed

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

class Rainbow:
    def __init__(self, red_pin, green_pin, blue_pin, colors, position=0, speed=0.5):
        # initialize LED objects and set instance variables
        self.leds = [LED(red_pin), LED(green_pin), LED(blue_pin)]
        self.colors = colors
        self.position = position
        self.speed = speed
        self.brightness_steps = 5  # adjust as needed

    def start(self):
        try:
            while True:
                for i in range(len(self.leds)):
                    # get current and next colors
                    color_index = (i + self.position) % len(self.colors)
                    next_color_index = (i + self.position + 1) % len(self.colors)
                    color = self.colors[color_index]
                    next_color = self.colors[next_color_index]

                    # get color transition time and brightness step size
                    r1, g1, b1 = color
                    r2, g2, b2 = next_color
                    brightness = 100.0
                    transition_time = abs(next_color_index - color_index) / self.speed
                    brightness_step_size = (brightness / self.brightness_steps)

                    # start color transition loop
                    start_time = time.time()
                    while True:
                        elapsed_time = time.time() - start_time
                        if elapsed_time >= transition_time:
                            break

                        # calculate duty cycles for each color and set LED brightness
                        t = elapsed_time / transition_time
                        r = int(r1 + (r2 - r1) * t)
                        g = int(g1 + (g2 - g1) * t)
                        b = int(b1 + (b2 - b1) * t)
                        brightness_value = brightness * (math.sin(math.pi * t) ** 2)
                        blend_factor = (math.sin(math.pi * t) + 1) / 2
                        r_duty_cycle, g_duty_cycle, b_duty_cycle = self.get_duty_cycles(r, g, b, brightness_value, blend_factor, brightness_step_size)
                        self.set_led_brightness(i, r_duty_cycle, g_duty_cycle, b_duty_cycle)

        except KeyboardInterrupt:
            # clean up GPIO pins and PWM
            for led in self.leds:
                led.pwm.stop()
            GPIO.cleanup()

    def get_duty_cycles(self, r, g, b, brightness_value, blend_factor, brightness_step_size):
        # calculate duty cycle for each color based on brightness and blend factor
        r_duty_cycle = (r / 100.0 * brightness_value) + (blend_factor * brightness_step_size)
        g_duty_cycle = (g / 100.0 * brightness_value) + (blend_factor * brightness_step_size)
        b_duty_cycle = (b / 100.0 * brightness_value) + (blend_factor * brightness_step_size)
        return r_duty_cycle, g_duty_cycle, b_duty_cycle

    def set_led_brightness(self, i, r_duty_cycle, g_duty_cycle, b_duty_cycle):
        # set duty cycle for each color on corresponding LED
        self.leds[i].set_duty_cycle(r_duty_cycle)
        self.leds[(i + 1) % len(self.leds)].set_duty_cycle(g_duty_cycle)
        self.leds[(i + 2) % len(self.leds)].set_duty_cycle(b_duty_cycle)