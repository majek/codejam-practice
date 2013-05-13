import sys


def solve(A, idx):
    if idx == N:
        return 0
    m = M[idx]
    if A > m: # Absorb
        return solve(A+m, idx+1)
    else:
        if A > 1:
            c = 0; Ad = A
            while Ad <= m:
                Ad += Ad-1
                c += 1
            assert Ad > m
            return min([solve(Ad+m, idx+1) + c,
                        solve(A, idx+1) + 1,])
        else:
            return solve(A, idx+1) + 1

for case_no in xrange(1, input() + 1):
    print >> sys.stderr, "Case #%s:" % (case_no,)
    print "Case #%s:" % (case_no,),

    A, N = map(int, raw_input().split())
    M = map(int, raw_input().split())

    M.sort()

    mem = {}
    print solve(A, 0)
