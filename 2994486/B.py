import sys

for case_no in xrange(1, input() + 1):
    print "Case #%s:" % (case_no,),

    A, B, K = map(int, raw_input().split())

    A, B = min(A,B), max(A,B)
    k = set(xrange(K))

    print sum(1 if i & j in k else 0 for i in xrange(A) for j in xrange(B))
