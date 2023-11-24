#pip3 install requests, pyserial and meshtastic
#make sure you defind the devPath. search for it in the code and change it to your Meshtastic device's devPath (example COM5 or similar for Windows, /dev/ttyUSB0 or similiar for Linxu)
import requests
import json
import subprocess
import serial
import meshtastic
import meshtastic.serial_interface
from pubsub import pub
import time
import datetime
from decimal import Decimal


RECVSTR = ""
datainput2 = ""
MANUALBTCTRANS = ""
MANUALBTCTR = ""
BTCBROAD = ""

#-----------------------------------------------------------DEFINE FUNCTIONS -------------------------------------------  

#LORA RADIO INITIALIZATION
def onReceive(packet, interface): # called when a packet arrives
    global RECVSTR
    global MANUALBTCTRANS
    global MANUALBTCTR
    global datainput2
    RECVSTR = str(packet['decoded']['text'])
    print("")
    print(RECVSTR)
    print("")
    interface.sendText("rcvd..")
    if "==" in RECVSTR:
        interface.sendText("FIN!")
        RECVSTR = RECVSTR.replace("+","")
        RECVSTR = RECVSTR.replace("=","")
        MANUALBTCTRANS += RECVSTR
        MANUALBTCTR = MANUALBTCTRANS
        print("")
        print(MANUALBTCTR)
        print("")
        print("Length:"+str(len(MANUALBTCTR)))
        if len(MANUALBTCTR) > 0:
            try:
                interface.sendText("Length:"+str(len(MANUALBTCTR)))
            except Exception:
                print(f"failed")
    if "+" in RECVSTR:
        interface.sendText("cont...")
        RECVSTR = RECVSTR.replace("+","")
        MANUALBTCTRANS += RECVSTR
        print("")
        print(MANUALBTCTRANS)
        print("")
        if len(MANUALBTCTRANS) > 0:
            try:
                interface.sendText("Length:"+str(len(MANUALBTCTRANS)))
            except Exception:
                print(f"failed")
        
    if "-clear-" in RECVSTR:
        BTCBROAD = ""
        BTCSEND = ""
        MANUALBTCTR = ""
        MANUALBTCTRANS = ""
        interface.sendText("Code cleared!")
    
    if "-mempool-" in RECVSTR:
        MEMPOOL = subprocess.getoutput("curl -sSL \"https://mempool.space/api/v1/fees/recommended\"")
        MEMjson = json.loads(MEMPOOL)
        MEMCHECK = str(MEMjson['halfHourFee'])+" Sats/vByte"
        print(MEMCHECK)
        interface.sendText(MEMCHECK)     

    

def onConnection(interface, topic=pub.AUTO_TOPIC): # called when we (re)connect to the radio
    # defaults to broadcast, specify a destination ID if you wish
    interface.sendText("hello mesh")
    print(f"Lora Online")




#TRY LORA RADIO CONNECTION
#try:
pub.subscribe(onReceive, "meshtastic.receive.text")
pub.subscribe(onConnection, "meshtastic.connection.established")
interface = meshtastic.serial_interface.SerialInterface(devPath='COM8') #you need to input your devPath (windows will be COM# like COM5, linux something like /dev/ttyUSB0
#except Exception:
#    print(f"Lora not initialized")



#BEGIN MAIN LOOP WAITING FOR USER INPUT ------------------------------------------------------------
then = datetime.datetime.now()
while True:
    time.sleep(0.25)
    
    #CHECK FOR LORA COMMS
    now = datetime.datetime.now()
    if now.minute - then.minute > 5:
        then = datetime.datetime.now()
        try:
            pub.subscribe(onReceive, "meshtastic.receive.text")
            pub.subscribe(onConnection, "meshtastic.connection.established")
            interface = meshtastic.serial_interface.SerialInterface(devPath='COM8') #you need to input your devPath (windows will be COM# like COM5, linux something like /dev/ttyUSB0
        except Exception:
            print(f"Lora comms not reestablished")
    
    if len(MANUALBTCTR) > 20:
        BTCSEND = "/usr/local/bin/bitcoin-cli sendrawtransaction "+MANUALBTCTR #This is where 
        interface.sendText("BTC Transaction Attempt Broadcast!")
        try:
            BTCBROAD = subprocess.getoutput(BTCSEND)
            print(BTCBROAD)
            if len(BTCBROAD) > 0:
                SENDTHIS = BTCBROAD.strip()
                if len(SENDTHIS) > 200:
                    interface.sendText(SENDTHIS[0:199])
                else:
                    interface.sendText(SENDTHIS)
                BTCBROAD = ""
                BTCSEND = ""
                MANUALBTCTR = ""
                MANUALBTCTRANS = ""
        except Exception:
            BTCBROAD = ""
            BTCSEND = ""
            MANUALBTCTR = ""
            MANUALBTCTRANS = ""
            interface.sendText("Error! Message -clear- and Retry")
            
        
