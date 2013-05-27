import sys


for case_no in xrange(1, input() + 1):
    print >> sys.stderr, "Case #%s:" % (case_no,)
    print "Case #%s:" % (case_no,),

    G = input()
    C = map(int, raw_input().split())

    x = set()
    for i in C:
        if i in x:
            x.remove(i)
        else:
            x.add(i)
    assert len(x) == 1
    print ''.join(str(i) for i in x)
