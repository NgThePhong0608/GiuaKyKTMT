import time
import Adafruit_Nokia_LCD as LCD
# Khai báo thư viện pillow để tạo và vẽ hình
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont


def main():
    # Khai báo các pin GPIO
    SCLK = 23
    DIN = 27
    DC = 17
    RST = 15
    CS = 18
    global disp  # khởi tạo biến global
    disp = LCD.PCD8544(DC, RST, SCLK, DIN, CS)  # Khởi tạo LCD
    disp.begin(contrast=60)
    # cài đặt độ sáng
    # # xóa màn hình.
    disp.clear()
    disp.display()  # tạo ảnh 1 bit color, với chiều rộng, cao bằng của LCD
    image = Image.new('1', (LCD.LCDWIDTH, LCD. LCDHEIGHT))
    # chọn đối tượng để vẽ.
    draw = ImageDraw.Draw(image)
    # và các hình khác
    draw.rectangle((27, 9, 57, 39), outline=0, fill=255)
    disp.image(image)
    disp.display()
    while True:
        time.sleep(2)


try:
    main()
except KeyboardInterrupt:  # xử lí sự kiện Ctrl+c
    disp.clear()
