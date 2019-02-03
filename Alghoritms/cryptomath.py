def gcd(a, b):
    while a != 0:
        a, b = b % a, a
    return b


def extended_euclid(a, b):
    if b == 0:
        return a, 1, 0
    else:
        d_prim, x_prim, y_prim = extended_euclid(b, a % b)
        d, x, y = d_prim, y_prim, x_prim - a // b * y_prim
        return d, x, y


def mod_inverse(a, b):
    x = extended_euclid(a, b)
    if x[0] == 1:
        return x[1] % b
    return None


def find_mod_inverse(a, m):
    """
    Rozszerzony algorytm Euklidesa
    :param a: int
    :param m: int
    :return: int
    """
    if gcd(a, m) != 1:
        return None
    u1, u2, u3 = 1, 0, a
    v1, v2, v3 = 0, 1, m
    while v3 != 0:
        q = u3 // v3
        v1, v2, v3, u1, u2, u3 = (u1 - q * v1), (u2 - q * v2), \
                                 (u3 - q * v3), v1, v2, v3
    return u1 % m


def find_mod_inverse_test_2(a, b):
    u = 1
    w = a
    x = 0
    z = b
    while w != 0:
        if w < z:
            u, x = x, u
            w, z = z, w
        q = w // z
        u = u - q * x
        w = w - q * z
    if z != 1:
        return None
    if x < 0:
        x = x + b
    return x
