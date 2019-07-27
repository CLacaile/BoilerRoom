# BOILER ROOM

Boiler Room is a set of devices aimed to control ignition of boilers according to temperature sensors spread accross the house. 
The master is a RaspPi 3 and the slaves (ESPs, Arduinos, ...) are connected via Wi-Fi to the master.
The master receive the temperature data from the slaves and computes whether the boiler should be on or off.
As of v0, the app will be a Django app that can be easily accessed via web browsers on other devices. It triggers a servomotor that turns the boiler switch.
In the future, a database will be implemented as well as an advanced responsive UI.

# v1 scheme for the future

![Boiler Room Diagram](Boiler-Room-diagram.png)

# v0 Roadmap

- [x] Install latest version of Python 3
- [x] Control servo with raspberry pi according to bool?
- [x] Install Django and create app
- [ ] Read temperature on ESP8266
- [ ] Set communication between master and slaves
- [ ] Build Apache production server

# Notes

As of v0 BoilerManager is a Django webapp that only controls the GPIO of the RPi.
In the future, it will monitor sensors data as well as perform the computations for the tempratures.

## Django

### Build Python 3.6.9 from sources

Installation process is detailed [here](https://github.com/instabot-py/instabot.py/wiki/Installing-Python-3.7-on-Raspberry-Pi)

1. Install the build tools :
```
sudo apt-get update -y
 sudo apt-get install build-essential tk-dev libncurses5-dev libncursesw5-dev libreadline6-dev libdb5.3-dev libgdbm-dev libsqlite3-dev libssl-dev libbz2-dev libexpat1-dev liblzma-dev zlib1g-dev libffi-dev -y
```
2. Fetch last version of Python (Python 3.6.9 as of writing)
```
wget https://www.python.org/ftp/python/3.6.9/Python-3.6.9.tar.xz
 tar xf Python-3.6.9.tar.xz
 cd Python-3.6.9
 ./configure
 make
 sudo make altinstall
```

### Django

1. Install Django:
```
pip3.7 install Django
```

2. Create the project:
```
django-admin startproject Boilr_project_<version>
```

3. Create an app:
```
python manage.py startapp Boilr
```

## Controling the servo
### What?

ServoControler is a simple Python script that takes as arg ON or OFF:
- ON will turn the servo all the way to one side (left, 1/1000s PW) using pigpio lib to turn the boiler switch.
- OFF will turn the servo all the way to the other side (right, 1/2000s PW).

*TODO*: log file to track ON/OFF status

*EDIT 26/07/2019* : this script will be the `views.py` file in the Django app

### How? : Control a servo with RPi 

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
*Note*: Pin 18 is mandatory to have stable hardware PWM

