import vigenere_cipher
import pyperclip
import detect_english


def main():
    message = 'Tzx isnz eccjxkg nfq lol mys bbqq I lxcz.'
    hacked_message = hack_vigenere(message)
    if hacked_message:
        print('Copying hacked message to clipboard.\n')
        pyperclip.copy(hacked_message)
        print(hacked_message)
    else:
        print('Hacking failed.')


def hack_vigenere(message):
    file = open('english_dictionary.txt')
    words = file.readlines()
    file.close()
    for word in words:
        word = word.strip()
        decrypted_text = vigenere_cipher.decrypt_message(message, word)
        if detect_english.is_english(decrypted_text, word_percentage=60):
            print('Possible key: %s\nMessage:\n%s' % (word, decrypted_text))
            key_pressed = input('Enter d to stop decrypting or '
                                'press ENTER to continue\n')
            if key_pressed.lower().startswith('d'):
                return decrypted_text


if __name__ == '__main__':
    main()
