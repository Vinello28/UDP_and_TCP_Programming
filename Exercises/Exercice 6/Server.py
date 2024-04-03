from socket import *

serverPort = 12000
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', serverPort))
serverSocket.listen(1)
print('The server is ready to receive')

while True:
    connectionSocket, addr = serverSocket.accept()
    sentence = ''
    i = 100
    while i > 0:
        sentence += connectionSocket.recv(1024).decode('utf-8')
        print(sentence.count('a'))
        i -= 1
    connectionSocket.close()
