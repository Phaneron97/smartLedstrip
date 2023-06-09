import random
import time
from py_classes.led import LED
from py_classes.fade import Fading
from py_classes.pulse import Pulsing

class Fireplace():
    def __init__(self, red_pin, green_pin, blue_pin):
        self.red_pin = LED(red_pin)
        self.green_pin = LED(green_pin)
        self.blue_pin = LED(blue_pin)
        
        self.fireplace_running = False
        
        self.red_fader = Fading(red_pin)
        self.red_pulser = Pulsing(red_pin)
        
        self.green_fader = Fading(green_pin)
        self.green_pulser = Pulsing(green_pin)
        
        self.blue_fader = Fading(blue_pin)
        self.blue_pulser = Pulsing(blue_pin)
        
    def validate_start_input(self, minBrightnessRed, maxBrightnessRed, minFreqRed, maxFreqRed,
                         minBrightnessGreen, maxBrightnessGreen, minFreqGreen, maxFreqGreen,
                         minBrightnessBlue, maxBrightnessBlue, minFreqBlue, maxFreqBlue,
                         minSleep, maxSleep):
        if not all(isinstance(value, (int, float)) for value in [
            minBrightnessRed, maxBrightnessRed, minFreqRed, maxFreqRed,
            minBrightnessGreen, maxBrightnessGreen, minFreqGreen, maxFreqGreen,
            minBrightnessBlue, maxBrightnessBlue, minFreqBlue, maxFreqBlue,
            minSleep, maxSleep
        ]):
            raise ValueError('Values other than integers and floats detected for input fireplace')  # Invalid datatype (not int or float)

        if not (0 <= minBrightnessRed <= 255) or not (0 <= maxBrightnessRed <= 255) or \
                not (0 <= minBrightnessGreen <= 255) or not (0 <= maxBrightnessGreen <= 255) or \
                not (0 <= minBrightnessBlue <= 255) or not (0 <= maxBrightnessBlue <= 255):
            raise ValueError('Brightness settings out of range (0-255)') # Invalid brightness value (out of range)

        if not (100 <= minFreqRed <= 5000) or not (100 <= maxFreqRed <= 5000) or \
                not (100 <= minFreqGreen <= 5000) or not (100 <= maxFreqGreen <= 5000) or \
                not (100 <= minFreqBlue <= 5000) or not (100 <= maxFreqBlue <= 5000):
            raise ValueError('Frequency settings out of range (100-5000)')  # Invalid frequency value (out of range)

        return True  # All parameters are valid



    def flicker(self, minBrightnessRed, maxBrightnessRed, minFreqRed, maxFreqRed,
                minBrightnessGreen, maxBrightnessGreen, minFreqGreen, maxFreqGreen,
                minBrightnessBlue, maxBrightnessBlue, minFreqBlue, maxFreqBlue,
                minSleep, maxSleep):
        
        # Choose random effects and durations
        # red_effect = random.choice([self.red_fader.fade_in, self.red_fader.fade_out, self.red_pulser.pulse])
        # red_duration = random.uniform(minSleep, maxSleep)
        
        # green_effect = random.choice([self.green_fader.fade_in, self.green_fader.fade_out, self.green_pulser.pulse])
        # green_duration = random.uniform(minSleep, maxSleep)
        
        # blue_effect = random.choice([self.blue_fader.fade_in, self.blue_fader.fade_out, self.blue_pulser.pulse])
        # blue_duration = random.uniform(minSleep, maxSleep)
        
        # Call the randomly chosen effects with the respective durations
        # red_effect(red_duration, self.fireplace_running)
        # green_effect(green_duration, self.fireplace_running)
        # blue_effect(blue_duration, self.fireplace_running)
        
        
        
        sleep_time = random.uniform(minSleep, maxSleep)
        time.sleep(sleep_time)


    def start(self, minBrightnessRed, maxBrightnessRed,minFreqRed,maxFreqRed,
              minBrightnessGreen,maxBrightnessGreen,minFreqGreen,maxFreqGreen,
              minBrightnessBlue,maxBrightnessBlue,minFreqBlue,maxFreqBlue,
              minSleep,maxSleep):
        # try:
        self.fireplace_running = True
        while self.fireplace_running:
            self.flicker(minBrightnessRed, maxBrightnessRed, minFreqRed, maxFreqRed,
                         minBrightnessGreen,maxBrightnessGreen,minFreqGreen,maxFreqGreen,
                         minBrightnessBlue,maxBrightnessBlue,minFreqBlue,maxFreqBlue,
                         minSleep,maxSleep)
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