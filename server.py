import socket

sd=socket.socket()
addr = socket.gethostname()

port = 15001
sd.bind((addr,port))

sd.listen(5)


while True:
	AccSock,clientAddress = sd.accept()
	print(str(clientAddress))
	AccSock.send(b'Thanks for calling'+str.encode(str(clientAddress)))
	AccSock.close()
	