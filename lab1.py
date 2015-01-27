# -*- coding: latin-1 -*-

#
#  IS-105 LAB1
#
#  lab1.py - kildekode vil inneholde studentenes løsning.
#
#
#


#
#  Oppgave 5
#
#  Tips:
#    For å finne desimalverdien til et tegn kan funksjonen ord brukes, for eksempel
#      ord('A') , det vil gi et tall 65 i ti-tallssystemet
#    For å formattere 6 i ti-tallssystemet til 00000110 i to-tallssystemet
#      '{0:08b}'.format(6)
#      00000110
#
#    Formatteringsstrengen forklart:
#      {} setter en variabel inn i strengen
#      0 tar variabelen i argument posisjon 0
#      : legger til formatteringsmuligheter for denne variabelen (ellers hadde den 6 desimalt)
#      08 formatterer tall til 8 tegn og fuller med nuller til venstre hvis nødvendig
#      b konverterer tallet til dets binære representasjon
#
#	 Hvilke begrensninger vil en slik funksjon ha? (tips: prøv med bokstaven 'å', f.eks.)
#	 Forklar resultatet ascii8Bin('å')
#	 Hvilke faktorer påvirker resultatet? Forklar.
#	 faktor som spiller inn er at å ikke er ascii så den
#	 så den returnerer en string med størrelse 2
#
import sys
import psutil
import platform
import subprocess
# Skriv inn fullt navn på gruppemedlemene (erstatte '-' med navn slikt 'Kari Trå')
gruppe = {  'student1': 'Yngve Olsen Ranestad', \
			'student2': 'Arild Høyland', \
            'student3': 'Steffen Sande', \
            'student5': 'Even Adrian Nilsen', \
            'student6': 'Håkon Dale', \
            'student7': 'Øistein Syversen Fongaard', \
}

print "Gruppemedlemmer:"
# Print alle 'values' i dictionary gruppe
for k, v in gruppe.items():
    print "\t%s" % v

#
#  Oppgave 1
#    Leke med utskrift
#    Skriv ut følgende "ascii art" i en funksjon (erstatte pass)
#    Funksjonen skal hete ascii_fugl() og skal være uten argumenter og uten returverdier
#    Den skal skrive ut følgende når den brukes ascii_fugl
#
#       \/_
#  \,   /( ,/
#   \\\' ///
#    \_ /_/
#    (./
#     '`

print "oppgave 1"

def ascii_bird():
    print """
           \\/_
      \\,   /( ,/
       \\\\\\' ///
        \\_ /_/
        (./
         '`
     """

ascii_bird()
#
#  Oppgave 2
#    bitAnd - x&y
#	 Implementer funksjonen som gjør en "bitwise" AND operasjon (erstatt pass)
#    Eksempel: bitAnd(6, 5) = 4
#		Forklaring: 6 binært er 110, mens 5 er 101. Hvis vi sammenligner bitvis
#					1 AND 1 gir 1, 1 AND 0 gir 0 og 0 AND 1 gir 0 => 100 binært
#					er 4 desimalt. Antagelse: posisjonsbasert tallsystem og
#					den mest signifikante bit-en er lengst til venstre

print "oppgave 2"

def bitAnd(x, y):
	print "%d and %d" %(x, y)
	return x & y

bitandvariabel = bitAnd(6, 5)

print "bitandvariabel = %d" % bitandvariabel

#
#  Oppgave 3
#    bitXor - x^y
#    Eksempel: bitXor(4, 5) = 1
#
print "oppgave 3"
def bitXor(x, y):
	print "%d xor %d" % (x, y)
	return x ^ y

bitxorvariabel = bitXor(4, 5)

print "bitxorvariabel = %d" % bitxorvariabel

#
#  Oppgave 4
#    bitOr - x|y
#    Eksempel: bitOr(0, 1) = 1
#
print "oppgave 4"
def bitOr(x, y):
	print "%d or %d" % (x,y)
	return x | y

bitorvariabel = bitOr(0, 1)

print "bitorvariabel = %d" % bitorvariabel

#
#  Oppgave 5
print "oppgave 5"

#def ascii8Bin(letter):
	#enBin = ord(letter)
	#tilBin = "{0:08b}".format(enBin)
	#print(tilBin)
	#return tilBin

#ascii8Bin('f')

def ascii8Bin(letter):
	enBin = ord(letter)
	tilBin = "{0:08b}".format(enBin)
	#print "%s er %s" % (letter, tilBin)
	return tilBin

shitson = ascii8Bin('a')

print "shitson = %s" % shitson


#
#  Oppgave 6
#    transferBin - ta en tilfeldig streng som argument og skriver ut en blokk av 8-bits strenger
#                  som er den binære representasjon av strengen
#    Eksempel: transferBin("Hi") skriver ut:
#                01001000
#                01101001
#	 Forklart hver linje i denne funksjonen (hva er list, hva gjør in)
#	 Skriv selv inn tester ved å bruke assert i funksjonen test()
#

print "oppgave 6"

def transferBin(string):
	l = list(string)
	for c in l:
		# skriv ut den binære representasjon av hvert tegn (bruk ascii8Bin funksjonen din)
		print "Den binære representasjonen for"
		ascii8Bin(c)
		return ascii8Bin(c)

transferBin("abc")


#
#  Oppgave 7
#    transferHex - gjør det samme som transferBin, bare skriver ut representasjonen
#					av strengen heksadesimalt (bruk formattering forklart i Oppgave 6)
#					Skriv gjerne en støttefunksjon ascii2Hex, som representerer et tegn
#					med 2 heksadesimale tegn
#    Skriv selv inn tester ved å bruke assert i funksjonen test()
#

print "oppgave 7"

def ascii2Hex(letter):
	enHex = ord(letter)
	tilHex = "{0:02X}".format(enHex)
	return tilHex

def transferHex(string):
	l = list(string)
	for c in l:
		print "Den heksadesimale representasjonen for %s" % c
		ascii2Hex(c)
		return ascii2Hex(c)

transferHex("19al")

#
# Oppgave 8
# 		Implementer en funksjon unicodeBin, som kan behandle norske bokstaver
# 		Kravspesifikasjon for denne funksjonen er den samme som for ascii8Bin funksjonen

print "oppgave 8"

def unicodeBin(character):
	enBin = ord(character.decode("utf8"))
	tilBin = "{0:08b}".format(enBin)
	#print "%s er %s" % (letter, tilBin)
	return tilBin

unicodeBin("å")

#
# Oppgave 9
# 	Studer python module psutils (må være obs på versjon)
#   Prøv å finne ut hvordan du kan finne ut og skrive ut følgende informasjon om din
#   datamaskin-node:
#
# 			xBrand and model
# 			*Hard drive capacity
# 			*Amount of RAM
# 			xModel and speed of CPU
# 			xDisplay resolution and size
# 			xOperating system
#
#	Forklar hvorfor man kan / ikke kan finne denne informasjon vha. psutil modulen.
#	Skriv en funksjon printSysInfo som skriver ut den informasjon som psutil kan finne.
#	Kan dere skrive en test for denne funksjonen?
#	Hvilke andre muligheter har man for å finne informasjon om maskinvare i GNU/Linux?
#

print "oppgave 9"

def printSysInfo():
	#Hard drive capacity
	diskUsage = psutil.disk_usage('/')
	print "disk capacity:", diskUsage.total/1000000000, "GB"
	#Amount of RAM
	mem = psutil.virtual_memory()
	print "memory total:", mem.total/1000000, "mb"
	#Model and speed of CPU
	#Display resolution and size
	scrnsize = subprocess.Popen('xrandr | grep "\*" | cut -d" " -f4',shell=True, stdout=subprocess.PIPE).communicate()[0]
	print "your screen resolution:", scrnsize
	#Operating system !using psutil
	pf = platform.platform()
	print "your platform:", pf

printSysInfo()
print "{0:08b}".format('c3 a5')
unicodeBin('å')

def test():
	#assert bitAnd(6, 5) == 4
	#assert bitXor(4, 5) == 1
	#assert bitOr(0, 1) == 1
	#assert ascii8Bin('a') == '01100001'
	#assert ascii8Bin('A') == '01000001'
	#assert transferBin('a') == '01100001'
	#assert transferHex("1") == '31'
	assert unicodeBin('å') == '11100101'
	# Dine egne tester
	return "Testene er fullført uten feil."


# Bruk denne funksjonen for å vise at alle testene er kjørt feilfritt
#print test()
