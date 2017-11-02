# -*- coding: utf-8 -*-
"""
Created on Wed Nov  1 14:43:30 2017

@author: Varnit Goel
"""
def discon():
	clThread.exit()

def leave(conn_msg,csock):
	grp_start = conn_msg.find('LEAVE_CHATROOM:'.encode('utf-8')) + 15
	grp_end = conn_msg.find('\n'.encode('utf-8'), grp_start) - 1

	group_name = conn_msg[grp_start:grp_end]

	response = "LEFT_CHATROOM".encode('utf-8') + groupname + "\n".encode('utf-8')
	response += "JOIN_ID".encode('utf-8') + str(clThread.uid).encode('utf-8')

	grpmessage = "CLIENT_NAME:".encode('utf-8') + (self.clientname).encode('utf-8') + "\n".encode('utf-8')
	grpmessage += "CLIENT_ID:".encode('utf-8') + str(self.uid).encode('utf-8') +"\n".encode('utf-8')
	grpmessage += "LEFT GROUP".encode('utf-8')
	if group_name == g1:
		g1_clients.remove(self.clientname)
		for x in g1_clients:
			(g1_clients[x].socket).send(chat_text)
	elif group_name == g2:
		g2_clients.remove(self.clientname)
		for x in g2_clients:
			(g2_clients[x].socket).send(chat_text)
	csock.send(response)
	

def chat(conn_msg,csock):
	chat_msg_start = conn_msg.find('MESSAGE:'.encode('utf-8')) + 9
	chat_msg_end = conn_msg.find('\n\n'.encode('utf-8'),chat_msg_start) - 1	

	chat_msg = conn_msg[chat_msg_start:chat_msg_end]

	grp_start = conn_msg.find('CHAT:'.encode('utf-8')) + 5
	grp_end = conn_msg.find('\n'.encode('utf-8'), grp_start) - 1

	group_name = conn_msg[grp_start:grp_end]
	
	chat_text = 'CHAT:'.encode('utf-8') + chat_msg + '\n'.encode('utf-8')			##change to Room number
	chat_text += 'CLIENT_NAME:'.encode('utf-8') +str(clThread.clientid).encode('utf-8')
	chat_text += 'MESSAGE: ' + chat_msg.encode('utf-8') 
	
	if group_name == g1:
		for x in g1_clients:
			(g1_clients[x].socket).send(chat_text)
	elif group_name == g2:
		for x in g2_clients:
			(g2_clients[x].socket).send(chat_text)
            