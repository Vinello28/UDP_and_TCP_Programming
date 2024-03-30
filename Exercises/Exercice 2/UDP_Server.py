# Description: UDP Server that receives a number from a client and sends back to the client
# if the number is prime or not.

from socket import *


def is_prime(n):
    if n < 2:
        return False
    if n % 2 == 0:
        return False
    return True

serverPort = 12000
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(('', serverPort))
print("The server is ready to receive")

while True:
    message, clientAddress = serverSocket.recvfrom(2048)
    number = int(message.decode())
    print(f"Received number: {number}")
    if is_prime(number):
        response = "The number is prime"
    else:
        response = "The number is not prime"
    serverSocket.sendto(response.encode(), clientAddress)
    print(f"Sent response: {response} to {clientAddress}")