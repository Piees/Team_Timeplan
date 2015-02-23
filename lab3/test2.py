#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
def unic(character):
    utf8_byte_array = bytearray(format(character))
    uba = []
    # Itererer gjennom det formaterte unicodesymbolet
    for n in range(len(format(character))):
        uba.append("{0:08b}".format(utf8_byte_array[n]))
        # symbolet
        if n == 1:
            uba[1] = str(uba[1]).replace("101", "100", 1)
        uni_bin = ' '.join(str(uba))
    return uni_bin

def ascii8Bin(letter):
    enBin = ord(letter)
    return "{0:08b}".format(enBin)

def flip(var):
    if var[2] == '0':
        a = var[:2] + '1' + var[4:]
    else:
        a = var[:2] + '0' + var[4:]

def unic(character):
    utf8_byte_array = bytearray(format(character))
    uba = []
    # Itererer gjennom det formaterte unicodesymbolet
    for n in range(len(format(character))):
        uba.append("{0:08b}".format(utf8_byte_array[n]))
        # symbolet
        if len(utf8_byte_array) == 1:
            type(utf8_byte_array)
            #print "unibin: ", uni_bin
            pre_bin = int(utf8_byte_array, 2)
            uni_bin = pre_bin[:2] + '0' + pre_bin[3:]
            #uni_bin = uni_bin[3] ^ 00100000
        if n == 1:
            uba[1] = str(uba[1]).replace("101", "100", 1)
        uni_bin = ' '.join(str(uba))
    return uni_bin

 ##DETTE ER KODEN VI PRooVER aa Faa FLIPPA BIN NUMMER FOR aa Faa CAPSLOCK
def unicodeBin(character):
    utf8_byte_array = bytearray(format(character))
    uba = []
    # Itererer gjennom det formaterte unicodesymbolet
    for n in range(len(format(character))):
        # Legger den binære versjonen av symbolet i en liste
        uba.append("{0:08b}".format(utf8_byte_array[n]))
        # Konverterer listen til en string bestående av den binære koden til
        # symbolet
        uni_bin = ' '.join(uba)
    return uni_bin
'''

def flip(var):
    a = ''
    print "var er: " + var
    #calc = '0' + var
    calc = var.replace('b', '')
    if len(calc) == 7:
        pass
    if calc[2] == '0':
        a = calc[:2] + '1' + calc[3:]
    else:
        a = calc[:2] + '0' + calc[3:]
    return a
inbin = []
sentence = 'å'
swtc = False
def uni():
    for n in sentence:
        print "n er: " + n
        if unicodeBin(n) == '11000011':
            print "funker dette?"
            swtc = True
        elif swtc == True:
            inbin.append('11000011 ' + flip(bin(ord(n))))
            print "inbin er: " + inbin
        else:
            inbin.append(flip(bin(ord(n))))
            swtc = False
        print inbin
    for x in range(len(inbin)):
        print chr(int(inbin[x], 2))
