# Description: Server side of the persistent connection

from socket import *

serverPort = 12000
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', serverPort))
serverSocket.listen(1)

while True:
    print('The server is ready to receive')
    connectionSocket, addr = serverSocket.accept()
    print('Connection from:', addr)
    while True:
        sentence = connectionSocket.recv(1024).decode('utf-8')
        if sentence == '.':
            break
        capitalizedSentence = sentence.upper()
        connectionSocket.send(capitalizedSentence.encode('utf-8'))
    connectionSocket.close()
