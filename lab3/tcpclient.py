#!/usr/bin/env python
# -*- coding: utf-8 -*-

from socket import *
serverName = '127.0.0.1'
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName,serverPort))
letter = raw_input("Type and we'll switch for you: ")
clientSocket.send(letter)
modifiedSentence = clientSocket.recv(1024)
print 'From Server:', modifiedSentence
clientSocket.close()
