#!/usr/bin/env python
# -*- coding: utf-8 -*-

import lab2
from basecode_w_bugs import flips
from socket import *
serverPort = 12000
serverSocket = socket(AF_INET,SOCK_STREAM)
#serverSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
serverSocket.bind(('',serverPort))
serverSocket.listen(1)
print 'The server is ready to receive'
while 1:
    connectionSocket, addr = serverSocket.accept()
    received = connectionSocket.recv(1024)
    #capitalizedletter = letter.upper()
    prcd = received.split(' ')
    toproc = str(prcd.pop)
    svar = ''
    if prcd[len(prcd) - 1] == 'roman':
        print "EUREKA!!"
        svar = lab2.romanmath(prcd[0], prcd[1], prcd[2])
        connectionSocket.send(svar)
    elif prcd[len(prcd) - 1] == 'uni':
        print "dickbutt"
        bode = ''.join(received)
        bode = bode.replace('uni', '')
        print bode
        svar = bode.decode('utf-8').upper().encode('utf-8')
        #svar = flips(bode) denne er work in progress
        connectionSocket.send(svar)
        print svar
    else:
        print "you suck "
        print "received " + received
        print toproc
        print "svar " + svar
        svar = lab2.romanmath(prcd[0], prcd[1], prcd[2])
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
    #connectionSocket.send(svar)
    connectionSocket.close()
