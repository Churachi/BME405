import RPi.GPIO as GPIO

while True:
    # For 5s, read output of sound sensor in 100 ms intervals
    # Turn LED on for 100s if sound sensor is tapped
    sound = mcp.read_adc(1)
    print(sound)        
    time.sleep(0.1)