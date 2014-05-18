import collections
import sys


for case_no in xrange(1, input() + 1):
    print >> sys.stderr, "Case #%s:" % (case_no,)
    print "Case #%s:" % (case_no,),

    N = input()
    M = [map(int, raw_input()) for _ in xrange(N)]
    A = [max(i if v == 1 else -1 for i, v in enumerate(r)) for r in M]

    c = 0
    while True:
        for i in xrange(N-1):
            if A[i] > i:
                for j in xrange(i+1, N):
                    if A[j] <= i:
                        break
                else:
                    assert False
                r = A.pop(j)
                assert r <= i
                A.insert(i, r)
                c += j-i
                break
        else:
            break
    print c
