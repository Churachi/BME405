import RPi.GPIO as GPIO
import time
import Adafruit_GPIO.SPI as SPI
import Adafruit_MCP3008
import numpy as np
from scipy.io.wavfile import write

# using physical pin 11 to blink an LED
GPIO.setmode(GPIO.BOARD)
chan_list = [10]
GPIO.setup(chan_list, GPIO.IN)

# Hardware SPI Configuration
SPI_PORT = 0
SPI_DEVICE = 0
mcp = Adafruit_MCP3008.MCP3008(spi=SPI.SpiDev(SPI_PORT, SPI_DEVICE))

#Sample Rate Setup
samplerate = 4000
array = np.zeros(shape=(1, 1))
button = False
fileName = 0

while True:
    print("Code is running")
    # if GPIO.input(10) == GPIO.HIGH:
        # time.sleep(500)
    button = True
    
    while button == True:
        print("I am recording data")
        #sound is the data needed, storing sound in array
        sound = mcp.read_adc(1)
        print(sound)
        np.append(array, sound)
        time.sleep(0.00025)

        if GPIO.input(10) == GPIO.HIGH:
            print("I am done recording data")
            time.sleep(0.1)
            button = False
            print("About to print")
            write(f"example{fileName}.wav", samplerate, array.astype(np.int16))
            print("Example %s printed" %(str(fileName)))
            array = np.zeros(shape=(1, 1))
            fileName = fileName + 1