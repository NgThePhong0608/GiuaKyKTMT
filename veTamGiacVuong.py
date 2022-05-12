import time
import Adafruit_Nokia_LCD as LCD
# khai bao thu vien pillow de tao va ve hinh
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont


def main():
    SCLK = 23
    DIN = 27
    DC = 17
    RST = 15
    CS = 18
    global disp
    disp = LCD.PCD8544(DC, RST, SCLK, DIN, CS)
    disp.begin(contrast=60)
    disp.clear()
    disp.display()
    image = Image.new('1', (LCD.LCDWIDTH, LCD.LCDHEIGHT))
    draw = ImageDraw.Draw(image)
    draw.polygon([(27, 38), (57, 38), (27, 10)], outline=0, fill=255)
    disp.image(image)
    disp.display()
    while True:
        time.sleep(2)


try:
    main()
except KeyboardInterrupt:
    disp.clear()
