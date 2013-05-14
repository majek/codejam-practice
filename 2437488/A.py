import collections
import itertools
import sys
import math


# run length encoding
def count_and_group(l):
    '''
    >>> count_and_group([1])
    [(1, 1)]
    >>> count_and_group([0])
    [(1, 0)]
    >>> count_and_group([0,0,1,0,0,1,1,1,0,0])
    [(2, 0), (1, 1), (2, 0), (3, 1), (2, 0)]
    '''
    return [(len(list(g)), k) for k, g in itertools.groupby(l)]

def group_bad(list_of_a, n):
    '''
    >>> list(group_bad(count_and_group([0,0,0,1,0,1,1,0,1,1,1,0,1,1,1,1,1,0,1,1,1]), 3))
    [(8, False), (3, True), (1, False), (5, True), (1, False), (3, True)]
    '''
    bad = 0
    for ct, v in list_of_a:
        if v and ct >= n:
            if bad: yield (bad, False)
            yield (ct, True)
            bad = 0
        else:
            bad += ct
    if bad: yield (bad, False)

def dupa(counts, n):
    l = 0
    a = []
    for i in xrange(len(counts)):
        fct, fv = counts[i]
        for k in xrange(fct):
            if fv and fct - k >= n:
                a.append( l + k + n)
            else:
                ll = l + fct
                for j in xrange(i+1, len(counts)):
                    ct, v = counts[j]
                    if v:
                        a.append( ll + n )
                        break
                    ll += ct
                else:
                    a.append( None )
        l += fct
    return a

def solve():
    s = 0
    for i in xrange(total):
        if D[i] != None:
            s += total - (D[i] -1)
    return s

if __name__ == '__main__':
    for case_no in xrange(1, input() + 1):
        print >> sys.stderr, "Case #%s:" % (case_no,)
        print "Case #%s:" % (case_no,),

        L, n = raw_input().split()
        n = int(n)
        vowels = set('aeiou')
        new_l = [int(c not in vowels) for c in L]

        counts = list(group_bad(count_and_group(new_l), n))
        total = len(L)
        D = dupa(counts, n)
        assert len(D) == total
        print solve()
