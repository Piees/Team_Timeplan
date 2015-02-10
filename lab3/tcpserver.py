from socket import *
serverPort = 12000
serverSocket = socket(AF_INET,SOCK_STREAM)
serverSocket.bind(('',serverPort))
serverSocket.listen(1)
print 'THe server is ready to receive'
while 1:
    connectionSocket, addr = serverSocket.accept()
    sentence = connectionSocket.recv(1024)
    #capitalizedSentence = sentence.upper()
    def unicodeBin(character):
        utf8_byte_array = bytearray(format(character))
        print utf8_byte_array
        uba = []
        for n in range(len(format(character))):
            print utf8_byte_array[n]
            uba.append("{0:08b}".format(utf8_byte_array[n]))
            uni_bin = ' '.join(uba)
        int(uni_bin[13]) ^ 1
        return uni_bin
    connectionSocket.send(unicodeBin(sentence))
    connectionSocket.close()
