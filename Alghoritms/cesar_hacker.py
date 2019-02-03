import detect_english

def main():
    cipher = 'GUVF VF ZL FRPERG ZRFFNTR.'
    print(hack_cipher(cipher))


def hack_cipher(cipher):
    """
    Funkcja, która deszyfruje podany tekst kolejnymi kluczami, zaczynając od 1.
    Wypisze na ekranie pary wartości: klucz, rozszyfrowana wiadomość.
    :param cipher: str
    :return: list
    """
    LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    cipher = cipher.upper()
    for key in range(1, len(LETTERS)):
        translated = ''
        for symbol in cipher:
            if symbol in LETTERS:
                index = LETTERS.find(symbol)
                num = index - key
                if num >= len(LETTERS):
                    num += len(LETTERS)
                translated += LETTERS[num]
            else:
                translated += symbol
        if detect_english.is_english(translated, word_percentage=40):
            return translated, str(key)
    return '', ''


if __name__ == '__main__':
    main()
