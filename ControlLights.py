!#/usr/bin/env Python

import time
from neopixel import *

class Lights():

        self.NAME  # Holds the name of the light for multiple light support
        self.LED_COUNT  
        self.LED_PIN
        self.LED_FREQ_HZ
        self.LED_DMA
        self.LED_INVERT
        self.STATUS  # Holds the status of the led for reporting

    def __init__(self, NAME, LED_COUNT, LED_PIN, LED_FREQ_HZ=800000, LED_DMA=5, LED_INVERT=False):
        self.NAME = NAME  # Holds the name of the light for multiple light support
        self.LED_COUNT = LED_COUNT  
        self.LED_PIN = LED_PIN
        self.LED_FREQ_HZ = LED_FREQ_HZ
        self.LED_DMA = LED_DMA
        self.LED_INVERT = LED_INVERT
        self.STATUS = ""  # Holds the status of the led for reporting

        self.neopixel = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT)  # This is the neopixel object that I am expanding on
        self.neopixel.begin()
          
    def getStatus(self):
        return self.STATUS

    def setRed(self):
        """Sets the leds to red

        Keyword arguments:
        """
        color = Color(255, 0, 0)

        for i in range(LED_COUNT):
            neopixel.setPixelColor(i, color)

        neopixel.show()

        self.STATUS = "RED (INDEFINITE)"


    def setGreen(self, time=2):
        """Sets the leds to green for a set time

        Keyword arguments:
        time -- the time (in seconds) you want it to remain green (default 2.0)
        """
        color = Color(0, 255, 0)

        for i in range(LED_COUNT):
            neopixel.setPixelColor(i, color)

        neopixel.show()

        time.sleep(time)

        self.STATUS = "GREEN (%d seconds)" % time

