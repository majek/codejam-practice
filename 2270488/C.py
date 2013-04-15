import sys
import itertools
import collections
import bisect

'''
# to generate for_real_fixed2
import itertools

ispalindrome = lambda a: a[::-1] == a

for l in range(1, 26):
    ones = ['01' for _ in range(l)]
    ones[0] = '1'
    if l > 1:
        ones[-1] = '012'

    twos = ['0' for _ in range(l)]
    twos[0] = '2'
    twos[-1] = '012'
    for chars in itertools.product(*twos):
        a = ''.join(itertools.chain(chars[:-1], reversed(chars)))
        b = ''.join(itertools.chain(chars, reversed(chars)))
        for c in (long(a), long(b)):
            d = pow(c, 2)
            n = str(d)
            if ispalindrome(n):
                print n

    for chars in itertools.product(*ones):
        a = ''.join(itertools.chain(chars[:-1], reversed(chars)))
        b = ''.join(itertools.chain(chars, reversed(chars)))
        for c in (long(a), long(b)):
            d = pow(c, 2)
            n = str(d)
            if ispalindrome(n):
                print n
'''

good = []
with open('for_real_fixed2', 'rb') as f:
    for line in f:
        good.append(long(line))


for case_no in xrange(0, input()):
    print >> sys.stderr, "Case #%s:" % (case_no + 1,)
    print "Case #%s:" % (case_no + 1,),

    A, B = map(long, raw_input().split())
    c = 0
    idx1 = bisect.bisect_left(good, A)
    idx2 = bisect.bisect_right(good, B)
    print idx2-idx1
