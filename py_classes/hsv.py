class HSVtoRGB:    
    def validate_hsv(self, hue, saturation, value): # Validate input from rainbow loop
        # Validate input datatypes
        if not isinstance(hue, int):
            raise ValueError("Invalid float for 'hue'")
        if not isinstance(saturation, (float, int)):
            raise ValueError("Invalid float for 'saturation'")
        if not isinstance(value, (float, int)):
            raise ValueError("Invalid float for 'value'")

        # Validate input value ranges
        if not (0 <= hue <= 360):
            raise ValueError("'hue' must be between 0 and 255.")
        if not (0.0 <= saturation <= 1.0):
            raise ValueError("'saturation' be between 0.0 and 1.0.")
        if not (0.0 <= value <= 1.0):
            raise ValueError("'value' be between 0.0 and 1.0.")
        if not isinstance(hue, int):
            raise ValueError("'hue' must be an integer.")
    
    def convert(self, hue, saturation=1.0, value=1.0):
        self.validate_hsv(hue, saturation, value)
        
        # HSV -> RGB conversion algorithm found on internet
        chroma = saturation * value 
        x = chroma * (1 - abs((hue / 60) % 2 - 1)) 
        m = value - chroma
        
        # Hue degrees determines which color is turned on
        if 0 <= hue < 60:
            red, green, blue = chroma, x, 0
        elif 60 <= hue < 120:
            red, green, blue = x, chroma, 0
        elif 120 <= hue < 180:
            red, green, blue = 0, chroma, x
        elif 180 <= hue < 240:
            red, green, blue = 0, x, chroma
        elif 240 <= hue < 300:
            red, green, blue = x, 0, chroma
        elif 300 <= hue < 360:
            red, green, blue = chroma, 0, x
        else:
            raise ValueError("hue outside possible range")
        
        # Get value between 0-255 for dutycycle
        r = (red + m) * 255
        g = (green + m) * 255
        b = (blue + m) * 255
        
        # print (int(r), int(g), int(b))
        return (int(r), int(g), int(b)) # Return final RGB values as tuple