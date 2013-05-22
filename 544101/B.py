import sys


def solve(costs, idx):
    if idx == A_len:
        return costs

    v = A[idx]

    # 1) Try to delete v
    c = [costs[i] + D for i in xrange(256)]

    # 2) Change value to i. Cost of change + minimum on the left.
    # This also covers not-changing anything.
    for i in xrange(256):
        c[i] = min(c[i], abs(i-v) +
                   min(costs[j] for j in xrange(max(0, i-M), min(256, i+M+1))))

    # 3) Insert stuff after
    if M:
        for i in xrange(256):
            for j in xrange(256):
                ins, rest = divmod(abs(i-j), M)
                c[i] = min(c[i], c[j] + (ins + int(bool(rest))) * I)

    return solve(c, idx+1)

for case_no in xrange(1, input() + 1):
    print >> sys.stderr, "Case #%s:" % (case_no,)
    print "Case #%s:" % (case_no,),

    D, I, M, A_len = map(int, raw_input().split())
    A = map(int, raw_input().split())

    print min(solve([0] * 256, 0))
