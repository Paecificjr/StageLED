#/usr/bin/python3

import time
import sys
import board
import neopixel

class Lights():

    NAME = "" # Holds the name of the light for multiple light support
    STATUS = "" # Holds the status of the led for reporting
    neopixel = None  # This is the neopixel object that I am expanding on

    def __init__(self, NAME, LED_COUNT, LED_PIN, LED_FREQ_HZ=800000, LED_DMA=5, LED_INVERT=False):
        self.NAME = NAME  # Holds the name of the light for multiple light support
        self.STATUS = ""  # Holds the status of the led for reporting
        BRIGHTNESS = 0.2
        self.neopixel = neopixel.NeoPixel(LED_PIN, LED_COUNT)  # This is the neopixel object that I am expanding on
          
    def getStatus(self):
        return self.STATUS

    def setRed(self):
        """Sets the leds to red

        Keyword arguments:
        """
        color = (255, 0, 0)

        self.neopixel.fill(color)

        self.STATUS = "RED (INDEFINITE)"


    def setGreen(self, wait=2):
        """Sets the leds to green for a set time

        Keyword arguments:
        time -- the time (in seconds) you want it to remain green (default 2.0)
        """
        color = (0, 255, 0)

        self.neopixel.fill(color)

        time.sleep(wait)

        self.STATUS = "GREEN (%d seconds)" % time


def main(argv):
    userInput = input("Please enter a color: ")

    lead = Lights(NAME="Lead", LED_COUNT=7, LED_PIN=board.D18)

    while userInput not in 'q':
        userInput = input("Please enter a color: ")

        if userInput in "green":
            lead.setGreen()

        elif userInput in "red":
            lead.setRed()
        
        else:
            print("Input not accepted")
        
if __name__ == "__main__":
    main(sys.argv)
