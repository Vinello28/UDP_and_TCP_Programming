from socket import *
from time import sleep

serverName = 'localhost'
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))
sentence = 'a'

for i in range(100):
    clientSocket.send(sentence.encode('utf-8'))
    sleep(0.1)

clientSocket.close()
