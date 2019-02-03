import random


def main():
    f = open("baza1.txt")
    message = f.read()
    f.close()
    print(message)
    key = 2
    hidden_message = hide_message(message, key)
    print(hidden_message)
    print(translate_message(hidden_message, key))

def get_words(key):
    all_words = {}
    file = open("english_dictionary.txt")
    all_words_list = file.read().split('\n')
    file.close()

    for word in all_words_list:
        if len(word) > key:
            all_words[word] = 0
    return all_words

#lista slow kandydatow do losowania
def get_candidates(letter, key):
    candidates = []
    all_words = get_words(key)
    for candidate in all_words:
        if candidate[key] == letter:
            candidates.append(candidate)
    return candidates


#key czyli ktora litera slowa
def hide_message(message, key):
    message = message.split(' ')
    hidden_message = []
    for word in message:
        word = list(word)
        for letter in word:
	    if letter == '\n':
	        
            candidates = get_candidates(letter, key)
            hidden_message.append(random.choice(candidates))
	hidden_message.append(' ')
    return ''.join(hidden_message)

def translate_message(message, key):
    message = message.split(' ')
    translated = []
    for word in message:
        word  = list(word)
        translated.append(word[key])
    return ' '.join(translated)

if __name__ == '__main__':
    main()