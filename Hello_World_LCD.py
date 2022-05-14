import RPi.GPIO as GPIO
import time
import Adafruit_Nokia_LCD as LCD

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

# chuong trinh bam bt1 hien thi helloworld ra terminal, va man hinh glcd


def main():
    BT1 = 14
    SCLK = 23
    DIN = 27
    DC = 17
    RST = 15
    CS = 18
    global disp
    disp = LCD.PCD8544(DC, RST, SCLK, DIN, CS)  # khoi tao lcd
    disp.begin(contrast=60)
    disp.clear()  # xoa man hinh
    disp.display()
    GPIO.setmode(GPIO.BCM)  # setup mode

    string = "hello world"
    # cai dat cac nut
    GPIO.setup(BT1, GPIO.IN, pull_up_down=GPIO.PUD_UP)

    while True:
        if GPIO.input(BT1) == GPIO.LOW:
            image = Image.new('1', (LCD.LCDWIDTH, LCD.LCDHEIGHT))
            draw = ImageDraw.Draw(image)
            draw.rectangle(
                (0, 0, LCD.LCDWIDTH-1, LCD.LCDHEIGHT-1), outline=0, fill=255)
            # load font chu
            font = ImageFont.load_default()
            # hien thi dong chu ra man hinh
            draw.text((8, 30), string, font=font)
            # hien thi hinh anh
            disp.image(image)
            print(string)
            disp.display()
            time.sleep(0.5)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        disp.clear()
        disp.display()
