import sys

GATE_AND=-1
GATE_OR=-2

def plus(a,b):
    if a is Ellipsis or b is Ellipsis:
        return Ellipsis
    return a + b


for case_no in xrange(1, input() + 1):
    print >> sys.stderr, "Case #%s:" % (case_no,)
    print "Case #%s:" % (case_no,),

    M, V = map(int, raw_input().split())

    CH = [None] * M
    GT = [None] * M
    for m in xrange(M):
        r = map(int, raw_input().split())
        if len(r) == 2:
            G, C = r
            GT[m] = GATE_AND if G == 1 else GATE_OR
            CH[m] = bool(C)
        else:
            GT[m] = r[0]

    def solve(m):
        gt = GT[m]
        if gt is 0:
            return [0, Ellipsis]
        if gt is 1:
            return [Ellipsis, 0]
        l_f, l_t = solve(2*m+1)
        r_f, r_t = solve(2*m+2)

        cost_and = [min(l_f, r_f), plus(l_t, r_t)]
        cost_or = [plus(l_f, r_f), min(l_t, r_t)]
        if CH[m] == False:
            if gt is GATE_AND:
                return cost_and
            else:
                return cost_or
        if gt is GATE_AND:
            return min(cost_and[0], plus(cost_or[0], 1)), min(cost_and[1], plus(cost_or[1], 1))
        else:
            return min(plus(cost_and[0], 1), cost_or[0]), min(plus(cost_and[1], 1), cost_or[1])

    r = solve(0)[V]
    if r is Ellipsis:
        print "IMPOSSIBLE"
    else:
        print r
