Sure, here is the README file with the appropriate markdown formatting:

```markdown
# Foundamentals of Communications and Internet Laboratory Exercises

This repository contains the laboratory exercises for the course "Foundamentals of Communications and Internet". The exercises are implemented in Python and cover various topics related to networking and communication protocols.

## Repository Structure

The repository is organized into two main directories:

1. `Basics of Socket Programming`: This directory contains basic examples of client-server applications using TCP/IP and UDP protocols.

2. `Exercises`: This directory contains the exercises from the laboratory course. Each exercise is placed in its own subdirectory.

## Files Description

- `Basics of Socket Programming/ClientApp.py`: A simple client application that uses socket programming to establish a TCP/IP connection with a server. It sends a user-inputted message to the server and receives a response, which is then printed to the console.

- `Basics of Socket Programming/ServerDeamon.py`: A simple server application that uses socket programming to listen for incoming TCP/IP connections. It receives a message from a client, modifies it, and sends it back to the client.

- `Exercises/Exercice 2/UDP_Server.py`: A UDP Server that receives a number from a client and sends back to the client if the number is prime or not.

- `Exercises/Exercice 2/UDP_Client.py`: A UDP Client that sends a number to a server and receives back if the number is prime or not.

- `Basics of TCP sockets/Server.py`: A TCP server that receives a message from a client, modifies it by converting it to uppercase, and sends it back to the client.

- `Basics of TCP sockets/Client.py`: A TCP client that sends a message to a server and receives back the modified message.

## Running the Code

To run the code, navigate to the directory of the file and run the python script. For example, to run the `ClientApp.py` script, use the following command:

```bash
python3 ClientApp.py
```

Please note that you need to have Python 3.12 installed on your machine to run the scripts.

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License

[MIT](https://choosealicense.com/licenses/mit/)
```
