import string

LETTERS = string.ascii_uppercase


def main():
    text = 'This is my secret message.'
    print(encrypt_message(text, 13))
    print(decrypt_message(encrypt_message(text, 13), 13))


def encrypt_message(plaintext, key):
    ciphertext = ''
    for symbol in plaintext.upper():
        if symbol in LETTERS:
            index = LETTERS.find(symbol)
            ciphertext += LETTERS[(index + key) % len(LETTERS)]
        else:
            ciphertext += symbol
    return ciphertext


def decrypt_message(ciphertext, key):
    plaintext = ''
    for symbol in ciphertext.upper():
        if symbol in LETTERS:
            index = LETTERS.find(symbol)
            plaintext += LETTERS[(index - key) % len(LETTERS)]
        else:
            plaintext += symbol
    return plaintext


if __name__ == '__main__':
    main()
