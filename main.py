# -*- coding: utf-8 -*-
"""
Created on Wed Nov  1 18:04:20 2017

@author: Varnit Goel
"""

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