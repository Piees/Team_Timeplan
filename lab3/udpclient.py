#!/usr/bin/env python
# -*- coding: utf-8 -*-

from socket import *
serverName = '127.0.0.1'
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_DGRAM)
letter = raw_input('Input lowercase sentence:')
clientSocket.sendto(letter,(serverName, serverPort))
modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
print modifiedMessage

clientSocket.close()
