def is_happy(c, cream):
    for i, malted in c:
        if cream[i] == malted:
            return True
    if c[-1][1] == True:
        return c[-1][0]
    else:
        return False

def solve(cream, customers):
    while True:
        for c in customers:
            v = is_happy(c, cream)
            if v is True:
                continue
            elif v is False:
                return None
            else:
                cream[v] = True
                break
        else:
            return cream

for case_no in xrange(0, input()):
    print "Case #%s:" % (case_no + 1,),

    N = input()
    M = input()
    customers = []
    for _ in xrange(M):
        satisfy = []
        l = [int(v) for v in raw_input().split()]
        for i in range(1, l[0]*2+1, 2):
            satisfy.append( (l[i]-1, bool(l[i+1])) )
        customers.append(sorted(satisfy, key=lambda (a,b): b))
    mem = {}
    r = solve([False] * N, customers,)
    if r:
        print ' '.join(i and '1' or '0' for i in r)
    else:
        print 'IMPOSSIBLE'
