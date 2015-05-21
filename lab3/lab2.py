import re

def processit(a):
	prc = ""
	prc = re.sub(r"MX", 1010*"I", a)
	prc = re.sub(r"DX", 510*"I", prc)
	prc = re.sub(r"CX", 110*"I", prc)
	prc = re.sub(r"LX", 60*"I", prc)
	prc = re.sub(r"CM", 900*"I", prc)
	prc = re.sub(r"M", 1000*"I", prc)
	prc = re.sub(r"CD", 400*"I", prc)
	prc = re.sub(r"D", 500*"I", prc)
	prc = re.sub(r"XC", 90*"I", prc)
	prc = re.sub(r"C", 100*"I", prc)
	prc = re.sub(r"XL", 40*"I", prc)
	prc = re.sub(r"L", 50*"I", prc)
	prc = re.sub(r"IX", 9*"I", prc)
	prc = re.sub(r"X", 10*"I", prc)
	prc = re.sub(r"IV", 4*"I", prc)
	prc = re.sub(r"V", 5*"I", prc)
	return prc

def backwardsprocess(a):
	prc = ""
	prc = re.sub(r"I"*1000, "M", a)
	prc = re.sub(r"I"*900, "CM", prc)
	prc = re.sub(r"I"*500, "D", prc)
	prc = re.sub(r"I"*400, "CD", prc)
	prc = re.sub(r"I"*100, "C", prc)
	prc = re.sub(r"I"*90, "XC", prc)
	prc = re.sub(r"I"*50, "L", prc)
	prc = re.sub(r"I"*40, "XL", prc)
	prc = re.sub(r"I"*10, "X", prc)
	prc = re.sub(r"I"*9, "IX", prc)
	prc = re.sub(r"I"*5, "V", prc)
	prc = re.sub(r"I"*4, "IV", prc)
	return prc

def rmath(num1, num2):
	return backwardsprocess(processit(num1) + processit(num2))

def dec_to_rom(dec):
	bla = dec*"I"
	return backwardsprocess(processit(bla))

def rom_to_dec(rom):
	return len(processit(rom))

def romanreplace(rnum):
	k = 0
	result = ""
	tbr = ""
	whosbigger = {"I": 1,"V": 2,"X": 3,"L": 4,"C": 5,"D": 6,"M": 7}
	for a in rnum:
		try:
			if whosbigger.get(a) >= whosbigger.get(rnum[k + 1]):
				result += processit(a)
			else:
				tbr += processit(a)
		except IndexError:
			result += processit(a)
		k += 1
	result = result[len(tbr):]
	return result

def test():
	assert processit("V") == "IIIII"
	assert backwardsprocess("IIIII") == "V"
	assert dec_to_rom(5) == "V"
	assert rom_to_dec("X") == 10
	print "Test passed"
