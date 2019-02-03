import copy
import make_word_patterns
import re
import simple_substition_cipher
import word_patterns
import pprint
import string

LETTERS = string.ascii_uppercase
non_letters_or_space_pattern = re.compile('[^A-Z\s]')


def main():
    file = open('message_hacker.txt')
    message = file.read()
    file.close()
    print('Hacking...')
    letter_mapping = hack_cipher(message)
    print('Mapping:')
    pprint.pprint(letter_mapping)
    print('\nOriginal ciphertext:')
    print(message)
    print('\nCopying hacked message.')
    hacked_message = decrypt_with_cipher_letter_mappings(message,
                                                         letter_mapping)
    print(hacked_message)


def get_blank_cipher_letter_mapping():
    return {'A': [], 'B': [], 'C': [], 'D': [], 'E': [], 'F': [], 'G': [],
            'H': [], 'I': [], 'J': [], 'K': [], 'L': [], 'M': [], 'N': [],
            'O': [], 'P': [], 'Q': [], 'R': [], 'S': [], 'T': [], 'U': [],
            'V': [], 'W': [], 'X': [], 'Y': [], 'Z': []}


def add_letters_to_mapping(letter_mapping, cipherword, candidate):
    letter_mapping = copy.deepcopy(letter_mapping)
    for i in range(len(cipherword)):
        if candidate[i] not in letter_mapping[cipherword[i]]:
            letter_mapping[cipherword[i]].append(candidate[i])
    return letter_mapping


def intersect_mappings(map_a, map_b):
    intersected_mapping = get_blank_cipher_letter_mapping()
    for letter in LETTERS:
        if not map_a[letter]:
            intersected_mapping[letter] = copy.deepcopy(map_b[letter])
        elif not map_b[letter]:
            intersected_mapping[letter] = copy.deepcopy(map_a[letter])
        else:
            for mapped_letter in map_a[letter]:
                if mapped_letter in map_b[letter]:
                    intersected_mapping[letter].append(mapped_letter)
    return intersected_mapping


def remove_solved_letters_from_mapping(letter_mapping):
    letter_mapping = copy.deepcopy(letter_mapping)
    loop_again = True
    while loop_again:
        loop_again = False
        solved_letters = []
        for cipher_letter in LETTERS:
            if len(letter_mapping[cipher_letter]) == 1:
                solved_letters.append(letter_mapping[cipher_letter][0])
        for cipher_letter in LETTERS:
            for solved_letter in solved_letters:
                if (len(letter_mapping[cipher_letter]) != 1 and
                        solved_letter in letter_mapping[cipher_letter]):
                    letter_mapping[cipher_letter].remove(solved_letter)
                    if len(letter_mapping[cipher_letter]) == 1:
                        loop_again = True
    return letter_mapping


def hack_cipher(message):
    message = message.upper()
    intersected_map = get_blank_cipher_letter_mapping()
    cipherword_list = non_letters_or_space_pattern.sub('',
                                                       message.upper()).split()
    for cipherword in cipherword_list:
        new_map = get_blank_cipher_letter_mapping()
        word_pattern = make_word_patterns.get_word_pattern(cipherword)
        if word_pattern not in word_patterns.all_patterns:
            continue
        for candidate in word_patterns.all_patterns[word_pattern]:
            new_map = add_letters_to_mapping(new_map, cipherword, candidate)
        intersected_map = intersect_mappings(intersected_map, new_map)
    return remove_solved_letters_from_mapping(intersected_map)


def decrypt_with_cipher_letter_mappings(ciphertext, letter_mapping):
    ciphertext = ciphertext.upper()
    key = ['x'] * len(LETTERS)
    for cipher_letter in LETTERS:
        if len(letter_mapping[cipher_letter]) == 1:
            key_index = LETTERS.find(letter_mapping[cipher_letter][0])
            key[key_index] = cipher_letter
        else:
            ciphertext = ciphertext.replace(cipher_letter.lower(), '_')
            ciphertext = ciphertext.replace(cipher_letter.upper(), '_')
    key = ''.join(key)
    return simple_substition_cipher.decrypt_message(ciphertext, key), str(key)


if __name__ == '__main__':
    main()
