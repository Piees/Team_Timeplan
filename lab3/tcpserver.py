#!/usr/bin/env python
# -*- coding: utf-8 -*-

import lab2
import bs
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
		print prcd
		svar = lab2.rmath(prcd[0], prcd[1])
		connectionSocket.send(svar)
	elif prcd[len(prcd) - 1] == 'uni':
		bode = ''.join(received)
		bode = bode.replace(' uni', '')
		svar = bs.flips(bode)
		#svar = bode.decode('utf-8').upper().encode('utf-8')
		connectionSocket.send(svar)
		#print svar
	elif prcd == "invalid valuez":
		print "invalid valuez"
		connectionSocket.close()
connectionSocket.close()
