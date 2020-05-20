#UDP server
import socket

UDP_IP = "localhost"
print UDP_IP
UDP_port = 9990

serversocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

serversocket.bind((UDP_IP, UDP_port))

while True:
    data, addr = serversocket.recvfrom(1024)
    print "Server received message: ", data
