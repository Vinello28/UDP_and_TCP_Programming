# Description: UDP Client that sends a number to a server and receives back if the number is prime or not.

from socket import *

serverName = 'localhost'
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_DGRAM)

number = input("Enter a number: ")
clientSocket.sendto(number.encode(), (serverName, serverPort))
response, serverAddress = clientSocket.recvfrom(2048)
print(response.decode())
clientSocket.close()
