
import RPi.GPIO as GPIO
import time
blink_interval = .3
relay1 = 33 #brown
relay2 = 40 #orange
relay3 = 38 #purple
relay4 = 16 #blue
relay5 = 18 #green
relay6 = 22 #yellow
relay7 = 37 #white
relay8 = 35 #grey

#Config pins
GPIO.setmode(GPIO.BOARD)
GPIO.setup(relay1, GPIO.OUT)
GPIO.setup(relay2, GPIO.OUT)
GPIO.setup(relay3, GPIO.OUT)
GPIO.setup(relay4, GPIO.OUT)
GPIO.setup(relay5, GPIO.OUT)
GPIO.setup(relay6, GPIO.OUT)
GPIO.setup(relay7, GPIO.OUT)
GPIO.setup(relay8, GPIO.OUT)
GPIO.output(relay1, False)
GPIO.output(relay2, False)
GPIO.output(relay3, False)
GPIO.output(relay4, False)
GPIO.output(relay5, False)
GPIO.output(relay6, False)
GPIO.output(relay7, False)
GPIO.output(relay8, False)
GPIO.setwarnings(False)

from flask import Flask
app = Flask(__name__)

@app.route('/1')
def player_1():
        GPIO.output(relay1, True)
        time.sleep(blink_interval)
        GPIO.output(relay1, False)
        time.sleep(blink_interval)
        return 'ack' #for debugging only - remove for speed
@app.route('/2')
def player_2():
        GPIO.output(relay2, True)
        time.sleep(blink_interval)
        GPIO.output(relay2, False)
        time.sleep(blink_interval)
        return 'ack' #for debugging only - remove for speed

#GPIO.cleanup() - where? exceptions and finally
