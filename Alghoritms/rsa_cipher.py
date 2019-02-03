import sys

DEFAULT_BLOCK_SIZE = 128
BYTE_SIZE = 256


def main():
    filename = 'encrypted_file_rsa.txt'
    mode = 'decrypt'
    if mode == 'encrypt':
        message = '''"Journalists belong in the gutter because that is where 
        the ruling classes throw their guilty secrets." -Gerald Priestland 
        "The Founding Fathers gave the free press the protection it must 
        have to bare the secrets of government and inform the people." 
        -Hugo Black'''
        public_key_filename = 'mateusz_krol_public_key.txt'
        print('Encrypting and writing to %s...' % filename)
        encrypted_text = encrypt_write_to_file(filename, public_key_filename,
                                               message)
        print('Encrypted text:')
        print(encrypted_text)
    elif mode == 'decrypt':
        private_key_filename = 'mateusz_krol_private_key.txt'
        print('Reading from %s and decrypting...' % filename)
        decrypted_text = decrypt_from_file(filename, private_key_filename)
        print('Decrypted text:')
        print(decrypted_text)


def get_blocks_from_text(message, block_size=DEFAULT_BLOCK_SIZE):
    message_bytes = message.encode('ascii')
    block_ints = []
    for block_start in range(0, len(message_bytes), block_size):
        block_int = 0
        for i in range(block_start,
                       min(block_start + block_size, len(message_bytes))):
            block_int += message_bytes[i] * (BYTE_SIZE ** (i % block_size))
        block_ints.append(block_int)
    return block_ints


def get_text_from_blocks(block_ints, message_length,
                         block_size=DEFAULT_BLOCK_SIZE):
    message = []
    for block_int in block_ints:
        block_message = []
        for i in range(block_size - 1, -1, -1):
            if len(message) + i < message_length:
                ascii_number = block_int // (BYTE_SIZE ** i)
                block_int = block_int % (BYTE_SIZE ** i)
                block_message.insert(0, chr(ascii_number))
        message.extend(block_message)
    return ''.join(message)


def encrypt_message(message, key, block_size=DEFAULT_BLOCK_SIZE):
    encrypted_blocks = []
    n, e = key
    for block in get_blocks_from_text(message, block_size):
        encrypted_blocks.append(pow(block, e, n))
    return encrypted_blocks


def decrypt_message(encrypted_blocks, message_length,
                    key, block_size=DEFAULT_BLOCK_SIZE):
    decrypted_blocks = []
    n, d = key
    for block in encrypted_blocks:
        decrypted_blocks.append(pow(block, d, n))
    return get_text_from_blocks(decrypted_blocks, message_length, block_size)


def read_key_file(key_filename):
    file = open(key_filename)
    content = file.read()
    file.close()
    key_size, n, eord = content.split(',')
    return int(key_size), int(n), int(eord)


def encrypt_write_to_file(message_filename, key_filename,
                          message, block_size = DEFAULT_BLOCK_SIZE):
    key_size, n, e = read_key_file(key_filename)
    if key_size < block_size * 8:
        sys.exit('ERROR: Block size is %s bits and key size is %s bits. The'
                 'RSA cipher requires the block size to be equal to or greater'
                 'than the key size. Either decrease the block size or use'
                 'different keys.' % (block_size * 8, key_size))
    encrypted_blocks = encrypt_message(message, (n, e), block_size)
    for i in range(len(encrypted_blocks)):
        encrypted_blocks[i] = str(encrypted_blocks[i])
    encrypted_content = ','.join(encrypted_blocks)
    encrypted_content = '%s_%s_%s' % (len(message), block_size,
                                      encrypted_content)
    file = open(message_filename, 'w')
    file.write(encrypted_content)
    file.close()
    return encrypted_content


def decrypt_from_file(message_filename, key_filename):
    key_size, n, d = read_key_file(key_filename)
    file = open(message_filename)
    content = file.read()
    message_length, block_size, encrypted_message = content.split('_')
    message_length = int(message_length)
    block_size = int(block_size)
    if key_size < block_size * 8:
        sys.exit('ERROR: Block size is %s bits and key size is %s bits. The'
                 'RSA cipher requires the block size to be equal to or greater'
                 'than the key size. Did you specify the correct key file and'
                 'encrypted file?' % (block_size * 8, key_size))
    encrypted_blocks = []
    for block in encrypted_message.split(','):
        encrypted_blocks.append(int(block))
    return decrypt_message(encrypted_blocks, message_length, (n, d),
                           block_size)


if __name__ == '__main__':
    main()
