# TP-Link-HS100-Control
Python script to control TP-Link smart plugs over the local network using encrypted commands.


This script was used to control the TP-Link Kasa HS100 Smart Plug

##How it works:
The script used a TCP socket to send and encrypted JSON command to the plugs IP on port 9999

##Plug_State:
0 = Off
1 = On


##Notes:
This will only work on the same local network as the plug
The plug must be powered on at the wall


##Disclamer:
This code was created for educational and research purposes only.
