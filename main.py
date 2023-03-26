from py_classes.fireplace import Fireplace
from py_classes.rainbow import Rainbow

# Define the PWM pins for the red, green, and blue LEDs
red_pin = 12
green_pin = 13
blue_pin = 18
pins = [12, 13, 18]

############# Fireplace ###################

# # Create a Fireplace object with the three PWM pins
# fireplace = Fireplace(red_pin, green_pin, blue_pin)

# # Start the fireplace effect
# fireplace.start()


################ Rainbow ###################

colors = [
    (100, 0, 100),  # Violet
    (50, 0, 50),  # Indigo
    (0, 0, 100),  # Blue
    (0, 100, 0),  # Green
    (100, 100, 0),  # Yellow
    (100, 50, 0),  # Orange
    (100, 0, 0)  # Red
]

# In between colors

# (75, 0, 75),
# (25, 0, 75),
# (0, 50, 50),
# (50, 100, 0),
# (100, 75, 0),
# (100, 25, 0),    

rainbow = Rainbow(red_pin, green_pin, blue_pin, colors)

rainbow.start()