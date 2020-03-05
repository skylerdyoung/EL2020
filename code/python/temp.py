import RPi.GPIO as GPIO
import Adafruit_DHT as DHT

tempPin = 17

tempSensor = DHT.DHT11

while True:
        temperature, humidity = DHT.read_retry(tempSensor, tempPin)
        temperature = temperature * 9/5.0 +32
        if humidity is not None and temperature is not None:
                tempFahr = '{0:0.1f}'.format(temperature)
                print('Temperature = {0:0.1f}*F Humidity = {1:0.1f}%'.format(temperature, humidity))
        else:
                print('Failed to get reading. Try again!')

