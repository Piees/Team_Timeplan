#!/usr/bin/env python
# -*- coding: utf-8 -*-

from socket import *
serverName = '127.0.0.1'
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName,serverPort))
print "What'ya wanna do mon?"
wtd = raw_input("1 for roman math, 2 for caps lockifying\n")
switch = 1
while switch == 1:
	if wtd == '1':
		letter = raw_input("Type: <first number> <operator> <second number> with spaces\n")
		romansend = letter.split(' ')
		romaninf = letter + ' roman'
		clientSocket.send(romaninf)
		break
	elif wtd == '2':
		unisend = raw_input("What do you want caps lockified?\n")
		uniinf = unisend + ' uni'
		clientSocket.send(uniinf)
		break
	else:
		print "Try typing 1 or 2"
		wtd = raw_input("1 for roman math, 2 for caps lockifying\n")
modifiedSentence = clientSocket.recv(1024)
print 'From Server:', modifiedSentence
clientSocket.close()
