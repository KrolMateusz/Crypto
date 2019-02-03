import math


def is_prime(number):
    if number < 2:
        return False
    for i in range(2, int(math.sqrt(number))):
        if number % i == 0:
            return False
    return True


def prime_sieve(sieve_size):
    sieve = [True] * sieve_size
    sieve[0] = False
    sieve[1] = False
    for i in range(2, int(math.sqrt(sieve_size)) + 1):
        pointer = i * 2
        while pointer < sieve_size:
            sieve[pointer] = False
            pointer += i
    primes = []
    for i in range(sieve_size):
        if sieve[i]:
            primes.append(i)
    return primes
