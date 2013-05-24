import sys

for case_no in xrange(1, input() + 1):
    print >> sys.stderr, "Case #%s:" % (case_no,)
    print "Case #%s:" % (case_no,),

    C_len, K, B, T = map(int, raw_input().split())
    X = map(int, raw_input().split())
    V = map(int, raw_input().split())

    C = zip(X, V)

    moves = 0
    while C and K > 0:
        x, v = C.pop()
        if x + v * T >= B:
            K -= 1
            continue
        moves += K

    print moves if K == 0 else "IMPOSSIBLE"
