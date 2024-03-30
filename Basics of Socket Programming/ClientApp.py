# This Python script is a simple client application that uses socket programming to establish a TCP/IP connection with a server.
# It sends a user-inputted message to the server and receives a response, which is then printed to the console.
rom socket import *

serverName = 'localhost'
serverPort = 12000

clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))
message = input('Write something: ')
clientSocket.sendto(message.encode('utf-8'), (serverName, serverPort))
modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
modifiedMessage = modifiedMessage.decode('utf-8')
print(modifiedMessage)

clientSocket.close()