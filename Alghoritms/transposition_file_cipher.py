import os
import sys
import time
import transposition_cipher


def main():
    encrypt_file('frankenstein.txt', 'frankenstein.encrypted.txt', 7)
    decrypt_file('frankenstein.encrypted.txt', 'frankenstein.decrypted.txt', 7)


def encrypt_file(input_filename, output_filename, key):
    if not os.path.exists(input_filename):
        print('The file %s does not exist. Quitting...' % input_filename)
        sys.exit()
    elif os.path.exists(output_filename):
        print('This will overwrite the file %s. Press c to continue or '
              'q to quit.' % input_filename)
        pressed_key = input()
        if not pressed_key.lower().startswith('c'):
            sys.exit()
    input_file = open(input_filename)
    content = input_file.read()
    input_file.close()
    print('Encrypting...')
    start_time = time.time()
    encrypted = transposition_cipher.encrypt_message(content, key)
    total_time = round(time.time() - start_time, 2)
    output_file = open(output_filename, 'w')
    output_file.write(encrypted)
    output_file.close()
    print('Encrypting done, total time: %s, encrypted characters: %s'
          % (total_time, len(content)))
    print('Name of encrypted file is %s' % output_filename)


def decrypt_file(input_filename, output_filename, key):
    if not os.path.exists(input_filename):
        print('The file %s does not exist. Quitting...' % input_filename)
        sys.exit()
    elif os.path.exists(output_filename):
        print('This will overwrite the file %s. Press c to continue or '
              'q to quit.' % output_filename)
        pressed_key = input()
        if not pressed_key.lower().startswith('c'):
            sys.exit()
    input_file = open(input_filename)
    content = input_file.read()
    input_file.close()
    print('Decrypting...')
    start_time = time.time()
    decrypted = transposition_cipher.decrypt_message(content, key)
    total_time = round(time.time() - start_time, 2)
    output_file = open(output_filename, 'w')
    output_file.write(decrypted)
    output_file.close()
    print('Decrypting done, total time: %s, decrypted characters: %s'
          % (total_time, len(content)))
    print('Name of decrypted file is %s' % output_filename)


if __name__ == '__main__':
    main()
