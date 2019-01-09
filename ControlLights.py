#/usr/bin/env Python

import time
import sys
import neopixels

class Lights():

    NAME = "" # Holds the name of the light for multiple light support
    STATUS = "" # Holds the status of the led for reporting
    neopixel = None  # This is the neopixel object that I am expanding on

    def __init__(self, NAME, LED_COUNT, LED_PIN, LED_FREQ_HZ=800000, LED_DMA=5, LED_INVERT=False):
        self.NAME = NAME  # Holds the name of the light for multiple light support
        self.STATUS = ""  # Holds the status of the led for reporting

        self.neopixel = neopixel.NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT)  # This is the neopixel object that I am expanding on
        self.neopixel.begin()
          
    def getStatus(self):
        return self.STATUS

    def setRed(self):
        """Sets the leds to red

        Keyword arguments:
        """
        color = Color(255, 0, 0)

        for i in range(self.neopixel.getPixels()):
            self.neopixel.setPixelColor(i, color)

        self.neopixel.show()

        self.STATUS = "RED (INDEFINITE)"


    def setGreen(self, time=2):
        """Sets the leds to green for a set time

        Keyword arguments:
        time -- the time (in seconds) you want it to remain green (default 2.0)
        """
        color = Color(0, 255, 0)

        for i in range(self.neopixel.getPixels()):
            self.neopixel.setPixelColor(i, color)

        self.neopixel.show()

        time.sleep(time)

        self.STATUS = "GREEN (%d seconds)" % time


def main(argv):
    userInput = ""

    lead = Lights(NAME="Lead", LED_COUNT=7, LED_PIN=18)

    while userInput not in 'q':
        userInput = raw_input("Please enter a color: ")

        if userInput in "green":
            lead.setGreen()

        elif userInput in "red":
            lead.setRed()
        
        else:
            print("Input not accepted")
        
if __name__ == "__main__":
    main(sys.argv)
