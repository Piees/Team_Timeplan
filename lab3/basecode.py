letter = raw_input('Type 1 letter: ')

def flipbit(var):
    ba = ' '.join(format(x, 'b') for x in bytearray(var))
    bb = '0'+ba
    splitba = bb.split(' ')
    flippedarray = []
    #print ba
    if len(splitba) == 2:
        #print "16bit"
        #print len(splitba)
        prefix = splitba[0]
        suffix = splitba[1]
        placeholder = '0'
        if suffix[2] == '0':
            placeholder = suffix[:2] + '1' + suffix[3:]
        else:
            placeholder = suffix[:2] + '0' + suffix[3:]
        flippedarray.append(prefix)
        flippedarray.append(placeholder)
        return flippedarray
    else:
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
