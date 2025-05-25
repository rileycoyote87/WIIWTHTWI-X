import RPi.GPIO as GPIO
import time
import threading;
from threading import Thread
import queue

class GPIOThread(Thread):


    def __init__(self,queuein,relayval):
        threading.Thread.__init__(self)
        self.running = True;
        self.blink_interval = .3;
        self.relayList = [33,40,38,16,18,22,37,35];
        self.selectedRelay = self.relayList[relayval - 1];
        self.queue = queuein;
        try:
            print("init GPIO");
            GPIO.setmode(GPIO.BOARD);
            GPIO.setup(self.selectedRelay, GPIO.OUT);
            GPIO.output(self.selectedRelay, False);
            GPIO.setwarnings(False);
        except:
            print("exception, cleaning up");
            GPIO.cleanup();
            self.running = False;

    def spray(self,blinktime):
        try:
            print("Spraying " + str(self.selectedRelay) + 'for ' + str(blinktime));
            GPIO.output(self.selectedRelay, True);
            time.sleep(blinktime);
            GPIO.output(self.selectedRelay, False);
            time.sleep(.05);
            #GPIO.cleanup();
        except:
            print("exception, cleaning up");
            GPIO.cleanup();  
            self.running = False;



    def run(self):
        while self.running == True:
            #wait for item to fall into queue
            try:
                item = self.queue.get(timeout=2);
                self.spray(item);
            except queue.Empty:
                continue;
        print("exiting thread");
        GPIO.cleanup();
