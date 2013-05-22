import sys


for case_no in xrange(1, input() + 1):
    print >> sys.stderr, "Case #%s:" % (case_no,)
    print "Case #%s:" % (case_no,),

    N = input()

    A = []
    for _ in xrange(N):
        row = raw_input()
        z = 0
        for c in row[::-1]:
            if c == '0':
                z += 1
            else:
                break
        A.append( N - z )


    s = 0; q = None
    while s != q:
        q = s
        for i in xrange(N-1):
            if A[i] > i+1:
                for j in xrange(i+1, N):
                    if A[j] <= i+1:
                        for k in xrange(j-1, i-1, -1):
                            A[k], A[k+1] = A[k+1], A[k]
                            s += 1
                        break
    print s
