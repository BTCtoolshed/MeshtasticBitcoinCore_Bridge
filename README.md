# Meshtastic BitcoinCore Bridge
Broadcast Raw Transactions over Meshtastic Lora to a computer with Bitcoin Core

# Use Case
https://gotenna.com/blogs/newsroom/blockstream-satellite-and-gotenna-collaborate-to-make-sending-bitcoin-without-internet-possible

Blockstream demonstrated how to use Bitcoin Core without users needing an internet or cellular connection. The machine running Bitcoin Core connected to a Blockstream Satellite and receiving transaction information via Lora Radios (goTenna). 

My challenge was to send raw transactions for broadcasting over Lora, but using Meshtastic. Meshtastic's apps have a maximum buffer of 228 bytes (approximately 228 characters), but raw hex for bitcoin core transactions may be more than 1000 characters. This python file will interpret the "+" and "==" to construct long strings to broadcast the transaction.

# Necessary Devices

* A computer running Bitcoin Core
* A Meshtastic device connected over USB serial to the same computer. 

# Instructions
Bitcoin Core and Meshtastic already have great tutorials. If you don't know how to use Python, please go and find some training for this. If you do know how to use python, simply pip or pip3 install the Meshtastic, pyserial and requests python libraries if you do not have them installed. Then you can run the python file included.

# Commands
* **-mempool-** : Ask the Bitcoin Core machine for the latest midpoint of fees. This will help you construct your raw transaction offline, especially helpful if you have an offline phone wallet.
* **\+** : Add the + symbol and then approximately 200 characters of the raw transaction hex to start constructing the long string
* **\==** : Add == to terminate the string and send the transaction
* **-clear-** : If you make a mistake, you can clear the string and start over

# Example

**Begin by taking your raw transaction hex and dividing it into portions 200 characters or less and add a + sign to the text.**
![Stuff](https://github.com/BTCtoolshed/MeshtasticBitcoinCore_Bridge/blob/main/photos/Bridge01.png?raw=true)
<br><br>
**The very last portion of the hex should have two equal signs == after it to finish the string construction.**
![Stuff](https://github.com/BTCtoolshed/MeshtasticBitcoinCore_Bridge/blob/main/photos/Bridge02.png?raw=true)

<br><br>
**How do you fix when you make an error? You just type in -clear- and start over.**
![Stuff](https://github.com/BTCtoolshed/MeshtasticBitcoinCore_Bridge/blob/main/photos/BridgeBytes.png?raw=true)

<br><br>
**When the Python program begins, it sends out the message "hello mesh" to all who are on the connected device's Mesh network. 

Optional : By sending the message -mempool- , you can check the mempool's "midpoint" of fees to properly account for fees before creating a raw transaction. Every time the python program interacts with your messages sent over Meshtastic, you will see it reply "recvd.." to note that your message has been received.**
![Stuff](https://github.com/BTCtoolshed/MeshtasticBitcoinCore_Bridge/blob/main/photos/Bridge03.png?raw=true)

<br><br>
**Begin sending pieces of your raw transaction with the + sign as you constructed in prior steps. Send them in order! And wait until you see the reply "recvd.." and the following character count, like you see below as Length:204 (this will vary for you).**
![Stuff](https://github.com/BTCtoolshed/MeshtasticBitcoinCore_Bridge/blob/main/photos/Bridge05.png?raw=true)

<br><br>
**After receiving the confirmation of the length of the long string you are constructing, you can keep adding portions of the raw transaction...**
![Stuff](https://github.com/BTCtoolshed/MeshtasticBitcoinCore_Bridge/blob/main/photos/Bridge06.png?raw=true)

<br><br>
**When you reach the last line of the raw transaction, you need to use two equal signs == to terminate it and broadcast the transaction. You will see the "FIN!" message that signifies it will try to broadcast the transaction.**
![Stuff](https://github.com/BTCtoolshed/MeshtasticBitcoinCore_Bridge/blob/main/photos/Bridge06.png?raw=true)

<br><br>
**If there is an error, you will see a message from Bitcoin Core or the computer like this...**
![Stuff](https://github.com/BTCtoolshed/MeshtasticBitcoinCore_Bridge/blob/main/photos/Bridge07.png?raw=true)

<br><br>
**If the broadcast is successful, you will see a message from Bitcoin Core or the computer like this...**
![Stuff](https://github.com/BTCtoolshed/MeshtasticBitcoinCore_Bridge/blob/main/photos/Bridge08.png?raw=true)


