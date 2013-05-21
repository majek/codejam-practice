import sys
import itertools
import collections


def solve(S):
    X = {}

    r = set()
    while len(s) < 20:
        s.add(random.randint(0, len(S)-1))


for case_no in xrange(0, input()):
    print >> sys.stderr, "Case #%s:" % (case_no + 1,)
    print "Case #%s:" % (case_no + 1,)

    S = set(map(int, raw_input().split())[1:])

    a, b = solve(S)

    if a is None:
        print "Impossible"
    else:
        print ' '.join(map(str, a))
        print ' '.join(map(str, b))
