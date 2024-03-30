# Description: UDP Client that sends a message to a server and receives the number of consonants in the message.

from socket import *

serverName = 'localhost'
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_DGRAM)
message = input("Input lowercase sentence: ")
clientSocket.sendto(message.encode(), (serverName, serverPort))
clientSocket.settimeout(5)
try:
    consonants, serverAddress = clientSocket.recvfrom(2048)
    print(f"Received message: {consonants.decode()} from {serverAddress}")
except timeout:
    print("The server is not responding")
finally:
    clientSocket.close()
