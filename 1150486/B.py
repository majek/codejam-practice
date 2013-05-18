import collections
import itertools
import sys
import math
from pprint import pprint as pp


def transpose(A):
    R = len(A); C = len(A[0])
    B = [[None] * R for _ in xrange(C)]

    for r in xrange(R):
        for c, v in enumerate(A[r]):
            B[c][r] = v
    return B

def sum_matrix(A, k):
    R = len(A); C = len(A[0])
    B = [[None] * (C-k+1) for _ in xrange(R-k+1)]

    pr = 0
    for c in xrange(0, C-k+1):
        if c == 0:
            ss = sum(sum(A[r][c:c+k]) for r in xrange(0, k-1))
            pr = ss
        else:
            ss = pr + sum(-A[r][c-1] + A[r][c+k-1] for r in xrange(0, k-1))
            pr = ss
        for r in xrange(0, R-k+1):
            ss += sum(A[r+k-1][c:c+k])
            B[r][c] = ss - A[r][c] - A[r+k-1][c+k-1] - A[r+k-1][c] - A[r][c+k-1]
            ss -= sum(A[r][c:c+k])
    return B

def pos_matrix(A, off):
    t = [c + off for c in xrange(len(A[0]))]
    return [[v * c for c, v in itertools.izip(A[r], t)] for r in xrange(len(A))]


def solve(k):
    xs = sum_matrix(pos_X, k)
    xd = pos_matrix(sum_matrix(X, k), (k-1) / 2.)

    ys = sum_matrix(pos_Y, k)
    yd = pos_matrix(sum_matrix(Y, k), (k-1) / 2.)

    for r in xrange(R-k+1):
        for c in xrange(C-k+1):
            if xs[r][c] == xd[r][c] and ys[c][r] == yd[c][r]:
                return True


for case_no in xrange(1, input() + 1):
    print >> sys.stderr, "Case #%s:" % (case_no,)
    print "Case #%s:" % (case_no,),

    R, C, D = map(int, raw_input().split())

    W = [map(int, list(raw_input())) for _ in xrange(R)]
    X = W
    Y = transpose(W)

    pos_X = pos_matrix(X, 0)
    pos_Y = pos_matrix(Y, 0)

    for k in xrange(min(R, C), 3-1, -1):
        if solve(k):
            print k
            break
    else:
        print "IMPOSSIBLE"
