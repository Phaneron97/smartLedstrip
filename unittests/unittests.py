import unittest
from unittest.mock import MagicMock
import sys
sys.path.append('../')

from py_classes.hsv import HSVtoRGB
from py_classes.rainbow import Rainbow
from py_classes.led import LED


# Test HSV conversion
class TestHSVConversion(unittest.TestCase):
    def setUp(self):
        self.converter = HSVtoRGB()

    def test_convert(self): # Test with valid HSV values
        expected_rgb = (255, 0, 0)  # Expected RGB value for hue = 0
        self.assertEqual(self.converter.convert(0), expected_rgb)

        expected_rgb = (0, 255, 0)  # Expected RGB value for hue = 120
        self.assertEqual(self.converter.convert(120), expected_rgb)

        expected_rgb = (0, 0, 255)  # Expected RGB value for hue = 240
        self.assertEqual(self.converter.convert(240), expected_rgb)

    def test_invalid_hsv_values(self): # Test with invalid HSV values
        with self.assertRaises(ValueError):
            self.converter.convert(400) # Should raise ValueError for hue outside the range

        with self.assertRaises(ValueError):
            self.converter.convert(180, saturation=1.5) # Should raise ValueError for saturation outside the range

        with self.assertRaises(ValueError):
            self.converter.convert(180, value=1.5) # Should raise ValueError for value outside the range

    def test_default_saturation_and_value(self): # Test with default saturation and value        
        expected_rgb = (255, 0, 0)  # Expected RGB value with hue = 0, saturation = 1.0, value = 1.0
        self.assertEqual(self.converter.convert(0), expected_rgb)

    def test_negative_hue(self): # Test with negative hue        
        expected_rgb = (0, 0, 255) # Expected RGB value for hue = -120 (equivalent to 240)
        self.assertEqual(self.converter.convert(-120), expected_rgb)

    def test_hue_overflow(self): # Test hue overflow        
        expected_rgb = (0, 0, 255) # Expected RGB value for hue = 420 (equivalent to 60)
        self.assertEqual(self.converter.convert(420), expected_rgb)
        

# test Rainbow()
class TestRainbow(unittest.TestCase):
    def setUp(self):
        self.red_pin = MagicMock() # create mock object to simulate real Led object
        self.green_pin = MagicMock()
        self.blue_pin = MagicMock()
        self.rainbow = Rainbow(self.red_pin, self.green_pin, self.blue_pin)

    def test_start(self):
        self.rainbow.start()
        self.assertTrue(self.rainbow.rainbow_running)
        # Add assertions for LED pin behavior within the rainbow loop

    def test_turn_off(self):
        self.rainbow.turn_off()
        self.assertFalse(self.rainbow.rainbow_running)
        self.red_pin.turn_off.assert_called_once()
        self.green_pin.turn_off.assert_called_once()
        self.blue_pin.turn_off.assert_called_once()
        

# Test hex_to_rgb()
class HexToRgbTest(unittest.TestCase):

    def test_valid_hex_code(self):
        # Test a valid hex code
        hex_code = "#FF0000"
        expected_result = (255, 0, 0)
        result = hex_to_rgb(hex_code)
        self.assertEqual(result, expected_result)

    def test_invalid_hex_code_starting_without_hash(self):
        # Test an invalid hex code without '#' symbol at the beginning
        hex_code = "FF0000"
        with self.assertRaises(ValueError):
            hex_to_rgb(hex_code)

    def test_invalid_hex_code_with_incorrect_length(self):
        # Test an invalid hex code with incorrect length
        hex_code = "#FFFFF"
        with self.assertRaises(ValueError):
            hex_to_rgb(hex_code)   

if __name__ == '__main__':
    unittest.main()
