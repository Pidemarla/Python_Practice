from PIL import Image
import pyautogui
import time
import winsound

def is_color(pixel, target_color):
    r, g, b = target_color
    return pixel[0] == r and pixel[1] == g and pixel[2] == b

target_color = (1, 117, 79)  # RGB for #01754F

while True:
    screenshot = pyautogui.screenshot()
    pixels = list(screenshot.getdata())
    if any(is_color(pixel, target_color) for pixel in pixels):
        winsound.Beep(1000, 500)  # Beep if the color is found
    time.sleep(1)
