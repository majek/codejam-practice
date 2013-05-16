import sys


for case_no in xrange(1, input() + 1):
    print >> sys.stderr, "Case #%s:" % (case_no,)
    print "Case #%s:" % (case_no,),

    N = input()
    P = []
    S = []
    for _ in xrange(N):
        p, s = map(int, raw_input().split())
        P.append(p)
        S.append(s)
    T = input()

    M = [Ellipsis] * N
    for i in xrange(N):
        dist = T - P[i]
        if dist <= S[i]:
            M[i] = dist

    for i in xrange(N-1, 0-1, -1):
        min_swing = M[i]
        if min_swing is Ellipsis: continue
        for j in xrange(i-1, 0-1, -1):
            dist = P[i] - P[j]
            if dist < min_swing:
                continue
            if dist > S[j]:
                continue
            M[j] = min(M[j], dist)

    print 'YES' if M[0] <= P[0] else 'NO'

