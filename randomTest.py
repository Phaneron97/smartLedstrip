import random

minBrightnessRed = 40
maxBrightnessRed = 100

for i in range(100):
    red_duty_cycle = random.uniform(random.uniform(minBrightnessRed-5, minBrightnessRed+5), random.uniform(maxBrightnessRed-5, maxBrightnessRed))
    print(red_duty_cycle)