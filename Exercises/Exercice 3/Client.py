from socket import *

serverName = 'localhost'
serverPort = 12000

clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.settimeout(6)
try:
    clientSocket.connect((serverName, serverPort))
    sentence = input('Input something: ')
    clientSocket.send(sentence.encode('utf-8'))
    consonantsInSentence = clientSocket.recv(2048).decode('utf-8')
    print('From server: ', consonantsInSentence)
except:
    print('The server is not responding.')
finally:
    clientSocket.close()

