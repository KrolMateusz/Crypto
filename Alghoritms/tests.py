import random
import string
import time
import affine_cipher
import affine_hacker
import cesar_cipher
import cesar_hacker
import simple_substition_cipher
import simple_substition_hacker
import transposition_cipher
import transposition_hacker
import vigenere_cipher
import vigenere_hacker


def test_transposition():
    print('SZYFR KOLUMNOWY\n')
    wynik_2 = 0
    for i in range(3):
        wynik = 0
        message = string.ascii_uppercase * random.randint(100, 400)
        message = list(message)
        random.shuffle(message)
        message = ''.join(message)
        print('Test No %s: %s..., message length: %s' % (i, message[:60], len(message)))
        for key in random.choices(range(1, len(message)), k=5):
            start_time = time.time()
            encrypted = transposition_cipher.encrypt_message(message, key)
            decrypted = transposition_cipher.decrypt_message(encrypted, key)
            if message != decrypted:
                print('Mismatch with key %s, message: %s, length of message '
                      '%s.' % (key, message, len(message)))
            else:
                wynik += 1
            print(round(time.time() - start_time, 2))
        if wynik == 5:
            wynik_2 += 1
    print(wynik_2 / 3)
    print('KONIEC\n')


def test_affine():
    print('SZYFR AFINICZNY\n')
    wynik_2 = 0
    for i in range(3):
        wynik = 0
        message = string.ascii_uppercase * random.randint(100, 400)
        message = list(message)
        random.shuffle(message)
        message = ''.join(message)
        print('Test No %s: %s..., message length: %s' % (i, message[:60], len(message)))
        for _ in range(5):
            start_time = time.time()
            key = affine_cipher.get_random_key()
            print('KLUCZ: %s' % (key))
            # if not affine_cipher.check_keys(*affine_cipher.get_key_parts(key), 'encrypt'):
            #     wynik += 1
            #     continue
            encrypted = affine_cipher.encrypt_message(message, key)
            if encrypted:
                decrypted = affine_cipher.decrypt_message(encrypted, key)
            else:
                decrypted = ''
            if message != decrypted and decrypted:
                print('Mismatch with key %s, message: %s, length of message '
                      '%s.' % (key, message, len(message)))
                print(decrypted)
            else:
                wynik += 1
            print(round(time.time() - start_time, 2))
        if wynik == 5:
            wynik_2 += 1
    print(wynik_2 / 3)
    print('KONIEC\n')


def test_cesar():
    print('SZYFR CEZARA\n')
    wynik_2 = 0
    for i in range(3):
        wynik = 0
        message = string.ascii_uppercase * random.randint(100, 400)
        message = list(message)
        random.shuffle(message)
        message = ''.join(message)
        print('Test No %s: %s... message length: %s' % (i, message[:60], len(message)))
        for key in random.choices(range(1, 26), k=5):
            start_time = time.time()
            encrypted = cesar_cipher.encrypt_message(message, key)
            decrypted = cesar_cipher.decrypt_message(encrypted, key)
            if message != decrypted:
                print('Mismatch with key %s, message: %s, length of message '
                      '%s.' % (key, message, len(message)))
                print(time.time() - start_time)
            else:
                wynik += 1
            print(round(time.time() - start_time, 2))
        if wynik == 5:
            wynik_2 += 1
    # print(time.time() - start_time)
    print(wynik_2 / 3)
    print('KONIEC\n')


def test_substition():
    wynik_2 = 0
    print('SZYFR PODSTAWIENIOWY\n')
    for i in range(3):
        wynik = 0
        message = string.ascii_uppercase * random.randint(100, 400)
        message = list(message)
        random.shuffle(message)
        message = ''.join(message)
        print('Test No %s: %s..., message length: %s' % (i, message[:60], len(message)))
        for _ in range(5):
            start_time = time.time()
            key = simple_substition_cipher.get_random_key()
            encrypted = simple_substition_cipher.encrypt_message(message, key)
            decrypted = simple_substition_cipher.decrypt_message(encrypted, key)
            if message != decrypted:
                print('Mismatch with key %s, message: %s, length of message '
                      '%s.' % (key, message, len(message)))
            else:
                wynik += 1
            print(round(time.time() - start_time, 2))
        if wynik == 5:
            wynik_2 += 1
    print(wynik_2 / 3)
    print('KONIEC\n')


def test_vigenere():
    wynik_2 = 0
    print('SZYFR VIGENERE\n')
    for i in range(3):
        wynik = 0
        message = string.ascii_uppercase * random.randint(100, 400)
        message = list(message)
        random.shuffle(message)
        message = ''.join(message)
        print('Test No %s: %s..., message length: %s' % (i, message[:60], len(message)))
        for test in range(5):
            start_time = time.time()
            key = string.ascii_uppercase[:random.randint(15, 25)] * random.randint(20, 40)
            encrypted = vigenere_cipher.encrypt_message(message, key)
            decrypted = vigenere_cipher.decrypt_message(encrypted, key)
            if message != decrypted:
                print('Mismatch with key %s, message: %s, length of message '
                      '%s.' % (key, message, len(message)))
            wynik += 1
            print(round(time.time() - start_time, 2))
        if wynik == 5:
            wynik_2 += 1
    print(wynik_2 / 3)
    print('KONIEC\n')


def test_affine_analysis():
    print('SZYFR AFINICZNY\n')
    with open('C:\\Users\\Mateusz\\PythonProjects\\Aplikacja_szyfrowanie\\Alghoritms\\message.txt') as file:
        message = file.read().upper()
    wynik = 0
    for _ in range(5):
        stary_time = time.time()
        ciphertext = affine_cipher.encrypt_message(message, affine_cipher.get_random_key())
        plaintext = affine_hacker.hack_affine(ciphertext)
        print(plaintext[0][:100])
        if plaintext[0] == message:
            wynik += 1
        print(round(time.time() - stary_time, 2))
    print(wynik / 5)


def test_cesar_analysis():
    print('\nSZYFR CEZARA')
    with open('C:\\Users\\Mateusz\\PythonProjects\\Aplikacja_szyfrowanie\\Alghoritms\\message.txt') as file:
        message = file.read().upper()
    wynik = 0
    for _ in range(5):
        start_time = time.time()
        ciphertext = cesar_cipher.encrypt_message(message, random.randint(1, 26))
        plaintext = cesar_hacker.hack_cipher(ciphertext)
        print(plaintext[0][:80])
        if plaintext[0] == message:
            wynik += 1
        print(round(time.time() - start_time, 2))
    print(wynik / 5)


def test_transposition_analysis():
    print('\nSZYFR KOLUMNOWY')
    with open('C:\\Users\\Mateusz\\PythonProjects\\Aplikacja_szyfrowanie\\Alghoritms\\message.txt') as file:
        message = file.read().upper()
    wynik = 0
    for _ in range(5):
        start_time = time.time()
        key = random.randint(2, len(message) // 2)
        ciphertext = transposition_cipher.encrypt_message(message, key)
        plaintext, key_analysis = transposition_hacker.hack_transposition_cipher(ciphertext)
        print('Klucz: {0}, klucz analizy {1}'.format(key, key_analysis))
        if plaintext== message:
            wynik += 1
        print(round(time.time() - start_time, 2))
    print(wynik / 5)


def test_substition_analysis():
    print('\nSZYFR PODSTAWIENIOWY')
    with open('C:\\Users\\Mateusz\\PythonProjects\\Aplikacja_szyfrowanie\\Alghoritms\\message_1.txt') as file:
        message = file.read().upper()
    wynik = 0
    for _ in range(5):
        start_time = time.time()
        key = simple_substition_cipher.get_random_key()
        ciphertext = simple_substition_cipher.encrypt_message(message, key)
        plaintext = simple_substition_hacker.decrypt_with_cipher_letter_mappings(ciphertext, simple_substition_hacker.hack_cipher(ciphertext))
        print(plaintext[0])
        if plaintext[0] == message:
            wynik += 1
        print(round(time.time() - start_time, 2))
    print(wynik / 5)


def test_vigenere_analysis():
    print('\nSZYFR VIGENERE')
    with open('C:\\Users\\Mateusz\\PythonProjects\\Aplikacja_szyfrowanie\\Alghoritms\\message.txt') as file:
        message = file.read().upper()
    wynik = 0
    for _ in range(5):
        start_time = time.time()
        key = list(string.ascii_uppercase[:random.randint(5, 12)])
        random.shuffle(key)
        key = ''.join(key)
        ciphertext = vigenere_cipher.encrypt_message(message, key)
        plaintext, key_analysis = vigenere_hacker.hack_vigenere(ciphertext)
        print(plaintext[:80])
        if key == key_analysis:
            wynik += 1
        print(round(time.time() - start_time, 2))
    print(wynik / 5)


if __name__ == "__main__":
    # test_cesar()
    # test_transposition()
    # test_affine()
    # test_substition()
    # test_vigenere()
    test_affine_analysis()
    test_cesar_analysis()
    test_transposition_analysis()
    test_substition_analysis()
    test_vigenere_analysis()
