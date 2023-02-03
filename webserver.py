#import socket module
from socket import *
import sys # In order to terminate the program 
serverSocket = socket(AF_INET, SOCK_STREAM)

# Prepate a server socket
# Fill in start
serverIP = '127.0.0.1'
serverPort = 12000
serverSocket.bind((serverIP, serverPort))
serverSocket.listen(1)
# Fill in end

while True:
	# Establish the connection
	print("The server is ready to recieve")
	connectionSocket, addr = serverSocket.accept() # Fill in start	# Fill in end
	print(f">> Connection from {str(addr)}")

	try:
		message = connectionSocket.recv(1024).decode() # Fill in start	# Fill in end
		filename = message.split()[1]
		f = open(filename[1:])
		print(f">> Opening File: {filename}")
		outputdata = f.readlines() # Fill in start	# Fill in end
		f.close()

		# Send HTTPS header lines into serverSocket
		# Fill in start
		connectionSocket.send("HTTP/ 1.1 200 OK\r\nHelloWorld\r\n".encode())
		connectionSocket.send("\r\n".encode())
		# Fill in end

		# Send the content of the requested file to the client
		# Fill in start
		for i in range(len(outputdata)):
			connectionSocket.send(outputdata[i].encode())
		connectionSocket.send("\r\n".encode())
		# Fill in end

		# Close the connectionn with this particular client
		connectionSocket.close()

	except IOError:
		# Send response message for file not found
		# Fill in start
		print(">> Error 404: Page Not Found")
		connectionSocket.send("HTTP/ 1.1 404 Not Found\r\n".encode())
		connectionSocket.send("\r\n".encode())
		connectionSocket.send(f"<HTML><head></head><body><h1>Error 404: Page Not Found!</h1><h2>Please continue to <a href='{serverIP}:{serverPort}/HelloWorld.html'>HelloWorld</a></h2></body></HTML>\r\n".encode())
		# Fill in end
		# Close client socket
		# Fill in start
		connectionSocket.close()
		# Fill in end
	serverSocket.close()
	sys.exit() # Terminate the program after sending the corresponding data