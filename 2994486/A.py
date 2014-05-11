import sys

def parse(s):
    a = []
    cc = None
    count = 0
    for c in s:
        if c == cc:
            count += 1
        else:
            if cc:
                a.append( (cc, count) )
            cc = c
            count = 1
    a.append( (cc, count) )
    return a

for case_no in xrange(1, input() + 1):
    print "Case #%s:" % (case_no,),

    S = [parse(raw_input()) for _ in xrange(input())]
    l = max(map(len, S))
    for k in S:
        if len(k) != l:
            print "Fegla Won"
            break
    else:
        ct = 0
        for i in xrange(l):
            kk = [s[i][0] for s in S]
            vv = sorted([s[i][1] for s in S])
            if len(set(kk)) != 1:
                print "Fegla Won"
                break
            else:
                #print >>sys.stderr, l, vv, S
                avg = vv[len(vv)/2]
                for v in vv:
                    ct += abs(v - avg)
        else:
            print ct
