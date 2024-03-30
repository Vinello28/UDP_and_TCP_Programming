# Description: UDP Server that receives a message from a client and sends back the number
# of consonants in the message.

from socket import *


serverPort = 12000
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(('', serverPort))
print("The server is ready to receive")

while True:
    message, clientAddress = serverSocket.recvfrom(2048)
    message = message.decode()
    print(f"Received message: {message} from {clientAddress}")
    consonants = 0
    for c in message:
        if c.lower() not in ['a', 'e', 'i', 'o', 'u'] and c.isalpha():
            consonants += 1
    serverSocket.sendto(str(consonants).encode(), clientAddress)
    print(f"Sent message: {consonants} to {clientAddress}")
