import sys
# ulimit -s 9000000
# sys.setrecursionlimit(900000)

def precompute(c_prob):
    mem = {}
    s = 1.
    for i, v in enumerate(c_prob):
        s *= v
        mem[i] = s
    return mem

for case_no in xrange(0, input()):
    print >> sys.stderr, "Case #%s:" % (case_no + 1,)
    print "Case #%s:" % (case_no + 1,),

    A, B = map(int, raw_input().split())
    c_prob = map(float, raw_input().split())

    enter_keys = 1 + B + 1

    min_cost = enter_keys

    mem = precompute(c_prob)

    to_type = B - A
    for wrong_chars in range(0, A):
        to_type = B - A + 2 * wrong_chars
        ok_prob = mem[A - wrong_chars -1]
        keep_on = ok_prob * (to_type + 1) + \
            (1. - ok_prob) * (to_type + 1 + B + 1)
        if keep_on < min_cost:
            min_cost = keep_on

    print '%.6f' % (min_cost,)
