#import statements

import RPi.GPIO as GPIO
import Adafruit_DHT
import time
import signal
import os

import paho.mqtt   
import mraa 


#setup

df = DefaultPins()

GPIO.setmode(GPIO.BCM)
df.setAllGPIO()

#classes

class DefaultPins:

    def __init__(self, **pins):
        self.name = "Default Pins"
        
        self.yellow_pin = pins.get("yellow_pin")
        self.green_pin = pins.get("green_pin")
        self.red_pin = pins.get("red_pin")

        self.touch_pin = pins.get("touch_pin")
        self.vibration_pin = pins.get("vibration_pin")
        self.sound_pin = pins.get("sound_pin")
        self.buzzer_pin = pins.get("buzzer_pin")
        self.converter_pin = pins.get("converter_pin")
       
    def configurePins( **pins)
        self.yellow_pin = pins.get("yellow_pin")
        self.green_pin = pins.get("green_pin")
        self.red_pin = pins.get("red_pin")

        self.touch_pin = pins.get("touch_pin")
        self.vibration_pin = pins.get("vibration_pin")
        self.sound_pin = pins.get("sound_pin")
        self.buzzer_pin = pins.get("buzzer_pin")
        self.converter_pin = pins.get("converter_pin")
        
    def setGPIO(attrib = None, gpioset = GPIO.OUT )
    
        if attrib == None:
        
            print("No attribute set.")
        
        else
    
            GPIO.setup(attrib, gpio)
  
    def setAllGPIO()
    
        GPIO.setup(self.yellow_pin,GPIO.OUT)
        GPIO.setup(self.green_pin,GPIO.OUT)
        GPIO.setup(self.red_pin,GPIO.OUT)

        GPIO.setup(self.touch_pin, GPIO.IN)
        GPIO.setup(self.vibration_pin, GPIO.IN)
        GPIO.setup(self.sound_pin, GPIO.IN)
        GPIO.setup(self.buzzer_pin,GPIO.IN)
        GPIO.setup(self.converter_pin, GPIO.IN)
        
        
class Sensor:

    global df
    
    status = None
    output = None
  
    pin_set = []

    def __init__(self):
        self.name = "Sensor"

    def displayStatusLED(lightTimeParam = 1):

    #used for testing purposes
    #this function connects to the three LEDS
    #to tell you what's happening
    
        tempStatusPin = None
        lightTime = lightTimeParam
    
        try:
    
            if status == "good to go":
    
                tempStatusPin = df.green_pin
                
            elif status == "stand by":
        
                tempStatusPin = df.yellow_pin
    
            else:
        
               tempStatusPin = df.red_pin

            GPIO.output(tempStatusPin,  True)
        
            time.sleep(lightTime)
    
            GPIO.output(tempStatusPin, False)
        
        except:
            
            print ( "Not Configured" )
            
    def setStatus(statusVal):
    
        self.status = statusVal
    
    
    def configureOutput(outputVal):
    
        self.output = outputVal
        
    def configurePins(**pins):
        
        for pin in pins:
        
            self.pin_set.append(pin)
        
    
class Touch(Sensor):

    def __init__(self):
        super().__init__()
        self.name = "Vibration " + self.name
        self.pin_set.append(df.touch_pin)

class Vibration(Sensor):

    def __init__(self):
        super().__init__()
        self.name = "Vibration " + self.name
        self.pin_set.append(df.vibration_pin)
        
class Sound(Sensor):

    def __init__(self):
        super().__init__()
        self.name = "Sound " + self.name 
        self.pin_set.append(df.sound_pin)


class Buzzer(Sensor):

    def __init__(self):
        super().__init__()
        self.name = "Buzzer " + self.name
        self.pin_set.append(df.buzzer_pin)

class Converter(Sensor):

    def __init__(self):
        super().__init__()
        self.name = "Converter " + self.name
        self.pin_set.append(df.converter_pin)