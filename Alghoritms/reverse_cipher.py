def reverse_cipher(plaintext):
    result = ''
    for index in range(len(plaintext) - 1, -1, -1):
        result += plaintext[index]
    return result


def main():
    text = input('Enter the cipher or the plaintext: ')
    print(reverse_cipher(text))


if __name__ == '__main__':
    main()
