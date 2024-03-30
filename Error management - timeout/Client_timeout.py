# Description: It receives a message from the client and sends it back after a certain amount of time.
# If the client does not receive the message within a certain amount of time,
# it won't return error, thanks to exception try catch clause.

from socket import *

serverName = 'localhost'
serverPort = 12000

clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.settimeout(1)
message = input('Input sentence: ')
clientSocket.send(message.encode('utf-8'))
try:
    modifiedMessage = clientSocket.recv(2048)
    print(f'Modified message: {modifiedMessage.decode("utf-8")}')
except:
    print('The server is not responding')
finally:
    clientSocket.close()
