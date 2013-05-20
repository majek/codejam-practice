import sys
import itertools
import collections


def get_numbers(X, v):
    while X[v]:
        n = X[v]
        yield n
        v -= n


def solve(S):
    all_sum = sum(S)
    X = [None] * (all_sum + 1)
    X[0] = 0

    for s in S:
        for i in xrange(len(X)-1, 0-1, -1):
            if X[i] is None:
                continue
            if X[i+s] is None:
                X[i+s] = s
            else:
                return (list(get_numbers(X, i+s)),
                        list(get_numbers(X, i)) + [s])
    return (None, None)


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
