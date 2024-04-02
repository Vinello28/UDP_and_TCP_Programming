
from socket import *

def Consonants(sentence):
    vocals = 'aeiou'
    count = 0
    for letter in sentence:
        if letter.lower() not in vocals:
            count += 1
    return count


serverPort = 12000
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', serverPort))
serverSocket.listen(1)
print('The server is ready to receive')

while True:
    connectionSocket, addr = serverSocket.accept()
    sentence = connectionSocket.recv(2048).decode('utf-8')
    print('Received from client:', sentence)
    consonantsInSentence = Consonants(sentence)
    tosend = 'Your sentence has ' + str(consonantsInSentence) + ' consonants.'
    connectionSocket.send(tosend.encode('utf-8'))
    connectionSocket.close()
