#UDP Client
import socket

#UDP_IP = socket.gethostname()
UDP_port = 9990

msg = raw_input("What would you like to tell the server? ")

clientsocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

clientsocket.sendto(msg, ('localhost',UDP_port))
