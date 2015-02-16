
def bit_or(x, y):
    return x | y

def bit_xor(x, y):
    return x ^ y

def uni_bin(ch):
    utf_ba = bytearray(format(ch))
    uba = []
    for n in range(len(format(ch))):
        uni_bin = '{0:08b}'.format(utf_ba[n])
        uba.append(int(uni_bin))
    return uba

def uni_xor(ch):
    utf_ba = bytearray(format(ch))
    uba = uni_bin(ch)
    print uba

