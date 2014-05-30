import sys
import collections
import itertools


for case_no in xrange(1, input() + 1):
    print >> sys.stderr, "Case #%s:" % (case_no,)
    print "Case #%s:" % (case_no,),

    M, N = map(int, raw_input().split())
    broken = [list(raw_input()) for _ in xrange(M)]

    def valid(state, prev):
        assert len(state) == len(prev) == N
        for i, s in enumerate(state):
            if s == 's':
                if i > 0 and (state[i-1] == 's' or prev[i-1] == 's'):
                    return False
                if i < N-1 and (state[i+1] == 's' or prev[i+1] == 's'):
                    return False
        return True

    def states(row):
        if not row:
            yield []
            return
        if row[0] == 'x':
            for p in states(row[1:]):
                yield ['x'] + p
            return
        assert row[0] == '.'

        for p in states(row[2:]):
            yield ['s'] + row[1:2] + p
        for p in states(row[1:]):
            yield row[0:1] + p


    mem = {}
    def solve(r, prev):
        k = (r, tuple(prev))
        if k in mem: return mem[k]
        if r == -1:
            return 0
        m = 0
        for state in states(broken[r]):
            if valid(state, prev):
                m = max(m, solve(r-1, state) +sum(c == 's' for c in state))
        mem[k] = m
        return m

    print solve(M-1, ['.'] * N)
