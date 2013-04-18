import sys
import array
import itertools

sys.setrecursionlimit(10000)

class E(Exception): pass

for case_no in xrange(1, input() + 1):
    print >> sys.stderr, "Case #%s:" % (case_no ,)
    print "Case #%s:" % (case_no ,),

    C = input()
    childs = [list() for _ in xrange(C)]
    for child in xrange(C):
        for parent in map(lambda s:int(s)-1, raw_input().split()[1:]):
            childs[parent].append( child )

    parents_map = {}
    def parents(i):
        if i not in parents_map:
            def chain():
                yield childs[i][:]
                for p in childs[i]:
                    yield parents(p)
            parents_map[i] = array.array('I', itertools.chain(*chain()))
            if len(parents_map[i]) != len(set(parents_map[i])):
                raise E()
        return parents_map[i]

    for i in xrange(len(childs)):
        try:
            parents(i)
        except E:
            print 'Yes'
            break
    else:
        print 'No'
