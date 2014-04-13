import sys
import itertools

for case_no in xrange(1, input() + 1):
    print "Case #%s:" % (case_no,)

    R, C, M = map(int, raw_input().split())

    A = [['.' for c in xrange(C)] for r in xrange(R)]
    pos = [(r, c) for c in xrange(C) for r in xrange(R)]
    pos.sort(key=lambda (a,b):max(a,b))
    for _ in xrange(M):
        r, c = pos.pop()
        A[r][c] = '*'

    if (len(pos) == 1 or
        (len(pos) > 1 and min(R,C) == 1) or
        len(pos) >=4):
        A[0][0] = 'c'
        for r in A:
            print ''.join(r)
    else:
        print "Impossible"

