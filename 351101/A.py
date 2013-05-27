import sys
import collections


for case_no in xrange(1, input() + 1):
    print >> sys.stderr, "Case #%s:" % (case_no,)
    print "Case #%s:" % (case_no,),

    C = input()
    I = input()
    P = map(int, raw_input().split())

    dd = collections.defaultdict(set)
    for i, v in enumerate(P):
        dd[v].add(i)

    for i, v in enumerate(P):
        delta = C - v
        if dd[delta] - set((i,)):
            sol = dd[delta] | set((i,))
            print min(sol)+1, max(sol)+1
            break
    else:
        assert False

