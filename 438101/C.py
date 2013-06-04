import sys
import itertools
import bisect


for case_no in xrange(1, input() + 1):
    print >> sys.stderr, "Case #%s:" % (case_no,)
    print "Case #%s:" % (case_no,),

    l = map(int, raw_input().split())
    P, C, S = l[0], l[1], l[2:]

    # Following mr Ralph
    while True:
        mean = sum(S) / C
        greater_than_mean = [i for i in xrange(P) if S[i] > mean]
        if not greater_than_mean:
            break
        for j in greater_than_mean:
            S[j] = mean

    print mean

