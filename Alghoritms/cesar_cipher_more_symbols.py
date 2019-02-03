def main():
    text = 'This is my secret message.'
    print(encryption(text, 13))
    print(decryption(encryption(text, 13), 13))


def encryption(plaintext, key):
    alphabet = ' !"#$%&\'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_`abcdefghijklmnopqrstuvwxyz{|}~'
    cipher = ''
    for symbol in plaintext:
        if symbol in alphabet:
            index = alphabet.find(symbol)
            num = index + key
            if num >= len(alphabet):
                num -= len(alphabet)
            cipher += alphabet[num]
        else:
            cipher += symbol
    return cipher


def decryption(cipher, key):
    alphabet = ' !"#$%&\'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_`abcdefghijklmnopqrstuvwxyz{|}~'
    plaintext = ''
    for symbol in cipher:
        if symbol in alphabet:
            index = alphabet.find(symbol)
            num = index - key
            if num < 0:
                num += len(alphabet)
            plaintext += alphabet[num]
        else:
            plaintext += symbol
    return plaintext


if __name__ == '__main__':
    main()
