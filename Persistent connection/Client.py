# Description: Client side of the persistent connection

from socket import *

serverName = 'localhost'
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))

while True:
    sentence = input('Input lowercase sentence:')
    clientSocket.send(sentence.encode('utf-8'))
    if sentence == '.':
        break
    modifiedSentence = clientSocket.recv(1024)
    print('From Server:', modifiedSentence.decode('utf-8'))

clientSocket.close()
