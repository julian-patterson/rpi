import time
from rpi_ws281x import PixelStrip, Color
import argparse

strip.begin()

#LED strip configuration
LED_COUNT = 80
LED_PIN = 18
LED_FREQ_HZ = 800000
LED_DMA = 10
LED_BRIGHTNESS = 255
LED_INVERT = False
LED_CHANNEL = 0

#Class assignment
def color(red, green, blue, white = 0):
    return (white << 24) | (red << 16) | (green << 8) | blue

def colorWipe(strip, color, wait_ms=50):
    for i in range(strip.numPixels()):
        strip.setPixelColor(i, color)
        strip.show()
        time.sleep(wait_ms / 1000.0)

#Color-variable assignment
def blue():
    colorWipe(strip, Color(0, 255, 0))
def red():
    colorWipe(strip, Color(255, 0, 0))
def purple():
    colorWipe(strip, Color(128, 128, 0))
def pink():
    colorWipe(strip, Color(255, 203, 192))
def yellow():
    colorWipe(strip, Color(255, 0, 255))

#Main Code
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-c','--clear', action='store_true', help= 'clear the display on exit')
    args = parser.parse_args()
    
    strip = PixelStrip(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL)
    strip.begin()
    
    print('Press Ctrl-C to quit.')
    if not args.clear:
        print('Use -c arguement to clear LEDs on exit')
    userinput = input('What color would you like: ')

    try:
        while True:
            if userinput == 'blue':
                yellow()
            if userinput == 'red':
                red()
            if userinput == 'purple':
                purple()
            if userinput == 'pink':
                pink()
            if userinput == 'yellow':
                yellow()
            else:
                print = ('Please enter a valid color')
                userinput = input('What color would you like: ')
    except KeyboardInterrupt:
        if args.clear:
            colorWipe(strip, Color(0,0,0), 10)    