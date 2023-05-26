import argparse
import time

from rpi_ws281x import Color, PixelStrip

LED_COUNT = 100
LED_PIN = 18
LED_FREQ_HZ = 800000
LED_DMA = 10
LED_BRIGHTNESS = 255
LED_INVERT = False
LED_CHANNEL = 0


def color(red, green, blue, white=0):
    return (white << 24) | (red << 16) | (green << 8) | blue


def colorWipe(strip, color):
    for i in range(strip.numPixels()):
        strip.setPixelColor(i, color)
        strip.show()


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-c', '--clear', action='store_true',
                        help='clear the display on exit')
    args = parser.parse_args()

    strip = PixelStrip(
        LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL)
    strip.begin()

    print('Press Ctrl-C to quit.')
    if not args.clear:
        print('Use -c arguement to clear LEDs on exit')

    try:
        while True:
            pixels = strip.numPixels()
            colorWipe(strip, Color(255, 0, 0))
            red = 255
            blue = 0
            for green in range(0, 256, 5):
                colorWipe(strip, Color(red, green, blue))

            for red in range(255, 0, -5):
                colorWipe(strip, Color(red, green, blue))

            for blue in range(0, 256, 5):
                colorWipe(strip, Color(red, green, blue))

            for green in range(255, 0, -5):
                colorWipe(strip, Color(red, green, blue))

            for red in range(0, 256, 5):
                colorWipe(strip, Color(red, green, blue))

            for blue in range(255, 0, -5):
                colorWipe(strip, Color(red, green, blue))

    except KeyboardInterrupt:
        if args.clear:
            strip.setPixelColorRGB(pixels, 0, 0, 0)
