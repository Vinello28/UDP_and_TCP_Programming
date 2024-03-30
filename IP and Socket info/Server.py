# Description: server that sends client's IP address and port number to client itself.

from socket import *

serverPort = 12000
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', serverPort))
serverSocket.listen(1)
print('The server is ready to receive')

while True:
    connectionSocket, clientAddress = serverSocket.accept()
    message = connectionSocket.recv(2048).decode('utf-8')
    print('Received message:', message, ' from ', clientAddress)
    messageModified = 'Your IP address is ' + clientAddress[0] + ' and your message is ' + message
    connectionSocket.send(messageModified.encode('utf-8'))
    connectionSocket.close()
