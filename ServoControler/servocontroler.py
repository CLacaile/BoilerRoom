# TODO log file to track ON/OFF status

import sys
import pigpio

if __name__ == "__main__":
    pi = pigpio.pi()
    if sys.argv[1] == "ON":
        # turn the boiler switch to ON position
        pi.set_servo_pulsewith(18, 1000)
        print(">> Boiler turned on")
    elif sys.argv[1] == "OFF":
        # turn the boiler switch to OFF position
        pi.set_servo_pulsewith(18, 2000)
        print(">> Boiler turned off")
