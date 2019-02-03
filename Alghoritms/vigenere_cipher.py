import pyperclip
import string

LETTERS = string.ascii_uppercase


def main():
    file = open('C:\\Users\\Mateusz\\PythonProjects\\Aplikacja_szyfrowanie\\Alghoritms\\message_vigenere.txt')
    message = file.read()
    file.close()
    key = 'ASIMOV'
    encrypted = encrypt_message(message, key)
    decrypted = decrypt_message(encrypted, key)
    print('Encrypted message:\n%s' % encrypted)
    print('\nCopying encrypted message to clipboard.\n')
    pyperclip.copy(encrypted)
    print('Decrypted message:\n%s' % decrypted)


def encrypt_message(message, key):
    message = message.upper()
    encrypted = []
    key_index = 0
    key = key.upper()
    for symbol in message:
        num = LETTERS.find(symbol.upper())
        if num != -1:
            num = (num + LETTERS.find(key[key_index])) % len(LETTERS)
            encrypted.append(LETTERS[num])
            key_index += 1
            if key_index == len(key):
                key_index = 0
        else:
            encrypted.append(symbol)
    return ''.join(encrypted)


def decrypt_message(message, key):
    message = message.upper()
    decrypted = []
    key_index = 0
    key = key.upper()
    for symbol in message:
        num = LETTERS.find(symbol.upper())
        if num != -1:
            num = (num - LETTERS.find(key[key_index])) % len(LETTERS)
            decrypted.append(LETTERS[num])
            key_index += 1
            if key_index == len(key):
                key_index = 0
        else:
            decrypted.append(symbol)
    return ''.join(decrypted)


if __name__ == '__main__':
    main()
