import string
from collections import OrderedDict

ENGLISH_LETTER_FREQUENCY = {'E': 12.70, 'T': 9.06, 'A': 8.17, 'O': 7.51,
                            'I': 6.97, 'N': 6.75, 'S': 6.33, 'H': 6.09,
                            'R': 5.99, 'D': 4.25, 'L': 4.03, 'C': 2.78,
                            'U': 2.76, 'M': 2.41, 'W': 2.36, 'F': 2.23,
                            'G': 2.02, 'Y': 1.97, 'P': 1.93, 'B': 1.29,
                            'V': 0.98, 'K': 0.77, 'J': 0.15, 'X': 0.15,
                            'Q': 0.10, 'Z': 0.07}
                            
ETAOIN = 'ETAOINSHRDLCUMWFGYPBVKJXQZ'
LETTERS = string.ascii_uppercase
ENGLISH_LETTER_FREQUENCY_SORTED = OrderedDict(sorted(ENGLISH_LETTER_FREQUENCY.items()))


def get_letter_count(message):
    letter_count = {'A': 0, 'B': 0, 'C': 0, 'D': 0, 'E': 0, 'F': 0, 'G': 0,
                    'H': 0, 'I': 0, 'J': 0, 'K': 0, 'L': 0, 'M': 0, 'N': 0,
                    'O': 0, 'P': 0, 'Q': 0, 'R': 0, 'S': 0, 'T': 0, 'U': 0,
                    'V': 0, 'W': 0, 'X': 0, 'Y': 0, 'Z': 0}
    for letter in message.upper():
        if letter in LETTERS:
            letter_count[letter] += 1
    return letter_count


def get_percentage_frequency(message):
    letter_count = get_letter_count(message)
    percentage_frequency = {'A': 0, 'B': 0, 'C': 0, 'D': 0, 'E': 0, 'F': 0, 'G': 0,
                            'H': 0, 'I': 0, 'J': 0, 'K': 0, 'L': 0, 'M': 0, 'N': 0,
                            'O': 0, 'P': 0, 'Q': 0, 'R': 0, 'S': 0, 'T': 0, 'U': 0,
                            'V': 0, 'W': 0, 'X': 0, 'Y': 0, 'Z': 0}
    sum_of_letter_count = sum(letter_count.values())
    for letter, count in letter_count.items():
        percentage_frequency[letter] = round(count / sum_of_letter_count * 100, 2)
    return percentage_frequency


def get_item_at_index_zero(item):
    return item[0]


def get_frequency_order(message):
    letter_to_frequency = get_letter_count(message)
    frequency_to_letter = {}
    for letter in LETTERS:
        if letter_to_frequency[letter] not in frequency_to_letter:
            frequency_to_letter[letter_to_frequency[letter]] = [letter]
        else:
            frequency_to_letter[letter_to_frequency[letter]].append(letter)
    for frequency in frequency_to_letter:
        frequency_to_letter[frequency].sort(key=ETAOIN.find, reverse=True)
        frequency_to_letter[frequency] = ''.join(frequency_to_letter
                                                 [frequency])
    frequency_pairs = list(frequency_to_letter.items())
    frequency_pairs.sort(key=get_item_at_index_zero, reverse=True)
    frequency_order = []
    for frequency_pair in frequency_pairs:
        frequency_order.append(frequency_pair[1])
    return ''.join(frequency_order)

def english_frequency_match_score(message):
    frequency_order = get_frequency_order(message)
    match_score = 0
    for common_letter in ETAOIN[:6]:
        if common_letter in frequency_order[:6]:
            match_score += 1
    for uncommon_letter in ETAOIN[-6:]:
        if uncommon_letter in frequency_order[-6:]:
            match_score += 1
    return match_score
