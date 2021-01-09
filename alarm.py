import schedule
import subprocess
import time
import argparse
from rpi_ws281x import PixelStrip, Color

#Variable configuration
LED_COUNT = 70
LED_PIN = 18
LED_FREQ_HZ = 800000
LED_DMA = 10
LED_BRIGHTNESS = 255
LED_INVERT = False
LED_CHANNEL = 0
userinput1 = str(input('What hour would you like to wake up Mr. Patterson? '))
userinput2= str(input('What minute would you like to wake up Mr. Patterson? '))
waketime = (str(userinput1) + ":" + str(userinput2))

print(waketime)

#function defintions
def lights():
	if __name__ == '__main__':
		parser = argparse.ArgumentParser()
		parser.add_argument('-c','--clear', action='store_true', help= 'clear the display on exit')
		args = parser.parse_args()
    
		strip = PixelStrip(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL)
		strip.begin()
    
		print('Press Ctrl-C to quit.')
		if not args.clear:
			print('Use -c arguement to clear LEDs on exit')
        
		try:
        
			while True:
				colorWipe(strip, Color(248, 0, 100))
		except KeyboardInterrupt:
			if args.clear:
				colorWipe(strip, Color(0,0,0), 10)

def color(red, green, blue, white = 0):
    return (white << 24) | (red << 16) | (green << 8) | blue
def colorWipe(strip, color, wait_ms=50):
    for i in range(strip.numPixels()):
        strip.setPixelColor(i, color)
        strip.show()
	
schedule.every().day.at(waketime).do(lights)

while True:
	schedule.run_pending()
	time.sleep(1)
