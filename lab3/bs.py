# -*- coding: utf-8 -*-

def flipbit(var):
	ba = ' '.join(format(x, 'b') for x in bytearray(var))
	#bb = '0'+ba
	bb = ba
	splitba = bb.split(' ')
	flippedarray = []
	while splitba != []:
		if len(splitba[0]) == 8 and splitba[0][:3] == '110':
			prefix = splitba[0]
			suffix = splitba[1]
			placeholder = '0'
			if prefix == '11000011': # latin simple, no accent
				if suffix[2] == '0':
					placeholder = suffix[:2] + '1' + suffix[3:]
				else:
					placeholder = suffix[:2] + '0' + suffix[3:]
			elif prefix == '11010100': #cyrillic, no accent
				if suffix[7] == '0':
					placeholder = suffix[:7] + '1'
				else:
					placeholder = suffix[:7] + '0'
			flippedarray.append(prefix)
			flippedarray.append(placeholder)
			splitba.pop(0)
			splitba.pop(0)
		elif len(splitba[0]) == 7:
			bb = '0' + splitba[0]
			placeholder = ''
			if bb[2] == '0':
				placeholder = bb[:2] + '1' + bb[3:]
			else:
				placeholder = bb[:2] + '0' + bb[3:]
			splitba.pop(0)
			flippedarray.append(placeholder)
		else:
			return "iv"
	return flippedarray


def flips(letter):
	flipped = flipbit(letter)
	#strflipped = ' '.join(flipped)
	svar = ''
	while flipped != []:
		if flipped[0][:3] == '110':
			a = flipped[0]
			b = flipped[1]
			unia = chr(int(a.decode("utf-8"),2))
			unib = chr(int(b.decode("utf-8"),2))
			unified = unia + unib
			svar += unified
			flipped.pop(0)
			flipped.pop(0)
		elif flipped[0][:2] == '01':
			#svar = chr(int(str(flipped),2))
			svar += chr(int(flipped[0].decode("utf-8"),2))
			flipped.pop(0)
		elif flipped == "iv":
			return "Invalid value"
	return svar


def test():
	assert flipbit('ԁ') == ['11010100', '10000000']
	assert flipbit('æ') == ['11000011', '10000110']
	assert flips('æ') == '\xc3\x86' #big æ value in hex
	print "The tests were successful."
