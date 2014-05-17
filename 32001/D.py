import sys
import itertools


def permute(p, g):
    return list(g[j] for j in p)


for case_no in xrange(1, input() + 1):
    print >> sys.stderr, "Case #%s:" % (case_no,)
    print "Case #%s:" % (case_no,),

    k = input()
    S = raw_input()
    G = [S[i:i+k] for i in xrange(0, len(S), k)]

    min_l = Ellipsis
    for p in itertools.permutations(range(k), k):
        min_l = min(min_l,
                    len(list(itertools.groupby(itertools.chain(*(permute(p, g) for g in G))))))

    print min_l
