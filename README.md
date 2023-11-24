# Meshtastic BitcoinCore Bridge
Broadcast Raw Transactions over Meshtastic Lora to a maching with Bitcoin Core

# Use Case
Blockstream demonstrated how to use Bitcoin Core without users needing an internet or cellular connection. The machine running Bitcoin Core connected to a Blockstream Satellite and receiving transaction information via Lora Radios (goTenna). 

My challenge was to send raw transactions for broadcasting over Lora, but using Meshtastic. Meshtastic's apps have a maximum buffer of 228 bytes (approximately 228 characters), but raw hex for bitcoin core transactions may be more than 1000 characters. This python file will interpret the "+" and "==" to construct long strings to broadcast the transaction.

# Necessary Devices

* A machine running Bitcoin Core, a Meshtastic device connected over USB serial to the same machine. Bitcoin Core and Meshtastic already have great tutorials.

# Instructions
If you don't know how to use Python, please go and find some training for this. If you do know how to use python, simply install the Meshtastic, pyserial and requests libraries if you do not have them installed. Then you can run the python file included.

# Commands
-mempool- : Ask the Bitcoin Core machine for the latest midpoint of fees. This will help you construct your raw transaction offline, especially helpful if you have an offline phone wallet.
+ : Add the + symbol and then approximately 200 characters of the raw transaction hex to start constructing the long string
== : Add == to terminate the string and send the transaction
-clear- : If you make a mistake, you can clear the string and start over

# Example
