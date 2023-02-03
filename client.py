#import socket module
from socket import *
import sys # In order to terminate the program 
clientSocket = socket(AF_INET, SOCK_STREAM)

if len(sys.argv) != 4:
    print(len(sys.argv))
    print(">> Incorrect Command. Use Command:'client.py server_host server_port filename'")
    sys.exit()

# Prepare a client socket and establish connection
serverIP = str(sys.argv[1]) # '127.0.0.1'
clientPort = int(sys.argv[2]) # 12000
filePath = str(sys.argv[3])

clientSocket.connect((serverIP,clientPort))

while True:

	try:
		# message = input("Enter filename: ")
		message = f"GET /{filePath}.html HTTP/1.1" # HTTP/1.1
		clientSocket.send(message.encode())

		recvMessage = clientSocket.recv(1024).decode()
		while(recvMessage):
			print(f"Response from Server: {recvMessage}")
			# sendMessage = clientSocket.send(f"recvMessage: {recvMessage}")
			recvMessage = clientSocket.recv(1024).decode()

		# Close the connectionn with this particular client
		clientSocket.close()

	finally:
		clientSocket.close()
		sys.exit() # Terminate the program after sending the corresponding data