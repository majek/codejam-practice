import sys
import itertools
import collections

for case_no in xrange(0, input()):
    print >> sys.stderr, "Case #%s:" % (case_no + 1,)
    print "Case #%s:" % (case_no + 1,),

    N, M = map(int, raw_input().split())
    A = [map(int, raw_input().split()) for _ in xrange(N)]

    # heights = collections.defaultdict(set)
    # for n in range(N):
    #     for m in range(M):
    #         heights[A[n][m]].add( (n,m) )


    max_row = [None] * N
    for n in range(N):
        max_row[n] = max(A[n])
    max_col = [None] * M
    for m in range(M):
        max_col[m] = max(A[i][m] for i in range(N))

    r = True
    for n in range(N):
        for m in range(M):
            c = A[n][m]
            if max_col[m] <= c or max_row[n] <= c:
                continue
            else:
                r = False
                break
        if not r:
            break
    print 'YES' if r else 'NO'
