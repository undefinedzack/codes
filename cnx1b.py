import numpy as np
from string import ascii_lowercase

def alphabet_to_number(text :str):
    text = text.lower()
    numbers = [ alphabets[character] for character in text ]
    return numbers

def number_to_alphabet(la :list):
    letters = [ numbers[the_number] for the_number in la ]
    return letters



if __name__ == '__main__':
    text = str(input(" Enter Text :"))
    private_key = str(input("Enter Private Key of length {}".format(len(text))))

    alphabets = {letter : str(index) for index, letter in enumerate(ascii_lowercase)}
    numbers =   { index : letter   for index, letter in enumerate(ascii_lowercase)}

    text_number = alphabet_to_number(text)
    private_key_number = alphabet_to_number(private_key)

    text_number = list(map(int, (item for item in text_number)))
    private_key_number = list(map(int, (item for item in private_key_number)))

    #encryption
    addition = list( np.add( np.array(text_number), np.array(private_key_number) ) )
    addition_alpha = number_to_alphabet(addition)

    cipher_text = "".join(addition_alpha)
    print('Cipher Text: {}'.format(cipher_text))

    #decryption
    cipher_text_number = alphabet_to_number(cipher_text)
    cipher_text_number = list(map(int, (item for item in cipher_text_number) ))
    subtraction = list( np.subtract( np.array(cipher_text_number) , np.array(private_key_number) ) )
    subtraction_alpha = number_to_alphabet(subtraction)

    decrypted_text = print('Decrypted Text: {}'.format("".join(subtraction_alpha)))