import sys
from collections import defaultdict


if True:
    L, D, N = map(int, raw_input().split())
    words = [raw_input() for _ in xrange(D)]
    tests = [raw_input() for _ in xrange(N)]

    idx = []
    for letters in zip(*words):
        x = defaultdict(set)
        for word_no, l in enumerate(letters):
            x[l].add(word_no)
        idx.append(x)

    for case_no, test in enumerate(tests):
        possible = set(xrange(D))
        i = 0
        while test:
            if test[0] == '(':
                token, _, test = test[1:].partition(')')
                possible &= reduce(lambda acc, s: acc | s, (idx[i][l] for l in token), set())
            else:
                token, test = test[0], test[1:]
                possible &= idx[i][token]
            i += 1
        assert i == L, i
        print "Case #%s:" % (case_no+1,), len(possible)
