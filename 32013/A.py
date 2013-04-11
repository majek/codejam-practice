
for case_no in xrange(input()):
    S = [raw_input() for _ in xrange(input())]
    Q = [raw_input() for _ in xrange(input())]
    S = set(S)

    s = set(S)
    r = 0
    for q in Q:
        if q in s:
            s.remove(q)
            if not s:
                s = set(S)
                s.remove(q)
                r += 1

    print "Case #%s: %s" % (case_no + 1, r)

