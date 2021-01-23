import time
from rpi_ws281x import PixelStrip, Color
import argparse



#LED strip configuration
LED_COUNT = 88
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
def green():
    colorWipe(strip, Color(0, 0, 255))
def red():
    colorWipe(strip, Color(255, 0, 0))
def blue():
    colorWipe(strip, Color(0, 255, 0))
def purple():
    colorWipe(strip, Color(128, 128, 0))
def lightgrey():
    colorWipe(strip, Color(255, 203, 192))
def yellow():
    colorWipe(strip, Color(255, 0, 103))
##
def white():
    colorWipe(strip, Color(255, 255, 255))
def turnoff():
    colorWipe(strip, Color(0, 0, 0))
def cyan():
    colorWipe(strip, Color(0, 255, 255))
def navy():
    colorWipe(strip, Color(0, 128, 0))
def salmon():
    colorWipe(strip, Color(255, 150, 165))


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
    print('You can choose the following colors: green, red, blue, purple, light grey, yellow, white, cyan, navy, salmon, or turn off')
    try:
        while True:
            userinput = input('What color would you like: ')
            if userinput == 'blue':
                blue()
            if userinput == 'red':
                red()
            if userinput == 'purple':
                purple()
            if userinput == 'light grey':
                lightgrey()
            if userinput == 'yellow':
                yellow()
            if userinput == 'green':
                green()
            if userinput == 'white':
                white()
            if userinput == 'turn off':
                turnoff()
            if userinput == 'cyan':
                cyan()
            if userinput == 'navy':
                navy()
            if userinput == 'salmon':
                salmon()
            else:
                print = ('Please enter a valid color')
                
    except KeyboardInterrupt:
        if args.clear:
            colorWipe(strip, Color(0,0,0), 10)    
