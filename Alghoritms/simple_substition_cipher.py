import random
import string

LETTERS = string.ascii_uppercase


def main():
    file = open('message.txt')
    message = file.read().upper()
    file.close()
    key = get_random_key()
    if check_key(key):
        print(LETTERS)
        print(key)
        print(message)
        print(encrypt_message(message, key))
        print(decrypt_message(encrypt_message(message, key), key))


def check_key(key):
    letters_list = list(LETTERS)
    key_list = list(key)
    letters_list.sort()
    key_list.sort()
    if key_list != letters_list:
        return False
    return True


def encrypt_message(message, key):
    message = message.upper()
    encrypted_message = ''
    for symbol in message:
        if symbol.upper() in LETTERS:
            sym_index = LETTERS.find(symbol.upper())
            if symbol.isupper():
                encrypted_message += key[sym_index]
            else:
                encrypted_message += key[sym_index].lower()
        else:
            encrypted_message += symbol
    return encrypted_message


def decrypt_message(message, key):
    message = message.upper()
    decrypted_message = ''
    for symbol in message:
        if symbol.upper() in key:
            sym_index = key.find(symbol.upper())
            if symbol.isupper():
                decrypted_message += LETTERS[sym_index]
            else:
                decrypted_message += LETTERS[sym_index].lower()
        else:
            decrypted_message += symbol
    return decrypted_message


def get_random_key():
    random_key = list(LETTERS)
    random.shuffle(random_key)
    return ''.join(random_key)


if __name__ == '__main__':
    main()
