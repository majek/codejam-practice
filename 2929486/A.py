import itertools
import sys


for case_no in xrange(1, input() + 1):
    print >> sys.stderr, "Case #%s:" % (case_no,)
    print "Case #%s:" % (case_no,),

    N = input()
    NN = N * N
    M = [map(int, raw_input().split()) for _ in xrange(NN)]

    good = set(range(1,NN+1))

    bad = 0
    for r in M:
        bad |= set(r) != good
    for c in zip(*M):
        bad |= set(c) != good
    for x in xrange(0, NN, N):
        for y in xrange(0, NN, N):
            square = [M[y+r][x:x+N]
                      for r in xrange(N)]
            bad |= set(itertools.chain(*square)) != good

    print "Yes" if not bad else "No"
