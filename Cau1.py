import RPi.GPIO as GPIO
import time
import os


def main():
    LED = 22
    BT1 = 14
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(BT1, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(LED, GPIO.OUT)
    ispressBT1 = True
    while True:
        if ispressBT1:
            if GPIO.input(LED) == GPIO.LOW:
                GPIO.output(LED, GPIO.HIGH)
                time.sleep(1)
            if GPIO.input(LED) == GPIO.HIGH:
                GPIO.output(LED, GPIO.LOW)
                time.sleep(1)
        if GPIO.input(BT1) == GPIO.LOW:
            print('BT1 is pressed')
            ispressBT1 = False
            GPIO.output(LED, GPIO.HIGH)
            time.sleep(0.5)


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        GPIO.cleanup()
