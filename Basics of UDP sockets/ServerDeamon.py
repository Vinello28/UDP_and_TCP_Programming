# This Python script is a simple server application that uses socket programming to listen for incoming TCP/IP connections.
# It receives a message from a client, modifies it, and sends it back to the client.
from socket import *

serverPort = 12000

serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', serverPort))
serverSocket.listen(1)

print('The server is ready to receive')

while True:
    connectionSocket, addr = serverSocket.accept()
    message = connectionSocket.recv(2048).decode('utf-8')
    print(f'Message received: {message}')
    modifiedMessage = message.upper()
    connectionSocket.send(modifiedMessage.encode('utf-8'))
    connectionSocket.close()
