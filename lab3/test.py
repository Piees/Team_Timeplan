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
'''

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
