# -*- coding: utf-8 -*-
"""
Created on Wed Nov  1 14:43:30 2017

@author: Varnit Goel
"""
#testing 1
import socket

#creating socket object 
s=socket.socket()
host=socket.gethostname()
print(host)
port=12221

s.bind((host,port))

s.listen(7)

while TRUE:
    c,adrs=s.accept()
    print("got connceted from %s", +str(adrs))
    
    response="welcome to the chatroom"
    c.send(response.encode('ascii'))
    c.close() 
    




server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostname()
port = 50000
server.bind((host,port))
print(host)
thread_count = []

g1_clients = []
g2_clients = []


while True:
        server.listen(4)
        (csock,(ip,port)) = server.accept()

        print("Connected to ",port,ip)
        #monitoring connections

        clThread = client_threads(ip,port,csock)
        clThread.start()
        thread_count.append(clThread)
        print("Threads :")
        print(thread_count)
        print(g1_clients)