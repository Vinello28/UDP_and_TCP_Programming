from socket import *

serverName = 'localhost'
serverPort = 12000

clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))

message = input("Write something: ")
clientSocket.send(message.encode('utf-8'))

modifiedMessage = clientSocket.recv(2048)
print(f"From Server: {modifiedMessage.decode('utf-8')}")

clientSocket.close()
