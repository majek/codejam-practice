import sys


def transpose(A):
    Y = len(A); X = len(A[0])
    B = [[None] * Y for _ in xrange(X)]
    for y in xrange(Y):
        for x in xrange(X):
            B[x][y] = A[y][x]
    return B

def find_symmetry(D, x):
    len_a = x
    len_b = (2*K - 1) - x - 1

    if not len_a or not len_b:
        return True

    l = min(len_a, len_b)
    for row in D:
        for v1, v2 in zip(row[x-l:x], row[x+1:x+l+1][::-1]):
            if v1 is not None and v2 is not None:
                if v1 != v2:
                    return False
    return True

def grow(a):
    return sum(2*k - 1 for k in xrange(K+1, K+a+1))


for case_no in xrange(1, input() + 1):
    print >> sys.stderr, "Case #%s:" % (case_no,)
    print "Case #%s:" % (case_no,),

    K = input()
    D = []
    for _ in xrange(K*2-1):
        row = [int(c) if c != ' ' else None
               for c in raw_input()]
        l = 2*K - 1 - len(row)
        if l:
            row += [None] * l
        D.append(row)

    D_p = transpose(D)
    X = [(x, find_symmetry(D, x)) for x in xrange(K*2-1)]
    Y = [(y, find_symmetry(D_p, y)) for y in xrange(K*2-1)]

    sym_x = [abs(K-1-x) for x, s in X if s]
    sym_y = [abs(K-1-y) for y, s in Y if s]

    print grow(min(sym_x) + min(sym_y))
