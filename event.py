from events import Event
from players.entity import Player
from players.helpers import index_from_userid
from messages import SayText2
import re
import urllib.request
import threading
from threading import Thread



HOST = '192.168.1.11'
PORT = 5000

playerReg = re.compile('\d.*');


class ServerRequest(Thread):


    def __init__(self,playerIndex,blinkTime):
        threading.Thread.__init__(self)
        self.playerIndex = playerIndex
        self.blinkTime = blinkTime;
    def run(self):
        request_string = "http://" + HOST + ":" + str(PORT) + "/players?player_id=" + str(self.playerIndex) + "&blinktime=" + str(self.blinkTime);
        #print(request_string);
        print(str(self.playerIndex) + ' ' + str(self.blinkTime) + "\n");
        try:
            urllib.request.urlopen(request_string).read();
        except:
            print("request exception");



def load():
    SayText2('Plugin has been loaded successfully!').send()


def unload():
    SayText2('Plugin has been unloaded successfully!').send()


@Event('player_hurt')
def on_player_death(game_event):
    # Get the user ID of the spawned player
    userid = game_event['attacker']
    #print(userid);
    if(userid > 0):
        playerName = Player.from_userid(userid).get_name();
        testRegEx = playerReg.match(playerName.replace('BOT ',''));
        #print(testRegEx);
        if(testRegEx):
            dmg_amt = game_event['dmg_health'];
            remaininghealth = game_event['health'];
            msg = playerName;
            msg += ' has pwn3d ';
            msg += Player.from_userid(game_event['userid']).get_name();
            try:
                #print(playerName.replace('BOT ',''));
                playerIndex = int((playerName.replace('BOT ',''))[:1]);
                if(playerIndex >=1 and playerIndex <=8):
                    if(remaininghealth == 0):
                        requestthread = ServerRequest(playerIndex,425);
                        requestthread.start();
                    else:
                        if(dmg_amt > 30):
                            requestthread = ServerRequest(playerIndex,dmg_amt+150);
                            requestthread.start();
            except:
                  print("invalid player");
