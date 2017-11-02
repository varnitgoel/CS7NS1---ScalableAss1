# -*- coding: utf-8 -*-
"""
Created on Wed Nov  1 14:43:30 2017

@author: Varnit Goel
"""
class client_threads(Thread):

	def __init__(self,ip,port,socket):
		Thread.__init__(self)
		self.ip = ip
		self.port = port
		self.chatroom =[] 
		self.socket = socket
		self.uid = random.randint(1000,2000)
		self.roomname = ''
		self.clientname = ''

	def run(self):
		while True:
			conn_msg = csock.recv(1024)
			cflag = check_msg(conn_msg)
			print('Connected')
			if cflag == 1 :
				 print('joining')
				 self.roomname,self.clientname = join(conn_msg,csock)
			elif cflag == 2 : leave(conn_msg,csock)
			elif cflag == 3 : discon(csock)
			elif cflag == 4 : chat()
			else : pass					 #error code for incorrect message	
			print(self.clientname)
			self.chatroom.append(self.roomname)
			print('roomnames')
			print(self.chatroom)