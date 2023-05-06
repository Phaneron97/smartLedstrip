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
    def convert(self, hue, saturation=1.0, value=1.0):
        # Convert HSV to RGB using the algorithm described here:
        # https://en.wikipedia.org/wiki/HSL_and_HSV#From_HSV
        c = value * saturation
        x = c * (1 - abs(((hue/60) % 2) - 1))
        m = value - c

        if 0 <= hue < 60:
            red, green, blue = c, x, 0
        elif 60 <= hue < 120:
            red, green, blue = x, c, 0
        elif 120 <= hue < 180:
            red, green, blue = 0, c, x
        elif 180 <= hue < 240:
            red, green, blue = 0, x, c
        elif 240 <= hue < 300:
            red, green, blue = x, 0, c
        elif 300 <= hue < 360:
            red, green, blue = c, 0, x
        else:
            red, green, blue = 0, 0, 0

        # Scale the RGB values from the range [0, 1] to [0, 100]
        red = int((red + m) * 100)
        green = int((green + m) * 100)
        blue = int((blue + m) * 100)

        return (red, green, blue)