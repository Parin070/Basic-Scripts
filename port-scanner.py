import socket
import threading
from queue import Queue

target = input("Enter target IP (x.x.x.x format): ")
#scanme.nmap.org <- For practice

queue = Queue()
open_ports=[]

def portscan(port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1) #waits max 1 second
        sock.connect((target, port))
        return True
    except:
        return False

def fillQueue(portList):
    for port in portList:
        queue.put(port)

def worker():
    while not queue.empty():
        port = queue.get()
        if portscan(port):
            print(f'Port {port} is open.')
            open_ports.append(port)

portList = [
    21, 22, 23, 25, 53, 80, 110, 119, 123, 143,
    161, 194, 443, 445, 465, 514, 515, 587, 631, 993,
    995, 1080, 1194, 1433, 1521, 1723, 2049, 2082, 2083, 2086,
    2087, 2095, 2096, 3000, 3306, 3389, 3724, 4444, 4500, 5000,
    5432, 5900, 5938, 6379, 6660, 6661, 6662, 6663, 6664, 6665,
    6666, 6667, 6668, 6669, 7000, 7070, 7777, 8000, 8080, 8081,
    8443, 8888, 9000, 9090, 9200, 9929, 10000, 10050, 10051, 11211,
    27017, 27018, 27019, 28017, 31337, 32400, 33060, 49152, 49153, 49154,
    49155, 49156, 49157, 50000, 51413, 54321, 55000, 55001, 60000, 61616,
    62078, 63000, 63001, 64000, 64001, 65000, 65001, 65100, 65200, 65535
]
#Contains both open and closed ports
fillQueue(portList)

thread_list=[]

for t in range(20):
    thread=threading.Thread(target=worker)
    thread_list.append(thread)

for i in thread_list:
    i.start()

for i in thread_list:
    i.join()

print(f'Open ports are: {open_ports}')