import sys

for case_no in xrange(0, input()):
    print >> sys.stderr, "Case #%s:" % (case_no + 1,)
    print "Case #%s:" % (case_no + 1,),

    S = map(int, raw_input().split())[1:]
    total = float(sum(S))
    S = [s / total for s in S]
    S = dict(enumerate(S))
    ordered_cont = sorted(S.iteritems(), key=lambda (c, v): v)

    lower = set()
    idx = {}
    for c, v in ordered_cont:
        lower.add( c )
        idx[v] = set(lower)
    keys = sorted(idx.keys())

    r = [None] * len(S)
    for c, v in ordered_cont:
        last_cost = 0
        for k in keys:
            if k < v: continue
            max_v = k
            cost_to_even = sum(max_v - S[cc] for cc in idx[k])
            if cost_to_even > 1.:
                break
            else:
                avg_cost = max_v
                rem_cost = 1 - cost_to_even
                avg_cost = max_v + rem_cost / len(idx[k])
                last_cost = avg_cost - v
        r[c] = last_cost
    print ' '.join('%.6f' % (100.*v,) for v in r)

