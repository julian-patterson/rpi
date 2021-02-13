from flask import Flask, render_template, redirect, request
from rpi_ws281x import PixelStrip, Color
import datetime
import time

#LED strip configuration/variable configuration
LED_COUNT = 88
LED_PIN = 18
LED_FREQ_HZ = 800000
LED_DMA = 10
LED_BRIGHTNESS = 255
LED_INVERT = False
LED_CHANNEL = 0
app = Flask(__name__)

def color(red, green, blue, white = 0):
    return (white << 24) | (red << 16) | (green << 8) | blue

def colorWipe(strip, color):
    for i in range(strip.numPixels()):
        strip.setPixelColor(i, color)
        strip.show()

@app.route('/<deviceName>')
def action(deviceName):
	strip = PixelStrip(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL)
	strip.begin()
	if deviceName == 'white':
		colorWipe(strip, color(255, 255, 255))
		return redirect('/', code=302)
	if deviceName == 'off':
		colorWipe(strip, color(0, 0, 0))
		return redirect('/', code=302)
	if deviceName == 'red':
		colorWipe(strip, color(255, 0, 0))
		return redirect('/', code=302)
	if deviceName == 'purple':
		colorWipe(strip, color(75, 130, 0))
		return redirect('/', code=302)
	if deviceName == 'yellow':
		colorWipe(strip, color(255, 0, 103))
		return redirect('/', code=302)
		
#@app.route('/', methods = ['POST', 'GET']) 
#def button():
	#strip = PixelStrip(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL)
	#forward_message = "Light on"
	#strip.begin()
	#return render_template('index.html')
	#if request.method == "POST":
		#if 'whitelight' in request.form:
			#colorWipe(strip, color(255, 255, 255))
		#if 'turnoff' in request.form:
		#	strip.begin()
		#	colorWipe(strip, color(255, 0, 0))
#	elif request.method == "GET":
#		return render_template('index.html')
@app.route('/')
def test():
	strip = PixelStrip(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL)
	strip.begin()
	return render_template('index.html')
			
if __name__ == '__main__':
	strip = PixelStrip(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL)
	strip.begin()
	app.run(debug=True, port=80, host='0.0.0.0')
	#port=int(os.getenv('PORT', 4444))
