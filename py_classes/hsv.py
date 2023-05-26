# class HSVtoRGB:
#     def convert(self, hue, saturation=1.0, value=1.0):
#         c = value * saturation
#         x = c * (1 - abs(((hue/60) % 2) - 1))
#         m = value - c

#         if 0 <= hue < 60:
#             red, green, blue = c, x, 0
#         elif 60 <= hue < 120:
#             red, green, blue = x, c, 0
#         elif 120 <= hue < 180:
#             red, green, blue = 0, c, x
#         elif 180 <= hue < 240:
#             red, green, blue = 0, x, c
#         elif 240 <= hue < 300:
#             red, green, blue = x, 0, c
#         elif 300 <= hue < 360:
#             red, green, blue = c, 0, x
#         else:
#             red, green, blue = 0, 0, 0

#         # Scale the RGB values from the range [0, 1] to [0, 255]
#         red = int((red + m) * 100)
#         green = int((green + m) * 100)
#         blue = int((blue + m) * 100)

#         return (red, green, blue)

class HSVtoRGB:
    
    # def convert_range(self, value, convert_to=255):
    #     converted_value = round(value * 100 / convert_to)
    #     if converted_value <= 50:
    #         return 0
    #     return converted_value
    
    def validate_hsv(self, hue, saturation, value):
        # Validate input types
        if not isinstance(hue, int):
            raise ValueError("Invalid float for 'hue'")
        if not isinstance(saturation, float):
            raise ValueError("Invalid float for 'saturation'")
        if not isinstance(value, float):
            raise ValueError("Invalid float for 'value'")

        # Validate input value ranges
        if not (0 <= hue <= 360):
            raise ValueError("'hue' must be between 0 and 255.")
        if not (0.0 <= saturation <= 1.0):
            raise ValueError("'saturation' be between 0.0 and 1.0.")
        if not (0.0 <= value <= 1.0):
            raise ValueError("'value' be between 0.0 and 1.0.")
    
    
    def convert(self, hue, saturation=1.0, value=1.0):
        self.validate_hsv(hue, saturation, value)
        
        chroma = saturation * value # calc chroma
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
        
        # Get value between 0-255 for dutycycle
        r = (red + m) * 255
        g = (green + m) * 255
        b = (blue + m) * 255
        
        # print (int(r), int(g), int(b))
        return (r, g, b)
            

# hsv_to_rgb = HSVtoRGB()

# for i in range(360):    
#     print(hsv_to_rgb.convert(i, 1, 1))