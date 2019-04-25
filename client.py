import socket
sd=socket.socket()
addr=socket.gethostname()

port=15001

sd.connect((addr,port))

msg = sd.recv(1024)
print(str(msg))
sd.close()