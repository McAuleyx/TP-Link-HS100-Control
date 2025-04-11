import socket
import json
import struct

def tplink_encrypt(msg):
    key = 171
    result = b''
    for c in msg:
        xor = key ^ ord(c)
        key = xor
        result += bytes([xor])
    return result

def tplink_decrypt(data):
    key = 171
    out = ''
    for b in data:
        out += chr(b ^ key)
        key = b
    return out

def onoff(ip, state):
    s = socket.socket()
    s.connect((ip, 9999))
    
    cmd = json.dumps({"system": {"set_relay_state": {"state": state}}})
    encrypted = tplink_encrypt(cmd)
    payload = struct.pack(">I", len(encrypted)) + encrypted
    s.send(payload)
    
    raw_len = s.recv(4)
    length = struct.unpack(">I", raw_len)[0]
    data = s.recv(length)
    s.close()
    
    return tplink_decrypt(data)

# set IP and desired state
plug_ip = '192.168.12.18'
plug_state = 0  # 0 = off, 1 = on

result = onoff(plug_ip, plug_state)

print("The plug was turned " + ("on" if plug_state else "off") + ".")
