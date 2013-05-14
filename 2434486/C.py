import sys
sys.setrecursionlimit(10000)


prefix_tree = {}
with open("garbled_email_dictionary.txt") as fd:
    for word in fd.read().split():
        tree = prefix_tree
        for c in word:
            tree = tree.setdefault(c, {})
        tree['#'] = word

print >> sys.stderr, "[*] Loaded!"


def _solve(msg, tree, change):
    if not msg:
        return (0 if '#' in tree else Ellipsis)

    C = msg[0]
    r = []
    if change > 0:
        # no changes
        if C in tree:
            r.append( (tree[C], change - 1, 0) )
        if '#' in tree and C in prefix_tree:
            r.append( (prefix_tree[C], change - 1, 0) )
    else:
        # changes possible
        for c in tree:
            if c != '#':
                # letter
                if c == C:
                    r.append( (tree[c], 0, 0) )
                else:
                    r.append( (tree[c], 4, 1) )
            else:
                # new word
                for d in prefix_tree:
                    if d == C:
                        r.append( (prefix_tree[d], 0, 0) )
                    else:
                        r.append( (prefix_tree[d], 4, 1) )

    best = Ellipsis
    nmsg = msg[1:]
    for ntree, nchange, cost in r:
        if best > cost:
            x = solve(nmsg, ntree, nchange)
            if x is not Ellipsis:
                best = min(best, x + cost)
    return best

def solve(message, tree, change):
    k = (message, id(tree), change)
    if k not in mem:
        mem[k] = _solve(message, tree, change)
    return mem[k]


for case_no in xrange(1, input() + 1):

    print >> sys.stderr, "Case #%s:" % (case_no,)
    print "Case #%s:" % (case_no,),

    S = raw_input()

    mem = {}
    print solve(S, prefix_tree, 0)
