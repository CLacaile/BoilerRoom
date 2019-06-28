# BOILER ROOM

Boiler Room is a set of devices aimed to control ignition of boilers according to temperature sensors spread accross the house. 
The master is a RaspPi 3 and the slaves (ESPs, Arduinos, ...) are connected via Wi-Fi to the master.
The master receive the temperature data from the slaves and computes whether the boiler should be on or off.
As of v0, the trigger for the on/off switch is a servomotor that turns the boiler switch.
The RaspPi also hosts an http server in order to configure the system (schedule, switching temperature, ...) on a web browser.

# v0 scheme

![Boiler Room Diagram](Boiler-Room-diagram.png)

# v0 TODO LIST

- Control servo with raspberry pi according to bool?
- Read temperature on ESP8266
- Set communication between master and slaves
- Build http server to control master

## Control servo with raspberry pi 

Make sure `pigpiod` deamon is running:
```
sudo killall pigpiod
sudo pigpiod
```
In Python:
```python
import pigpio
pi = pigpio.pi()
pi.set_servo_pulsewidth(18, 1500) # SG90 set to middle position
pi.set_servo_pulsewidth(18, 1000) # SG90 set to left position
pi.set_servo_pulsewidth(18, 2000) # SG90 set to right position
pi.stop()
```

## ServoControler

ServoControler is a simple Python script that takes as arg ON or OFF:
- ON will turn the servo all the way to one side (left, 1/1000s PW) using pigpio lib to turn the boiler switch.
- OFF will turn the servo all the way to the other side (right, 1/2000s PW).

*TODO*: log file to track ON/OFF status

## BoilerManager

BoilerManager is the core of the system.
As of v0 it simply reads the temperatures from the files of the database created by SocketServer and computes the average temperature.
It uses a .conf file to read the threshold temperature and the nb of sensors and decides whether to switch ON or OFF the boiler.
The computation of the average should be performed at regular intervals (10min?).
