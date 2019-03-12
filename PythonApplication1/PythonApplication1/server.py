
import socket
import os
import threading
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.settimeout(100)
sessions = []
addresses = []
nicknames = {}
def resend(ses, addr):
    num = len(nicknames)
    nicknames[num] = "Not set"
    while True:
            ses.settimeout(1000000)
            q = ses.recv(4096)
            print(q.decode())
            if q.decode() == "nickname":
                nicknames[num] = ses.recv(4096).decode()
            else:
                for i,v in enumerate(sessions):
                    try:
                        if nicknames[num] == "Not set":
                            v.send((nicknames[num] + " Sent a message!: " + q.decode()).encode())
                        else:
                            v.send((nicknames[num] + " Sent a message!: " + q.decode()).encode())
                    except Exception as e:
                        print(str(e))

LHOST = "83.160.125.93"
LPORT = 80

while True:
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.bind((LHOST, LPORT))
        print("yes")
        s.listen(1)
        ses, addr = s.accept()
        sessions.append(ses)
        addresses.append(addr)
        newthread = threading.Thread(target = resend, args=(ses, addr))
        newthread.setDaemon(True)
        newthread.start()
    except Exception as e: 
        print(str(e))
