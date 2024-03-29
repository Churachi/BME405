import RPi.GPIO as GPIO
import time
import Adafruit_GPIO.SPI as SPI
import Adafruit_MCP3008
import numpy as np
import scipy.io.wavfile
import array

# using physical pin 11 to blink an LED
GPIO.setmode(GPIO.BOARD)
chan_list = 10
GPIO.setup(chan_list, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

# Hardware SPI Configuration
SPI_PORT = 0
SPI_DEVICE = 0
mcp = Adafruit_MCP3008.MCP3008(spi=SPI.SpiDev(SPI_PORT, SPI_DEVICE))

#Sample Rate Setup
samplerate = 4000
lst = []
button = False
fileName = 0

while True:
    if GPIO.input(10) == GPIO.HIGH:
        print("Recording: Start")
        time.sleep(1)
        button = True
    
    while button == True:
        #sound is the data needed, storing sound in array
        sound = mcp.read_adc(1)
        lst.append(sound)
        time.sleep(0.00025)

        if GPIO.input(10) == GPIO.HIGH:
            print("Recording: End")
            time.sleep(1)
            button = False
            my_array = np.array(lst)

            # np.savetxt(f"example{fileName}.wav", lst, delimiter=',')   # X is an array
            scipy.io.wavfile.write("example0.wav", samplerate, my_array)

            print("Example %s printed" % str(fileName))
            lst = []
            fileName = fileName + 1
