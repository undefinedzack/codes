def crc_encode(data, key):
    # adding k-1 zero's at the end of the data
    data_with_added_zeros = data + ('0' * (len(key) - 1))

    remainder = modulo_division(data_with_added_zeros, key)
    crc_code = data + remainder

    return crc_code


def check_crc(data, key):
    if modulo_division(data, key) == '000':
        return True
    return False


def modulo_division(data, key):
    quotient = ""
    remainder = ""
    zero_string = '0' * len(key)

    for i in range(0, len(data) - len(key) + 1):
        a = data[i:i + len(key)]
        print(a)
        if a[0] == key[0]:
            temp = xor(a, key)
            remainder = temp[1:]
            data = data[0:i] + temp + data[i + len(key):]
            quotient += '1'
        else:
            temp = xor(a, zero_string)
            remainder = temp[1:]
            data = data[0:i] + temp + data[i + len(key):]
            quotient += '0'

    return remainder


def xor(A, B):
    result = ""
    if len(A) == len(B):
        for i in range(len(A)):
            result += str(int(A[i]) ^ int(B[i]))
    else:
        print('error in xor')

    return result


if __name__ == '__main__':
    length = int(input('Enter length of data'))
    data = str(input('Enter data: '))
    key = str(input('Enter key'))

    crc_code = crc_encode(data, key)

    print('The CRC code for {} : {}'.format(data,crc_code))

    # Data received at receiver side
    receiver_data = str(input('Enter data received by the receiver'))

    #checking CRC at the receiver end.
    if check_crc(receiver_data):
        print('The transmitted data has no errors')
    else:
        print('Error : CRC mismatch')
