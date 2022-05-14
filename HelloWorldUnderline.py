import time

import RPi.GPIO as GPIO
import Adafruit_Nokia_LCD as LCD
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont


def main():
    BT1 = 14
    SCLK = 23
    Din = 27
    DC = 17
    RST = 15
    CS = 18
    BT1 = 14
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(BT1, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    global disp
    disp = LCD.PCD8544(DC, RST, SCLK, Din, CS)
    disp.begin(contrast=60)
    disp.clear()
    disp.display()
    image = Image.new('1', (LCD.LCDWIDTH, LCD.LCDHEIGHT))
    draw = ImageDraw.Draw(image)
    draw.rectangle((0, 0, LCD.LCDWIDTH, LCD.LCDHEIGHT), outline=255, fill=255)
    draw.line((8, 30, 68, 30), fill=0)

    font = ImageFont.load_default()
    draw.text((6, 20), 'Hello Wolrd', font=font)
    disp.image(image)
    disp.display()

    while True:
        if GPIO.input(BT1) == GPIO.LOW:
            print('BT1 is pressed')
            disp.clear()
            disp1 = LCD.PCD8544(DC, RST, SCLK, Din, CS)
            image1 = Image.new('1', (LCD.LCDWIDTH, LCD.LCDHEIGHT))
            draw1 = ImageDraw.Draw(image1)
            draw1.rectangle((0, 0, LCD.LCDWIDTH, LCD.LCDHEIGHT),
                            outline=255, fill=255)
            draw1.line((8, 30, 68, 30), fill=0)

            disp1.image(image1)
            disp1.display()


try:
    main()
except KeyboardInterrupt:
    # disp.clear()
    pass
