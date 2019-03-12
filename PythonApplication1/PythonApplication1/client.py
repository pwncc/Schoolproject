import socket
import threading
LHOST = '83.160.125.93'
LPORT = 80
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.connect((LHOST, LPORT))

def one():
    print("start1")
    while True:
        try:
            inp = input()
            s.send(inp.encode())
        except Exception as e:
            print(str(e))

def two():
    print("start")
    while True:
        q = s.recv(4096).decode()
        print(q)

t1 = threading.Thread(target = one)
t2 = threading.Thread(target = two)
t1.setDaemon(True)
t2.setDaemon(True)
t1.start()
t2.start()
while True:
    pass