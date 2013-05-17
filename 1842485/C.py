import sys


def solve(a):
    b = X[a]
    t = (H[b] - H[a]) / (b-a)
    if b - a == 1:
        return True

    c = a + 1
    while True:
        assert H[c] is None
        H[c] = H[b] - (t+1)*(b-c)
        c = X[c]
        if c > b:
            return False
        if c == b:
            break
    return True


for case_no in xrange(1, input() + 1):
    print >> sys.stderr, "Case #%s:" % (case_no,)
    print "Case #%s:" % (case_no,),

    N = input()
    X = map(lambda s:int(s)-1, raw_input().split())

    H = [None] * N
    H[0] = 10**6


    p = 0
    while p < N-1:
        H[X[p]] = 10**6
        p = X[p]

    impossible = False
    for p in xrange(N-1):
        if H[p] is None:
            if not solve(p-1):
                impossible = True
                break

    if impossible:
        print "Impossible"
    else:
        print ' '.join(map(str, H))
