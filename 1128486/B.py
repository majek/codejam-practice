import sys


def build(t, t_noaccel):
    wait = max(0, T - t)
    assert wait < t_noaccel
    speedup = t_noaccel - wait
    return wait + speedup / 2

def solve(L, idx, t):
    if idx == N:
        return t
    if L == 0: # no speed boosters available
        r = t + sum(A[idx:])
    elif t >= T and L >= N - idx: # plenty remaining - always build
        r = t + sum(A[idx:]) / 2
    elif t >= T:
        a = sorted(A[idx:], reverse=True)
        r = t + sum(a[:L])/2 + sum(a[L:])
    else:
        r = min(solve(L-1, idx + 1, t + build(t, A[idx])),
                solve(L, idx + 1, t + A[idx]))
    return r

for case_no in xrange(1, input() + 1):
    print >> sys.stderr, "Case #%s:" % (case_no,)
    print "Case #%s:" % (case_no,),

    line = map(int, raw_input().split())
    L, T, N, _ = line[:4]
    A = map(lambda a:a*2, line[4:])
    while len(A) < N: A = A + A
    A = A[:N]

    idx = 0; t = 0
    while idx < N:
        # will arrive at next star before it finishes buildin
        if t + A[idx] <= T:
            t += A[idx]
            idx += 1
        else:
            break
    print solve(L, idx, t)
