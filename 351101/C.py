import sys


T = {2: 'abc', 3: 'def', 4: 'ghi', 5: 'jkl', 6: 'mno', 7: 'pqrs', 8: 'tuv',
     9: 'wxyz', 0: ' '}

rev_t = {}
for k, letters in T.iteritems():
    for i, l in enumerate(letters):
        rev_t[l] = str(k) * (i+1)

for case_no in xrange(1, input() + 1):
    print >> sys.stderr, "Case #%s:" % (case_no,)
    print "Case #%s:" % (case_no,),

    msg = raw_input()
    s = [rev_t[l] for l in msg]

    g = ['x']
    for ch in s:
        if g[-1][-1] == ch[0]:
            g.append(' ')
        g.append(ch)
    print ''.join(g[1:])
