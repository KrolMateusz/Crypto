import random


def rabin_miller(number):
    s = number - 1
    t = 0
    while s % 2 == 0:
        s = s // 2
        t += 1
    for trials in range(5):
        a = random.randrange(2, number - 1)
        v = pow(a, s, number)
        if v != 1:
            i = 0
            while v != (number - 1):
                if i == t - 1:
                    return False
                else:
                    i += 1
                    v = (v ** 2) % number
    return True


def is_prime(number):
    if number < 2:
        return False
    low_primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53,
                  59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113,
                  127, 131, 137,139, 149, 151, 157, 163, 167, 173, 179, 181,
                  191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251,
                  257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317,
                  331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397,
                  401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 463,
                  467, 479, 487, 491, 499, 503, 509, 521, 523, 541, 547, 557,
                  563, 569, 571, 577, 587, 593, 599, 601, 607, 613, 617, 619,
                  631, 641, 643, 647, 653, 659, 661, 673, 677, 683, 691, 701,
                  709, 719, 727, 733, 739, 743, 751, 757, 761, 769, 773, 787,
                  797, 809, 811, 821, 823, 827, 829, 839, 853, 857, 859, 863,
                  877, 881, 883, 887, 907, 911, 919, 929, 937, 941, 947, 953,
                  967, 971, 977, 983, 991, 997]
    if number in low_primes:
        return True
    for prime in low_primes:
        if number % prime == 0:
            return False
    return rabin_miller(number)


def generate_large_prime(keysize=1024):
    while True:
        number = random.randrange(2 ** (keysize - 1), 2 ** keysize)
        if is_prime(number):
            return number
