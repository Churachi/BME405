import RPi.GPIO as GPIO

# Hardware SPI Configuration
SPI_PORT = 0
SPI_DEVICE = 0
mcp = Adafruit_MCP3008.MCP3008(spi=SPI.SpiDev(SPI_PORT, SPI_DEVICE))

while True:
    # For 5s, read output of sound sensor in 100 ms intervals
    # Turn LED on for 100s if sound sensor is tapped
    sound = mcp.read_adc(1)
    print(sound)        
    time.sleep(0.1)
