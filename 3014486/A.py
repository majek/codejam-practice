import sys
import string
import itertools
import collections
import bisect


for case_no in xrange(1, input() + 1):
    print >> sys.stderr, "Case #%s:" % (case_no,)
    print "Case #%s:" % (case_no,),

    N, X = map(int, raw_input().split())
    S = map(int, raw_input().split())
    S.sort()

    c = 0
    i = 0
    while i < len(S):
        r = S.pop()
        if i < len(S) and S[i] + r <= X:
            #xprint >> sys.stderr, S[i], r
            i += 1
        c += 1
    print c
