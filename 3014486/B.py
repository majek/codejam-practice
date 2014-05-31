import sys
import string
import itertools

for case_no in xrange(1, input() + 1):
    print >> sys.stderr, "Case #%s:" % (case_no,)
    print "Case #%s:" % (case_no,),

    N = input()
    A = map(int, raw_input().split())

    m = max(A)
    mi = A.index(m)

    def count(l):
        c = 0
        while True:
            for i in xrange(len(l)-1):
                if l[i] > l[i+1]:
                    l[i+1], l[i] = l[i], l[i+1]
                    c += 1
                    break
            else:
                break
        return c

    mx = Ellipsis
    for s in itertools.chain(*(itertools.combinations(xrange(len(A)), l) for l in xrange(len(A)))):
        b = A[:]
        for x in s:
            if x != mi:
                b[x] = m + m - b[x]
        mx = min(mx, count([m + m - v for v in b]))
    print mx

