# -*- coding: utf-8 -*-

def flipbit(var):
	ba = ' '.join(format(x, 'b') for x in bytearray(var))
	#bb = '0'+ba
	bb = ba
	splitba = bb.split(' ')
	flippedarray = []
	if len(splitba) == 2:
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
		return flippedarray
	else:
		placeholder = '0'
		if bb[2] == '0':
			placeholder = bb[:2] + '1' + bb[3:]
		else:
			placeholder = bb[:2] + '0' + bb[3:]
		return placeholder


def flips(letter):
	flipped = flipbit(letter)
	strflipped = ' '.join(flipped)
	svar = ''
	if len(flipped) == 2:
		a = flipped[0]
		b = flipped[1]
		unia = chr(int(a.decode("utf-8"),2))
		unib = chr(int(b.decode("utf-8"),2))
		unified = unia + unib
		svar = unified
	else:
		svar = chr(int(str(flipped),2))
	return svar

def test():
	assert flipbit('ԁ') == ['11010100', '10000000']
	assert flipbit('æ') == ['11000011', '10000110']
	assert flips('æ') == '\xc3\x86' #big æ value in hex
	print "The tests were successful."
