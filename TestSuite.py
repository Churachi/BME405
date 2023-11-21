# Team Members: Chur Tam, Cathy Zhu
# Github Repo: git@github.com:Churachi/lab07.git

import RPi.GPIO as GPIO
import time
import Adafruit_GPIO.SPI as SPI
import Adafruit_MCP3008
import numpy as np
from scipy.io.wavfile import write

# using physical pin 11 to blink an LED
GPIO.setmode(GPIO.BOARD)
chan_list = [11]
GPIO.setup(chan_list, GPIO.OUT)

# Hardware SPI Configuration
SPI_PORT = 0
SPI_DEVICE = 0
mcp = Adafruit_MCP3008.MCP3008(spi=SPI.SpiDev(SPI_PORT, SPI_DEVICE))

#Sample Rate Setup
samplerate = 4000
array = np.zeros(shape=(1, 1))

while True:
    #sound is the data needed, storing sound in array
    sound = mcp.read_adc(1)
    print(sound)
    array[i] = sound

    write("example.wav", samplerate, array.astype(np.int16))

    time.sleep(0.00025)