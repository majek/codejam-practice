import sys
import itertools

def digits():
    yield 1
    yield 0
    for i in itertools.count(2):
        yield i

for case_no in xrange(1, input() + 1):
    print >> sys.stderr, "Case #%s:" % (case_no,)
    print "Case #%s:" % (case_no,),

    N = list(raw_input())

    symbols = set(N)
    if len(symbols) == 1:
        symbols.add('#')

    base = len(symbols)
    m = {}
    i = digits()
    for c in N:
        if c not in m:
            m[c] = i.next()
    n = 0
    for i, c in enumerate(reversed(N)):
        n += m[c] * (base ** i)
    print n
