import math
import pyperclip


def main():
    text = '''Charles Babbage, FRS (26 December 1791 - 18 October 1871) was an English
mathematician, philosopher, inventor and mechanical engineer who originated the
concept of a programmable computer. Considered a "father of the computer",
Babbage is credited with inventing the first mechanical computer that
eventually led to more complex designs. Parts of his uncompleted mechanisms are
on display in the London Science Museum. In 1991, a perfectly functioning
difference engine was constructed from Babbage's original plans. Built to
tolerances achievable in the 19th century, the success of the finished engine
indicated that Babbage's machine would have worked. Nine years later, the
Science Museum completed the printer Babbage had designed for the difference
engine.'''
    print(len(text))
    encrypted_text = encrypt_message(text, 6)
    print(encrypted_text + '|')
    print('\n' + decrypt_message(encrypted_text, 6) + '|')
    pyperclip.copy(encrypted_text)


def encrypt_message(message, key):
    message = message.upper()
    ciphertext = [''] * key
    for col_number in range(key):
        pointer = col_number
        while pointer < len(message):
            ciphertext[col_number] += message[pointer]
            pointer += key
    return ''.join(ciphertext)

def decrypt_message(ciphertext, key):
    ciphertext = ciphertext.upper()
    num_of_rows = key
    num_of_columns = math.ceil(len(ciphertext) / key)
    num_of_unused_boxes = num_of_rows * num_of_columns - len(ciphertext)
    plaintext = [''] * num_of_columns
    column = 0
    row = 0
    for symbol in ciphertext:
        plaintext[column] += symbol
        column += 1
        if column == num_of_columns or (column == num_of_columns - 1 and row >=
                                        num_of_rows - num_of_unused_boxes):
            column = 0
            row += 1
    return ''.join(plaintext)


if __name__ == '__main__':
    main()
