from socket import *


serverPort = 12000
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', serverPort))
serverSocket.listen(1)
print("The server is ready to receive")

while True:
    connectionSocket, addr = serverSocket.accept()
    message = connectionSocket.recv(2048)
    print(f"Received message: {message.decode()}")
    modifiedMessage = message.decode('utf-8').upper()
    connectionSocket.send(modifiedMessage.encode())
    print(f"Sent message: {modifiedMessage} to {addr}")
    connectionSocket.close()

