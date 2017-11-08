def discon():
	msg = "DISCONNECT: \n".encode('utf-8') 
	msg += "PORT: \n".encode('utf-8')
	msg += "CLIENT_NAME: ".encode('utf-8') + Cname.encode('utf-8') + "\n".encode('utf-8')
	s.send(msg)
	
	s.close()
	os._exit(1)


class Client(Thread):
	def __init__(self,socket):
		Thread.__init__(self)
		self.socket = socket
		print('Listening to server')

	def run(self):
		while True:
			data = self.socket.recv(1024)
			print('Message from Client: ')
			print(data.decode(encoding='utf-8'))