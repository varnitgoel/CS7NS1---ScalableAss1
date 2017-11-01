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