import sys
import itertools
import bisect


def war(N, K):
    apts = 0
    for n in N:
        i = bisect.bisect_left(K, n)
        if i == len(K):
            K = K[1:]
            apts += 1
            continue
        if i < len(K):
            assert K[i] > n
        if i > 0:
           assert K[i-1] <= n
        K = K[:i] + K[i+1:]
    return apts


def dwar(N, K):
    apts = 0
    while N:
        if K[0] < N[0]:
            apts += 1
            K = K[1:]
            N = N[1:]
            continue
        elif N[0] > K[-1]:
            apts += 1
        N = N[1:]
        K = K[:-1]
    return apts


for case_no in xrange(1, input() + 1):
    print "Case #%s:" % (case_no,),
    raw_input()

    N = sorted(map(float, raw_input().split()))
    K = sorted(map(float, raw_input().split()))


    print dwar(N[:], K[:]), war(N[:], K[:])
