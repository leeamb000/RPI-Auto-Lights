import RPi.GPIO as GPIO
import time
import asyncio
from kasa import SmartPlug

#configure pin set-up for each sensor
GPIO.setmode(GPIO.BCM)
PIR_PIN_SENSOR1 = 14
PIR_PIN_SENSOR2 = 15
GPIO.setup(PIR_PIN_SENSOR1, GPIO.IN)
GPIO.setup(PIR_PIN_SENSOR2, GPIO.IN)

#initialize global variables
hitSensor1 = False
hitSensor2 = False
time1 = 0
time2 = 0
numPeople = 0

#sensor 1 event
def MOTION1(PIR_PIN_SENSOR1):
    #access global variables
    global hitSensor1
    global hitSensor2
    global time1
    global time2
    global numPeople

    hitSensor1 = True #sensor 1 hit
    time1 = time.time() #set time sensor 1 was hit

    #when both sensors are hit
    timeTaken = time1 - time2
    if hitSensor1 == True & hitSensor2 == True & (timeTaken < 1.5): #and time taken is within timeout range
        #decrement number of people
        numPeople = numPeople - 1
        print(f'\nPeople in room: {numPeople}')
        #reset variables
        hitSensor1 = False
        hitSensor2 = False
        time1 = 0
        time2 = 0
        if numPeople == 0: #turn lights off
            print('*****lights off!*****')
            p = SmartPlug("192.168.0.234")
            asyncio.run(p.turn_off())
                

#sensor 2 event
def MOTION2(PIR_PIN_SENSOR2):
    #access global variables
    global hitSensor1
    global hitSensor2
    global time1
    global time2
    global numPeople

    hitSensor2 = True #sensor 2 hit
    time2 = time.time() #set time sensor 2 was hit

    #when both sensors are hit
    timeTaken = time2 - time1
    if hitSensor1 == True & hitSensor2 == True & (timeTaken < 1.5): #and time taken is within timeout range
        #increment number of people
        numPeople = numPeople + 1
        print(f'\nPeople in room: {numPeople}')
        #reset variables
        hitSensor1 = False
        hitSensor2 = False
        time1 = 0
        time2 = 0
        if numPeople == 1: #turn lights on  
            print('*****lights on!*****')
            p = SmartPlug("192.168.0.234")
            asyncio.run(p.turn_on())

#inputs
sensor1 = GPIO.add_event_detect(PIR_PIN_SENSOR1, GPIO.RISING, callback=MOTION1)
sensor2 = GPIO.add_event_detect(PIR_PIN_SENSOR2, GPIO.RISING, callback=MOTION2)

try:
    while True:
        if sensor1 == 1:
            sensor1
        elif sensor2 == 1:
            sensor2

except KeyboardInterrupt:
    print('Quit')
    GPIO.cleanup()
