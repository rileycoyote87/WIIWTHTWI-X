import time
import threading;
from threading import Thread
import queue
from gpiothread import GPIOThread;
import atexit;
from flask import Flask;
from flask import request;



queueDictionary = {};
threads = [];

for e in range(1,9):
        queueDictionary[e] = queue.Queue();

for q in queueDictionary.keys():
        t = GPIOThread(queueDictionary[q],q);
        t.daemon = True;
        t.start();
        threads.append(t);


def close_running_threads():
    for thread in threads:
        thread.running=False;
        thread.join()
    print("Threads complete, ready to finish")

atexit.register(close_running_threads)



app = Flask(__name__)

@app.route('/players', methods=['GET'])
def spray_player():
        player_id = request.args.get('player_id',type = int);
        blinktime = request.args.get('blinktime',type = float)/1000;
        
        if(player_id >= 1 and player_id <=8):
            print("Adding item to queue for " + str(player_id));
            queueDictionary[player_id].put(blinktime);
            print('Spraying' + str(player_id) + ' for ' + str(blinktime));
            return 'Spraying' + str(player_id) + ' for ' + str(blinktime);
        else:
                return "Invalid Player ID";

