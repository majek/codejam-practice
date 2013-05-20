import sys
import itertools

MAX = 102


for case_no in xrange(1, input() + 1):
    print >> sys.stderr, "Case #%s:" % (case_no,)
    print "Case #%s:" % (case_no,),

    M = [[0] * MAX for _ in xrange(MAX)]

    R = input()
    for _ in xrange(R):
        x1, y1, x2, y2 = map(int, raw_input().split())
        for y in xrange(y1, y2+1):
            M[y][x1:x2+1] = [1] * (x2+1 - x1)

    for d in itertools.count(1):
        N = [[0] * MAX for _ in xrange(MAX)]
        b = False
        for x in xrange(MAX):
            for y in xrange(MAX):
                if M[x][y]:
                    if M[x-1][y] or M[x][y-1]:
                        N[x][y] = 1
                        b = True
                    if M[x+1][y-1]:
                        N[x+1][y] = 1
                        b = True
        M = N
        if not b:
            break
    print d

