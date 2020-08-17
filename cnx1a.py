import numpy as np

def encrypt(matrix, rows, columns):
    matrix = np.transpose(matrix)
    matrix = np.array(matrix).reshape(1,rows * columns)
    print(matrix)

    encryted_text = ""
    ref = list(matrix[0])

    for i in range(len(ref)):
        if ref[i] == '-99':
            continue
        else:
            encryted_text += ref[i]

    return encryted_text

def decrypt(cipher_text, rows ,columns):
    cipher_text_letter_wise = [ cipher_text[i:i+1] for i in range(len(cipher_text))]
    diff = (rows*columns) - len(cipher_text_letter_wise)
    for i in range(diff):
        cipher_text_letter_wise.append(-99)

    matrix = np.array(cipher_text_letter_wise).reshape(columns, rows)
    matrix = np.transpose(matrix)
    matrix = np.array(matrix).reshape(1,rows * columns)

    ref = list(matrix[0])
    decrypted_text = ""

    for i in range(len(ref)):
        if ref[i] == '-99':
            continue
        else:
            decrypted_text += ref[i]

    return decrypted_text

if __name__ == "__main__":
    print('-------TRANSPOSITION CIPHER-------')
    text = str(input("Enter the text"))
    text_letter_wise = [ text[i:i+1] for i in range(len(text)) ]

    rows = int(input('Rows? '))
    columns = int(input('Columns? '))

    diff = (rows * columns) - len(text_letter_wise)

    for i in range(diff):
        text_letter_wise.append(-99)
    matrix = np.array(text_letter_wise).reshape(rows,columns)
    print(matrix)

    cipher_text = encrypt(matrix,rows,columns)
    print('Cipher Text: {}'.format(cipher_text))

    decrypted_text = decrypt(cipher_text,rows,columns)
    print("Decrypted Text: {}".format(decrypted_text))