import pyperclip
import cryptomath
import random
import string
import os

SYMBOLS = string.ascii_uppercase


def main():
    file = open(os.path.dirname(__file__) + '/affine_message.txt')
    print(os.path.dirname(__file__))
    message = file.read().upper()
    file.close()
    message = 'ala ma kota'
    my_key = 21 * 26 + 18
    my_mode = 'encrypt'

    if my_mode == 'encrypt':
        translated = encrypt_message(message, my_key)
    elif my_mode == 'decrypt':
        translated = decrypt_message(message, my_key)
    print('Key: %s' % my_key)
    print('%sed text:' % (my_mode.title()))
    print(translated)
    pyperclip.copy(translated)
    print('Full %sed text copied to clipboard.' % my_mode)


def get_key_parts(key):
    key_a = key // len(SYMBOLS)
    key_b = key % len(SYMBOLS)
    return key_a, key_b


def check_keys(key_a, key_b, mode):
    if key_a == 1 and mode == 'encrypt':
        # print('The affine cipher becomes incredibly weak when key A'
        #       ' is set to 1. Choose a different key.')
        return False
    if key_b == 0 and mode == 'encrypt':
        # print('The affine cipher becomes incredibly weak when key B'
        #       ' is set to 0. Choose a different key.')
        return False
    if key_a < 0 or key_b < 0 or key_b > len(SYMBOLS) - 1:
        # print('Key A must be greater than 0 and Key B must be'
        #       ' between 0 and %s.' % (len(SYMBOLS) - 1))
        return False
    if cryptomath.gcd(key_a, len(SYMBOLS)) != 1:
        # print('Key A (%s) and the symbol set size (%s) are not'
        #       ' relatively prime. Choose a different key.'
        #       % (key_a, len(SYMBOLS)))
        return False
    return True


def encrypt_message(message, key):
    message = message.upper()
    key_a, key_b = get_key_parts(key)
    ciphertext = ''
    if check_keys(key_a, key_b, 'encrypt'):
        for symbol in message:
            if symbol in SYMBOLS:
                sym_index = SYMBOLS.find(symbol)
                ciphertext += SYMBOLS[(sym_index * key_a + key_b) % len(SYMBOLS)]
            else:
                ciphertext += symbol
    return ciphertext


def decrypt_message(message, key):
    message = message.upper()
    key_a, key_b = get_key_parts(key)
    if check_keys(key_a, key_b, 'decrypt'):
        plaintext = ''
        mod_inverse_of_key_a = cryptomath.find_mod_inverse(key_a, len(SYMBOLS))
        for symbol in message:
            if symbol in SYMBOLS:
                sym_index = SYMBOLS.find(symbol)
                plaintext += SYMBOLS[(sym_index - key_b) * mod_inverse_of_key_a
                                    % len(SYMBOLS)]
            else:
                plaintext += symbol
        return plaintext


def get_random_key():
    while True:
        key_a = random.randint(2, len(SYMBOLS))
        key_b = random.randint(2, len(SYMBOLS))
        if cryptomath.gcd(key_a, len(SYMBOLS)) == 1:
            return key_a * len(SYMBOLS) + key_b


if __name__ == '__main__':
    main()
