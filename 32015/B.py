from collections import defaultdict

def filter_ugly(f):
    s = 0
    for v, n in f.iteritems():
        if v % 2 == 0 or v % 3 == 0 or v % 5 == 0 or v % 7 == 0:
            s += n
    return s

mem = None
def solve(prefix, elements):
    k = (prefix, elements)
    if k in mem:
        return mem[k]
    if len(elements) == 1:
        return {int(prefix + elements[0]): 1}
    r = defaultdict(lambda:0)
    e = elements[0]
    els = tuple(elements[1:])

    for v, n in solve('', els).iteritems():
        a = int(prefix+e)
        r[(a + v) % 210] += n
        r[(a - v) % 210] += n
    for v, n in solve(prefix + e, els).iteritems():
        r[v % 210] += n
    mem[k] = r
    return r


for case_no in xrange(0, input()):
    print "Case #%s:" % (case_no + 1,),
    value = [c for c in raw_input()]

    mem = {}
    f = solve('', tuple(value))
    print filter_ugly(f)
