import sys


for case_no in xrange(1, input() + 1):
    print >> sys.stderr, "Case #%s:" % (case_no,)
    print "Case #%s:" % (case_no,),

    N, M = map(int, raw_input().split())
    Exists = {raw_input() for _ in xrange(N)}
    Create = [raw_input() for _ in xrange(M)]

    Exists.add('')

    ans = 0
    for s in Create:
        assert s[-1] != '/'
        assert s[0] == '/'
        parts = []
        for part in s.split('/'):
            parts.append( part )
            p = '/'.join(parts)
            if p not in Exists:
                ans += 1
                Exists.add(p)

    print ans
