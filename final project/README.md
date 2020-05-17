Author(s): 
	Skyler Young
	Joshua Simons (teacher)


Version: 
	1.0


About:

This project is a collection of functions and classes that I wrote
to expand or utilize the sensors that we used in the Embedded Linux class.
I used my professor's code for reference.


Source(s):

	https://github.com/joshua-simons/EL2020/blob/sensor_lib/python/sensors.py


Documentation:

	DefaultPins :	a class that contains the default pinset for the library. It has the three light pins, as well as pins	
					for the touch, vibration, sound, buzzer and converter sensors. You can set GPIO activation for one pin
					at a time, or all at once.
					
	Sensor: 		The main class here. It has a method to light up the different LEDS depending on the status attribute. You can
					also set the status attribute, configure the output, and configure the pins.
					
	Touch:			Child class of sensor which has a touch pin set to its pinset by default
	
	Vibration:		Child class of sensor which has a vibration pin set to its pinset by default
	
	Sound:			Child class of sensor which has a sound pin set to its pinset by default
	
	Buzzer:			Child class of sensor which has a buzzer pin set to its pinset by default
	
	Converter:		Child class of sensor which has a converter pin set to its pinset by default
					

	
