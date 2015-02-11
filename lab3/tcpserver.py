#!/usr/bin/env python
# -*- coding: utf-8 -*-

import lab2
from socket import *
serverPort = 12000
serverSocket = socket(AF_INET,SOCK_STREAM)
serverSocket.bind(('',serverPort))
serverSocket.listen(1)
print 'The server is ready to receive'
svar = ''
while 1:
    connectionSocket, addr = serverSocket.accept()
    received = connectionSocket.recv(1024)
    #capitalizedletter = letter.upper()
    if received[1] == 'roman':
        svar = lab2.romanmath(received[0][0], received[0][1], received[0][2])
    elif received[1] == 'uni':
        print 'tbd'
    else:
        print "you suck"
    '''
    def flipbit(var): #hovedmetode
        ba = ' '.join(format(x, 'b') for x in bytearray(var)) #håndterer input
        bb = '0'+ba #fixer cutout av 0 før b
        splitba = bb.split(' ') #lager liste om det er space
        flippedarray = []
        #print ba
        if len(splitba) == 2: #hvis splitba lista er 2(bytes)
            #print "16bit"
            #print len(splitba)
            prefix = splitba[0]
            suffix = splitba[1]
            placeholder = '0'
            if suffix[2] == '0': #sjekker om 3 i string er 0
                placeholder = suffix[:2] + '1' + suffix[3:]
            else:
                placeholder = suffix[:2] + '0' + suffix[3:]
            flippedarray.append(prefix)
            flippedarray.append(placeholder)
            return flippedarray
        else: #om det ikke er 2 bytes
            #print "8bit"
            placeholder = '0'
            if bb[2] == '0':
                #print bb
                placeholder = bb[:2] + '1' + bb[3:]
            else:
                placeholder = bb[:2] + '0' + bb[3:]
            return placeholder
    flipped = flipbit(letter)
    strflipped = ' '.join(flipped)
    #print flipped
    svar = ''
    if len(flipped) == 2:
        a = flipped[0]
        b = flipped[1]
        unia = chr(int(a.decode("utf-8"),2))
        unib = chr(int(b.decode("utf-8"),2))
        unified = unia + unib
        svar = unified.decode("utf-8")
    else:
        svar = chr(int(str(flipped),2))
    print svar
    '''
    connectionSocket.send(svar)
    connectionSocket.close()
