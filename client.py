#Client for Multiple Client ChatServer

import sys, os
import socket
from threading import Thread

def join():
    chatroom = input('Enter Room name to proceed: ')

    conn_msg = "JOIN_ROOM:".encode('utf-8') + chatroom.encode('utf-8') + "\n".encode('utf-8')
    conn_msg += "CLIENT IP: \n".encode('utf-8')
    conn_msg += "PORT: \n".encode('utf-8')
    conn_msg += "CLIENT_NAME:".encode('utf-8') + client_name.encode('utf-8') + "\n".encode('utf-8')
    s.send(conn_msg)

def chat(socket):
    chat_room = input('Which room?: ')
    chat_message = input('Enter message to send: ')
    msg = "CHAT: ".encode('utf-8') + chat_room.encode('utf-8') + "\n".encode('utf-8')
    msg += "JOIN_ID: ".encode('utf-8') + str(jID).encode('utf-8') + "\n".encode('utf-8')
    msg += "CLIENT_NAME: ".encode('utf-8') + client_name.encode('utf-8') + "\n".encode('utf-8')
    msg += "MESSAGE: ".encode('utf-8') + chat_message.encode('utf-8') + "\n\n".encode('utf-8')
    socket.send(msg)

def leave(s):
    rTL = input('Room to Leave ')
    msg = "LEAVE_CHATROOM: ".encode('utf-8') + rTL.encode('utf-8') + "\n".encode('utf-8')
    msg += "JOIN_ID: ".encode('utf-8') + jID.encode('utf-8') + "\n".encode('utf-8')
    msg += "CLIENT_NAME: ".encode('utf-8') + client_name.encode('utf-8')
    s.send(msg)

def discon():
    msg = "DISCONNECT: \n".encode('utf-8')
    msg += "PORT: \n".encode('utf-8')
    msg += "CLIENT_NAME: ".encode('utf-8') + client_name.encode('utf-8') + "\n".encode('utf-8')
    s.send(msg)

    s.close()
    os._exit(1)

class Client(Thread):
    def __init__(self, socket):
        Thread.__init__(self)
        self.socket = socket
        print('Listening to server')

    def run(self):
        while True:
            data = self.socket.recv(1024)
            print('Message from Client: ')
            print(data.decode(encoding='utf-8'))

#Create socket object
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#Get name of local machine 
host = input('Enter Hostname: ')
port = input('Input Port no: ')

# connection to hostname on the port. 
s.connect((host, int(port)))

#Test response from the server
test_send = "HELO text \n".encode('utf-8')
s.send(test_send)
print(s.recv(1024))

client_name = input('Client Name: ')
join()
jID = 0
data = s.recv(1024)
print(data.decode(encoding='utf-8'))
p = data.find(b'JOINED')
if p == 0:
    jID_start = data.find('JOIN_ID'.encode('utf-8')) + 9
    jID_end = data.find('\n'.encode('utf-8'), jID_start) - 1
    jID = str(data[jID_start:jID_end])

serverThread = Client(s)
serverThread.start()

while (1):
    print('Enter your choice:')
    print('1. Connect')
    print('2. Talk/Chat')
    print('3. Leave')
    print('4. Disconnect')
    task = input('')
    if task == '1':
        join()
    elif task == '2':
        print('Chatting')
        chat(s)
    elif task == '3':
        leave(s)
    elif task == '4':
        discon()
    elif task == '5':
        print('Invalid Option')