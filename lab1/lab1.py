# -*- coding: latin-1 -*-

#
#  IS-105 LAB1
#
#  lab1.py - kildekode vil inneholde studentenes løsning.
#
#
#
import sys
import psutil
import subprocess
import platform

# Skriv inn fullt navn på gruppemedlemene (erstatte '-' med navn slikt 'Kari Trå')
gruppe = {  'student1': 'Yngve Olsen Ranestad', \
			'student2': 'Arild Høyland', \
			'student3': 'Steffen Sande', \
			'student4': 'Håkon Gilje', \
			'student5': 'Even Adrian Nilsen', \
			'student6': 'Håkon Dale', \
			'student7': 'Øistein Syversen Fongaard', \
}

print "Gruppemedlemmer:"
# Print alle 'values' i dictionary gruppe
for key, value in gruppe.items():
	print "\t%s" % value

#
#  Oppgave 1
#    Leke med utskrift
#    Skriv ut følgende "ascii art" i en funksjon (erstatte pass)
#    Funksjonen skal hete ascii_fugl() og skal være uten argumenter og uten returverdier
#    Den skal skrive ut følgende når den brukes ascii_fugl
#

# Vi gjør dette med print raw så vi slipper escapes
def ascii_bird():
	print r"       \/_"
	print r"  \,   /( ,/"
	print r"   \\\' ///"
	print r"    \_ /_/"
	print r"    (./"
	print r"     '`"

print "\nOppgave 1\n"

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
def bitAnd(x, y):
	return x & y

#
#  Oppgave 3
#    bitXor - x^y
#    Eksempel: bitXor(4, 5) = 1
#
def bitXor(x, y):
	return x ^ y

#
#  Oppgave 4
#    bitOr - x|y
#    Eksempel: bitOr(0, 1) = 1
#
def bitOr(x, y):
	return x | y
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
def ascii8Bin(letter):
	enBin = ord(letter)
	return "{0:08b}".format(enBin)

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

# skrive print før metoden for å få printet returverdien på hver linje
def transferBin(string):
	binlist = [] #opprett en liste
	l = list(string) #lag en liste av parameter i metoden
	for c in l: #en for-løkke
		binlist.append(ascii8Bin(c)) #legg til hvert returnerte i liste binlist
	binlist = "\n".join(binlist) #gjør lista om til en streng med newlines
	return binlist

#
#  Oppgave 7
#    transferHex - gjør det samme som transferBin, bare skriver ut representasjonen
#					av strengen heksadesimalt (bruk formattering forklart i Oppgave 6)
#					Skriv gjerne en støttefunksjon ascii2Hex, som representerer et tegn
#					med 2 heksadesimale tegn
#    Skriv selv inn tester ved å bruke assert i funksjonen test()
#
def ascii2_hex(letter):
	ascii_letter = ord(letter)
	return "{0:2x}".format(ascii_letter)

def transferHex(string):
	ascil= []
	l = list(string)
	for c in l:
		ascil.append(ascii2_hex(c))
	ascil = "\n".join(ascil)
	return ascil

#
# Oppgave 8
# 		Implementer en funksjon unicodeBin, som kan behandle norske bokstaver
# 		Kravspesifikasjon for denne funksjonen er den samme som for ascii8Bin funksjonen
def unicodeBin(character):
	utf8_byte_array = bytearray(character)
	uba = []
	# Itererer gjennom det formaterte unicodesymbolet
	for n in range(len(character)):
		# Legger den binære versjonen av symbolet i en liste
		uba.append("{0:08b}".format(utf8_byte_array[n]))
		# Konverterer listen til en string bestående av den binære koden til
		# symbolet
		uni_bin = ' '.join(uba)
	return uni_bin

#
# Oppgave 9
# 	Studer python module psutils (må være obs på versjon)
#   Prøv å finne ut hvordan du kan finne ut og skrive ut følgende informasjon om din
#   datamaskin-node:
#
# 			Brand and model
# 			Hard drive capacity
# 			Amount of RAM
# 			Model and speed of CPU
# 			Display resolution and size
# 			Operating system
#
#	Forklar hvorfor man kan / ikke kan finne denne informasjon vha. psutil modulen.
#		-
#	Skriv en funksjon printSysInfo som skriver ut den informasjon som psutil kan finne.
#	Kan dere skrive en test for denne funksjonen?
#	Hvilke andre muligheter har man for å finne informasjon om maskinvare i GNU/Linux?
#
def printSysInfo():
	#Hard drive capacity
	diskUsage = psutil.disk_usage('/')
	print "Disk capacity:", diskUsage.total/1000000000, "GB"
	#Amount of RAM
	mem = psutil.virtual_memory()
	print "Memory total:", mem.total/1000000, "mb"
	#Model and speed of CPU
	with open('/proc/cpuinfo') as f:
		cores = 0
		for line in f:
			if "model name" in line:
				mname = line.replace('	', '') #replace tab with nothing
				cores += 1
		print mname.strip('\n')
		print "number of cores: " + str(cores)
	#Display resolution and size
	scrnsize = subprocess.Popen('xrandr | grep "\*" | cut -d" " -f4',shell=True, stdout=subprocess.PIPE).communicate()[0]
	print "Your screen resolution:", scrnsize.strip('\n')
	#Operating system !using psutil
	pf = platform.platform()
	print "Your platform:", pf

printSysInfo()

def test():
	assert bitAnd(6, 5) == 4
	assert bitXor(4, 5) == 1
	assert bitOr(0, 1) == 1
	assert ascii8Bin('a') == '01100001'
	assert ascii8Bin('A') == '01000001'
	# Skriv her inn passende tester for tarnsferBin og transferHex funksjoner
	# fra oppgavene 6 og 7
	assert ascii2_hex('a') == '61'
	assert ascii2_hex('A') == '41'
	assert transferHex('aA') == '61\n41'
	assert unicodeBin('å') == '11000011 10100101'
	# Dine egne tester
	return "Tests completed."

print test()
# Bruk denne funksjonen for å vise at alle testene er kjørt feilfritt
