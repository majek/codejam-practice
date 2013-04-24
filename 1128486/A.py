import sys


for case_no in xrange(1, input() + 1):
    print >> sys.stderr, "Case #%s:" % (case_no,)
    print "Case #%s:" % (case_no,)

    R, C = map(int, raw_input().split())
    A = [list(raw_input()) for _ in xrange(R)]

    impossible = False
    for r in xrange(R):
        for c in xrange(C):
            if A[r][c] != '#': continue
            if r+1 == R or c+1 == C:
                impossible = True
                break
            ab = [(a, b) for a in (r, r+1) for b in (c, c+1)]
            if set([A[a][b] for a, b in ab]) != set('#'):
                impossible = True
                break
            for (a,b), v in zip(ab, r'/\\/'):
                A[a][b] = v
        if impossible:
            break
    if impossible:
        print "Impossible"
    else:
        for l in A:
            print ''.join(l)

