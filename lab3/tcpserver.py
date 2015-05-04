#!/usr/bin/env python
# -*- coding: utf-8 -*-

import lab2
from basecode import flips
from socket import *
serverPort = 12000
serverSocket = socket(AF_INET,SOCK_STREAM)
serverSocket.bind(('',serverPort))
serverSocket.listen(1)
print 'The server is ready to receive'
while 1:
	connectionSocket, addr = serverSocket.accept()
	received = connectionSocket.recv(1024)
	prcd = received.split(' ')
	toproc = str(prcd.pop)
	svar = ''
	if prcd[len(prcd) - 1] == 'roman':
		svar = lab2.romanmath(prcd[0], prcd[1], prcd[2])
		connectionSocket.send(svar)
	elif prcd[len(prcd) - 1] == 'uni':
		bode = ''.join(received)
		bode = bode.replace('uni', '')
		#print bode
		svar = ''
		#svar = bode.decode('utf-8').upper().encode('utf-8')
		connectionSocket.send(svar)
		#print svar
connectionSocket.close()
