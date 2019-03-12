
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
    nicknames[str(addr)] = "Not set"
    while True:
        try:
            ses.settimeout(1000000)
            q = ses.recv(4096)
            print(q.decode())
            if q.decode() == "nickname":
                nicknames[str(addr)] = ses.recv(4096).decode()
            else:
                for i,v in enumerate(sessions):
                    if nicknames[str(addr)] == "Not set":
                        v.send((str(addr[i]) + " Sent a message!: " + q.decode()).encode())
                    else:
                        v.send((nicknames[str(addr)] + " Sent a message!: " + q.decode()).encode())

        except Exception as e:
            print(str(e))
            break



def one():
    global s
    print("started")
    LHOST = '127.0.0.1'
    LPORT = 80
    s.bind((LHOST, LPORT))
    s.listen(1)
    while True:
        try:
            print("yes")
            ses, addr = s.accept()
            sessions.append(ses)
            addresses.append(addr)
            newthread = threading.Thread(target = resend(ses,addr))
            newthread.setDaemon(True)
            newthread.start()
        except Exception as e: 
            print(str(e))

thread = threading.Thread(target = one())
thread.setDaemon(True)
thread.start()
