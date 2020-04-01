
#!/usr/bin/python
#The Temperature reader uses the DHT22 sensor to read the temperature and humidity in the room once every 60 seconds, and 
#write the data to an sqlite database.  It has a temperature range test where if the temperature is within range, it keeps a green
#LED lit, and if the temperature is out of range, a red LED blinks, and a text message is sent to the user,
#alerting them to the temperature condition.
#This was written for Joshua Simons's Embedded Linux Class at SUNY New Paltz 2020
#And is licenses under the MIT Software License

#Import libraries as needed
import RPi.GPIO as GPIO
import Adafruit_DHT
import time
import os
import sqlite3 as sql
import smtplib

#Globals
redPin = 27
greenPin = 22
tempPin = 17

#Temp and Humidity Sensor
tempSensor = Adafruit_DHT.DHT22

#LED Variables---------------------------------------------------------------------------------------
#Duration of each Blink
blinkDur = .1
#Number of times to Blink the LED
blinkTime = 7
#----------------------------------------------------------------------------------------------------

#SMTP eMail Variables
eFROM = "kd2egt@gmail.com"
eTO = "8453094409@msg.fi.google.com"
Subject = "Alert!"
server = smtplib.SMTP_SSL('smtp.gmail.com', 465)

#Connect to the database
con = sql.connect('../log/tempLog.db')
cur = con.cursor()

#Set the initial checkbit to 0.  This will throw a warning when run, but will still work just fine
eChk = 0

#Initialize the GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(redPin,GPIO.OUT)
GPIO.setup(greenPin,GPIO.OUT)

#Function to blink the red LED. onn/off duration is set by global blinkDur
def oneBlink(pin):
	GPIO.output(pin,True)
	time.sleep(blinkDur)
	GPIO.output(pin,False)
	time.sleep(blinkDur)

#Function to alert the user via text/email (text uses email to sms gateway)
def alert(tempF):
	global eChk
	if eChk == 0:
		Text = "The monitor now indicates that the temperature is now "+str(tempF)
		eMessage = 'Subject: {}\n\n{}'.format(Subject, Text)
		server.login("kd2egt@gmail.com", "ybihbernfcvynzju")
		server.sendmail(eFROM, eTO, eMessage)
		server.quit
		eChk = 1
#Function to read the Temperature and humidity off of the DHT sednsor and return it.
#Temperature is converted to Fahrenheit
def readDHT(tempPin):
	humidity, temperature = Adafruit_DHT.read_retry(tempSensor, tempPin)
	temperature = temperature * 9/5.0 +32
	if humidity is not None and temperature is not None:
		tempF = '{0:0.1f}'.format(temperature)
		humid = '{1:0.1f}'.format(temperature, humidity)
	else:
		print('Error Reading Sensor')

	return tempF, humid

#Dummy time for first itteration of the loop
oldTime = 60

#Read Temperature right off the bat
tempF, hum = readDHT(tempPin)

try:
	while True:
		#Send text message alert if temperature is out of range
		if 60 <= float(tempF) <= 70:
			eChk = 0
			GPIO.output(redPin,False)
			GPIO.output(greenPin,True)
		else:
			GPIO.output(greenPin,False)
#			alert(tempF)
			oneBlink(redPin)

		#if loop set for every 60 seconds
		if time.time() - oldTime > 59:
			tempF, humid = readDHT(tempPin)

			#Defines and executes the sql query (tempLog is the table name in the .db)
			cur.execute('INSERT INTO tempLog values(?,?,?)', (time.strftime('%Y-%m-%d %H:%M:%S'),tempF,humid))
			con.commit()
			print("Temp and Humidity Read and Logged "+time.strftime('%Y-%m-%d %H:%M:%S'))
			oldTime = time.time()

except KeyboardInterrupt:
	os.system('clear')
	con.close()
	print ("Temperature Logger and Web App Exited Cleanly")
	exit(0)
	GPIO.cleanup
