
def parse(s):
    a, b = [int(v) for v in s.split(':', 1)]
    return a*60 + b


for case_no in xrange(input()):
    T = input()
    NA_ct, NB_ct = [int(v) for v in raw_input().split()]
    NA = []; NB = []
    A = []; B = []
    for _ in range(NA_ct):
        dep, arr = [parse(v) for v in raw_input().split()]
        A.append( (dep, -1) )
        B.append( (arr+T, 1) )
        NA.append( (dep, arr) )
    for _ in range(NB_ct):
        dep, arr = [parse(v) for v in raw_input().split()]
        B.append( (dep, -1) )
        A.append( (arr+T, 1) )
        NB.append( (dep, arr) )

    A.sort(key=lambda (a,b): (a, -b))
    B.sort(key=lambda (a,b): (a, -b))
    ma = 0; d = 0
    for t, v in A:
        d += v
        ma = min(d, ma)
    mb = 0; d = 0
    for t, v in B:
        d += v
        mb = min(d, mb)

    print "Case #%s: %s %s" % (case_no + 1, -ma, -mb)

