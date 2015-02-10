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
