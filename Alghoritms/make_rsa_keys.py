import cryptomath
import os
import rabin_miller
import random
import sys


def main():
    print('Making key files...')
    make_key_files('mateusz_krol', 1024)
    print('Key files made.')


def generate_key(key_size):
    print('Generating p prime')
    p = rabin_miller.generate_large_prime(key_size)
    print('Generating q prime')
    q = rabin_miller.generate_large_prime(key_size)
    n = p * q
    print('Generating e that is relatively prime to (p - 1) * (q - 1).')
    while True:
        e = random.randrange(2 ** (key_size - 1), 2 ** key_size)
        if cryptomath.gcd(e, (p - 1) * (q - 1)) == 1:
            break
    print('Calculating d that is mod inverse of e...')
    d = cryptomath.find_mod_inverse(e, (p - 1) * (q - 1))
    public_key = (n, e)
    private_key = (n, d)
    print('Public key: ', public_key)
    print('Private key: ', private_key)
    return public_key, private_key


def make_key_files(name, key_size):
    if os.path.exists('%s_public_key.txt' % name) or\
            os.path.exists('%s_private_key.txt' % name):
        sys.exit('WARNING: File %s_public_key.txt or %s_private_key.txt '
                 'already exists. Use different name' % (name, name))
    public_key, private_key = generate_key(key_size)
    print('The public key is a %s and a %s digit number.'
          % (len(str(public_key[0])), len(str(public_key[1]))))
    print('Writing public key to file: %s_public_key.txt' % name)
    file = open('%s_public_key.txt' % name, 'w')
    file.write('%s,%s,%s' % (key_size, public_key[0], public_key[1]))
    file.close()
    print('The private key is a %s and a %s digit number.'
          % (len(str(private_key[0])), len(str(private_key[1]))))
    print('Writing private key to file: %s_private_key.txt' % name)
    file = open('%s_private_key.txt' % name, 'w')
    file.write('%s,%s,%s' % (key_size, private_key[0], private_key[1]))
    file.close()


if __name__ == '__main__':
    main()
