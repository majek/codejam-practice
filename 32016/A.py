for case_no in xrange(0, input()):
    print "Case #%s:" % (case_no + 1,),

    _ = input()
    A = [int(v) for v in raw_input().split()]
    B = [int(v) for v in raw_input().split()]
    A.sort()
    B.sort(reverse=True)
    r = sum(a*b for a, b in zip(A,B))
    print r
