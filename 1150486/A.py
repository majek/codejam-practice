import sys


for case_no in xrange(1, input() + 1):
    print >> sys.stderr, "Case #%s:" % (case_no,)
    print "Case #%s:" % (case_no,),

    X, Ws, Rs, Rt, N = map(int, raw_input().split())

    C = [map(int, raw_input().split()) for _ in xrange(N)]

    assert Rs >= Ws

    ds = []
    s = 0
    for b, e, sp in C:
        if b-s:
            ds.append( (s, b-s, 0) )
        ds.append( (b, e-b, sp) )
        s = e
    if s < X:
        ds.append( (s, X-s, 0) )
    assert ds[0][0] == 0 and ds[-1][0] + ds[-1][1] == X

    ds.sort(key=lambda (s,d,sp): sp)
    t = 0.
    for s, d, sp in ds:
        wspeed = float(Ws + sp)
        rspeed = float(Rs + sp)
        rdist = min(Rt * rspeed, d)
        if rdist > 0:
            rt = rdist / rspeed
            Rt -= rt
            wt = (d-rdist) / wspeed
        else:
            rt = 0
            wt = d / wspeed
        t += rt + wt
    print '%.6f' % (t,)
