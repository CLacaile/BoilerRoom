# BOILER ROOM

Boiler Room is a set of devices aimed to control ignition of boilers according to temperature sensors spread accross the house. 
The master is a RaspPi 3 and the slaves (ESPs, Arduinos, ...) are connected via Wi-Fi to the master.
The master receive the temperature data from the slaves and computes whether the boiler should be on or off.
As of v0, the trigger for the on/off switch is a servomotor that turns the boiler switch.
The RaspPi also hosts an http server in order to configure the system (schedule, switching temperature, ...) on a web browser.

# v0 TODO LIST

- Control servo with raspberry pi according to bool?
- Read temperature on ESP8266
- Set communication between master and slaves
- Build http server to control master