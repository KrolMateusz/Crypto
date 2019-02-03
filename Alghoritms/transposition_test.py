import random
import sys
import transposition_cipher


def main():
    test_cipher()


def test_cipher():
    # Wykonuję 100 testów, dla których generuje wiadomość złożoną z liter
    # alfabetu łacińskiego. Następnie zamieniam kolejność liter i szyfruje, a
    # następnie deszyfruje wiadomość wszystkimi kluczami. Gdy oryginalny tekst
    # jest inny niż tekst najpierw zaszyfrowany, a później odszyfrowany,
    # zwracam komunikat i kończę działanie programu.
    for i in range(100):
        message = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' * random.randint(10, 40)
        message = list(message)
        random.shuffle(message)
        message = ''.join(message)
        print('Test No %s: %s...' % (i, message[:100]))
        for key in range(1, len(message)):
            encrypted = transposition_cipher.encrypt_message(message, key)
            decrypted = transposition_cipher.decrypt_message(encrypted, key)
            if message != decrypted:
                print('Mismatch with key %s, message: %s, length of message '
                      '%s.' % (key, message, len(message)))
                sys.exit()
    print('Test passed')


if __name__ == '__main__':
    test_cipher()
