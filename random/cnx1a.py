import numpy as np

def encrypt(text, rows, columns):
    text_letter_wise = [text[i:i + 1] for i in range(len(text))]

    (text_letter_wise.append('#') for i in range( (rows * columns) - len(text_letter_wise) ) )

    matrix = np.array(text_letter_wise).reshape(rows, columns).transpose().ravel()
    encryted_text = ""

    for i in range(len(matrix)):
        encryted_text += matrix[i]

    return encryted_text

def decrypt(cipher_text, rows ,columns):
    cipher_text_letter_wise = [ cipher_text[i:i+1] for i in range(len(cipher_text))]

    matrix = np.array(cipher_text_letter_wise).reshape(columns, rows).transpose().ravel()
    decrypted_text = ""

    for i in range(len(matrix)):
        if matrix[i] == '#':
            continue
        else:
            decrypted_text += matrix[i]

    return decrypted_text

if __name__ == "__main__":
    print('-------TRANSPOSITION CIPHER-------')
    text = str(input("Enter the text"))

    rows = int(input('Rows? '))
    columns = int(input('Columns? '))

    cipher_text = encrypt(text,rows,columns)
    print('Cipher Text: {}'.format(cipher_text))

    decrypted_text = decrypt(cipher_text,rows,columns)
    print("Decrypted Text: {}".format(decrypted_text))