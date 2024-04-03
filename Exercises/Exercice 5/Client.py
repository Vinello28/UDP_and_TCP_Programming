from socket import *

serverName = 'localhost'
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_DGRAM)
message = input('Input number:')
clientSocket.sendto(message.encode('utf-8'), (serverName, serverPort))
clientSocket.settimeout(2)
try:
    modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
    print(modifiedMessage.decode('utf-8'))
except timeout:
    print('Timeout')
finally:
    clientSocket.close()

clientSocket.close()
