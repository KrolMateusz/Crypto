import pprint


def main():
    all_patterns = {}
    input_file = open('english_dictionary.txt')
    all_words = input_file.read().split('\n')
    input_file.close()
    for word in all_words:
        pattern = get_word_pattern(word)
        if pattern not in all_patterns:
            all_patterns[pattern] = [word]
        else:
            all_patterns[pattern].append(word)
    output_file = open('word_patterns.py', 'w')
    output_file.write('all_patterns = ')
    output_file.write(pprint.pformat(all_patterns))
    output_file.close()


def get_word_pattern(word):
    word = word.upper()
    next_number = 0
    letter_numbers = {}
    word_pattern = []
    for letter in word:
        if letter not in letter_numbers:
            letter_numbers[letter] = str(next_number)
            next_number += 1
        word_pattern.append(letter_numbers[letter])
    return '.'.join(word_pattern)


if __name__ == '__main__':
    main()
