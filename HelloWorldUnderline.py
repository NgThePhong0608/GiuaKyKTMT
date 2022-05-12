import time


import Adafruit_Nokia_LCD as LCD
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont


def main():
    SCLK = 23
    Din = 27
    DC = 17
    RST = 15
    CS = 18
    BT1 = 14

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


try:
    main()
except KeyboardInterrupt:
    disp.clear()
