from socket import *


def isPrime(n):
    if n == 2 or n == 0:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


serverPort = 12000
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(('', serverPort))
print('The server is ready to receive')

while True:
    message, clientAddress = serverSocket.recvfrom(2048)
    message = int(message.decode('utf-8'))
    if isPrime(message):
        serverSocket.sendto('The number is prime'.encode('utf-8'), clientAddress)
    else:
        serverSocket.sendto('The number is not prime'.encode('utf-8'), clientAddress)
    serverSocket.close()
