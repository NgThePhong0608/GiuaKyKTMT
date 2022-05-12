import time
import RPi.GPIO as GPIO
import Adafruit_Nokia_LCD as LCD
from PIL import Image, ImageDraw, ImageFont


def main():

    TRIG = 16
    ECHO = 26
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
    global pulse_end

    while True:
        print("Waiting For Sensor To Settle")

        GPIO.output(GREEN, GPIO.HIGH)

        time.sleep(2)

        while GPIO.input(ECHO) == 0:
            pulse_start = time.time()
        while GPIO.input(ECHO) == 1:
            pulse_end = time.time()

        pulse_duration = pulse_end - pulse_start
        distance = pulse_duration*17150
        distance = round(distance, 2)
        string = str(distance) + " cm"
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
        print(chuoi)
        disp.display()
        time.sleep(0.5)


try:
    main()

except KeyboardInterrupt:
    GPIO.cleanup()
