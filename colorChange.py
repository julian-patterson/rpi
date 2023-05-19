import argparse
import time

import rpi_ws281x

LED_COUNT = 100
LED_PIN = 18
LED_FREQ_HZ = 800000
LED_DMA = 10
LED_BRIGHTNESS = 255
LED_INVERT = False
LED_CHANNEL = 0

strip = rpi_ws281x.Adafruit_NeoPixel(
    LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_BRIGHTNESS, LED_INVERT, LED_CHANNEL)

pixels = strip.numPixels()


def color_change():
    while True:
        for red in range(0, 256):
            strip.setPixelColorRGB(pixels, red, green, blue)
            strip.show()
            time.sleep(0.5)

        for green in range(0, 256):
            strip.setPixelColorRGB(pixels, red, green, blue)
            strip.show()
            time.sleep(0.5)

        for red in range(255, 0, -1):
            strip.setPixelColorRGB(pixels, red, green, blue)
            strip.show()
            time.sleep(0.5)

        for blue in range(0, 256):
            strip.setPixelColorRGB(pixels, red, green, blue)
            strip.show()
            time.sleep(0.5)

        for green in range(255, 0, -1):
            strip.setPixelColorRGB(pixels, red, green, blue)
            strip.show()
            time.sleep(0.5)

        for red in range(0, 256):
            strip.setPixelColorRGB(pixels, red, green, blue)
            strip.show()
            time.sleep(0.5)

        for blue in range(255, 0, -1):
            strip.setPixelColorRGB(pixels, red, green, blue)
            strip.show()
            time.sleep(0.5)


def lights():
    if __name__ == '__main__':
        parser = argparse.ArgumentParser()
        parser.add_argument('-c', '--clear', action='store_true',
                            help='clear the display on exit')
        args = parser.parse_args()

        strip = rpi_ws281x.Adafruit_NeoPixel(
            LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL)
        strip.begin()

        print('Press Ctrl-C to quit.')
        if not args.clear:
            print('Use -c arguement to clear LEDs on exit')

        try:
            while True:
                color_change()

        except KeyboardInterrupt:
            if args.clear:
                strip.setPixelColorRGB(pixels, 0, 0, 0)


def color(red, green, blue, white=0):
    return (white << 24) | (red << 16) | (green << 8) | blue
