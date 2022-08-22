#!/usr/bin/env python

import mport RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
import syslog
import datetime
from time import sleep


reader = SimpleMFRC522()

while True:
        syslog.syslog("Waiting for a card")
        print("Waiting for a card")
        if reader.read():

                id, text = reader.read()
                print(id)
                print(text)
                syslog.syslog(syslog.LOG_INFO, "RFID: " + str(id) + str(text))
                sleep(2)

        else:
                syslog.syslog(syslog.LOG_INFO, datetime.time + "No card found")
                print("No card found")
                sleep(2)

                continue
#finally:
#        GPIO.cleanup()