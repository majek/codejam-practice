
def modexp(g, u, p):
    """
    >>> modexp(2, 10000, 47) == 2 ** 10000 % 47
    True
    >>> modexp(2, 6, 99)
    64
    >>> modexp(2, 7, 99)
    29
    >>> modexp(2, 8, 99)
    58
    """
    # via: http://stackoverflow.com/questions/5486204/fast-modulo-calculations-in-python-and-ruby
    """computes s = (g ^ u) mod p
    args are base, exponent, modulus
    (see Bruce Schneier's book, _Applied Cryptography_ p. 244)"""
    s = 1
    while u != 0:
        if u & 1:
            s = (s * g) % p
        u >>= 1
        g = (g * g) % p
    return s
