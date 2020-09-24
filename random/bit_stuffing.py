def bit_stuffing(bit_string):
    knt = 0
    for i in range( len(bits_string)-5 ):
        if bit_string[i:i+5] == '11111':
            bit_string = bit_string[:i+5] + '0' + bit_string[i+5:]
            knt += 1
    print('bits added: {}'.format(knt))

    return bit_string

def de_stuffing(bit_string):
    knt = 0
    for i in range(len(bits_string) - 5):
        if bit_string[i:i + 5] == '11111':
            bit_string = bit_string[:i + 5]  + bit_string[i + 6:]
            knt += 1

    print('bits removed: {}'.format(knt))
    return bit_string

if __name__ == '__main__':
    text = str(input("Enter Text: "))

    bits_string = ''.join(format(ord(i), 'b') for i in text)
    print('Bits String: ' + bits_string)

    data_after_bit_stuffing = bit_stuffing(bits_string)
    print('Data after bit stuffing: '+data_after_bit_stuffing)

    data_after_de_stuffing = de_stuffing(data_after_bit_stuffing)
    print('Data after de stuffing: '+data_after_de_stuffing)


