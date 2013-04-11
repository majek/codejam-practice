import random
import array
import nzmath.factor.methods as methods
import nzmath.prime as prime
from collections import defaultdict

def extend(primes, p):
    all_subsets = set(p)
    for i in p:
        if i in primes:
            all_subsets |= primes[i]
    r = frozenset(all_subsets)
    for i in all_subsets:
        primes[i] = r


for case_no in xrange(0, input()):
    print "Case #%s:" % (case_no + 1,),

    A, B, P = map(long, raw_input().split())
    B += 1
    sz = B-A

    prime_numbers = []
    for p in prime.generator():
        if p > sz:
            break
        if p >=P: prime_numbers.append( p )

    arr = defaultdict(list)
    for p in prime_numbers:
        s = (A / p) * p
        if s < A: s += p
        while s < B:
            arr[s].append( p )
            s += p
    primes = {}
    g = 0
    n = A
    while n < B:
        p = arr[n]
        if p:
            extend(primes, p)
        else:
            g += 1
        n += 1

    print g + len(set(primes.itervalues()))
