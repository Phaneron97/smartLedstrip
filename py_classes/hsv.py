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
    # def convert(self, hue, saturation=1.0, value=1.0):
    #     # https://en.wikipedia.org/wiki/HSL_and_HSV#From_HSV
    #     # c = value * saturation
    #     # x = c * (1 - abs(((hue/60) % 2) - 1))
    #     # m = value - c

    #     # if 0 <= hue < 60:
    #     #     red, green, blue = c, x, 0
    #     # elif 60 <= hue < 120:
    #     #     red, green, blue = x, c, 0
    #     # elif 120 <= hue < 180:
    #     #     red, green, blue = 0, c, x
    #     # elif 180 <= hue < 240:
    #     #     red, green, blue = 0, x, c
    #     # elif 240 <= hue < 300:
    #     #     red, green, blue = x, 0, c
    #     # elif 300 <= hue < 360:
    #     #     red, green, blue = c, 0, x
    #     # # else:
    #     # #     red, green, blue = 0, 0, 0
        
    #     hue /= 60
    #     chroma = value * saturation
    #     x = chroma * (1 - abs(hue % 2 - 1))
    #     r, g, b = 0.0, 0.0, 0.0

    #     if 0 <= hue < 1:
    #         r, g, b = chroma, x, 0.0
    #         # print("R", chroma)
    #     elif 1 <= hue < 2:
    #         r, g, b = x, chroma, 0.0
    #         # print("G", chroma)
    #     elif 2 <= hue < 3:
    #         r, g, b = 0.0, chroma, x
    #         # print("G", chroma)
    #     elif 3 <= hue < 4:
    #         r, g, b = 0.0, x, chroma
    #         # print("B", chroma)
    #     elif 4 <= hue < 5:
    #         r, g, b = x, 0.0, chroma
    #         # print("B", chroma)
    #     elif 5 <= hue < 6:
    #         r, g, b = chroma, 0.0, x
    #         # print("R", chroma)

    #     # Scale the RGB values from the range [0, 1] to [0, 100]
    #     # red = int((red + m) * 100)
    #     # green = int((green + m) * 100)
    #     # blue = int((blue + m) * 100)
        
    #     m = value - chroma
    #     r, g, b = round((r + m) * 255, 2), round((g + m) * 255, 2), round((b + m) * 255, 2)

    #     return (r, g, b)
    
    # def convert_range(self, value, convert_to=255):
    #     converted_value = round(value * 100 / convert_to)
    #     if converted_value <= 50:
    #         return 0
    #     return converted_value
    
    
    def convert(self, hue, saturation=1.0, value=1.0):
        chroma = saturation * value # calc chroma
        x = chroma * (1- abs((hue/60) % 2 - 1)) 
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
        
        # print("r", r)
        # print("g", g)
        # print("b", b)
        return (r, g, b)
            

# hsv_to_rgb = HSVtoRGB()

# for i in range(360):    
#     print(hsv_to_rgb.convert(i, 1, 1))