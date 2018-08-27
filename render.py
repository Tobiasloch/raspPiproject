import numpy
import time
from threading import Thread
from gpiozero import PWMLED

class gameObject:
	
	def __init__(self, texture):
		self.texture = texture
		self.texture = None
		self.position = [0.0,0.0]
		self.scale = [0.0,0.0]
		self.animationList = [[0,0]]
		self.animationSpeed = 0
	
	def move(self, x,y):
		position[0]+=x
		position[1]+=y
	
	def loadAnimation(self):
		print("animation")
	
pass

class graphicEngine:
	
	def __init__(self, pixelsX, pixelsY, pixelSleeping=0.01, frameRate=30):
		xPins = [PWMLED(2), PWMLED(3), PWMLED(4), PWMLED(17), PWMLED(27), PWMLED(22), PWMLED(10), PWMLED(9), PWMLED(11), PWMLED(0), PWMLED(5), PWMLED(6), PWMLED(13), PWMLED(19)]
		yPins = [PWMLED(26), PWMLED(14), PWMLED(15), PWMLED(18), PWMLED(23), PWMLED(24), PWMLED(25), PWMLED(8), PWMLED(7), PWMLED(1), PWMLED(12), PWMLED(16), PWMLED(20), PWMLED(21)]

		self.pixelsX = pixelsX
		self.pixelsY = pixelsY
		
		self.pixelSleeping = pixelSleeping
		self.frameRate = frameRate
		
		self.led = numpy.resize(xPins, pixelsX)
		self.ground = numpy.resize(yPins, pixelsY)
		
		self.pixels = numpy.zeros((pixelsX, pixelsY))
		pass
	
	def run(self):
		renderer = Thread(target=self.paint, args=())
		renderer.start()
		
		self.calcPixels()
		time.sleep(20)
		renderer.join()
	pass
	
	def calcPixels(self):
		self.pixels[0][0] = 1
		self.pixels[1][1] = 0.5
	pass
	
	def paint(self):
		t = 100
		while t>0:
			i = 0
			while i < self.pixelsX:
				j = 0
				while j < self.pixelsY:
					self.ground[j].on()
					self.led[i].value = self.pixels[i][j]
				
					time.sleep(self.pixelSleeping)
				
					self.ground[j].off()
					self.led[i].off()
					j = j+1
				pass
			i = i+1
			pass
			t=t-1
		pass
	pass
	
pass
