import sys


def derive(i, t, j, k):
    if t in 'TL':
        def xx(F):
            x = (F[i], t)
            if x == (True, 'T') or x == (False, 'L'):
                return [(j, True)]
            elif x == (True, 'L') or x == (False, 'T'):
                return [(j, False)]
            return []
    elif t in 'SD':
        def xxx(F):
            return []
        def xx(F):
            jj, kk = j, k
            if F[jj] is None and F[kk] is None:
                return []
            if F[jj] is None:
                jj, kk = kk, jj
            assert F[jj] is not None
            first_town = F[jj]
            x = (F[i], t)
            if x == (True, 'S') or x == (False, 'D'):
                return [(kk, first_town)]
            elif x == (True, 'D') or x == (False, 'S'):
                return [(kk, not first_town)]
            return []
    return xx

def rev_derive(i, t, j, k):
    if t in 'TL':
        def xx(F):
            if F[j] in (True, False):
                x = (t, F[j])
                if x == ('T', True) or x == ('L', False):
                    return [(i, True)]
                elif x == ('L', True) or x == ('T', False):
                    return [(i, False)]
            return []
    elif t in 'SD':
        def xx(F):
            if F[j] is None or F[k] is None:
                return []
            same_towns = F[j] == F[k]
            x = (t, same_towns)
            if x == ('S', True) or x == ('D', False):
                return [(i, True)]
            elif x == ('D', True) or x == ('S', False):
                return [(i, False)]
            return []
    return xx


def propagate(F, i):
    xs = []
    for fun in I[i]:
        xs += fun(F)
    for (i, val) in xs:
        if F[i] is None:
            F[i] = val
            if not propagate(F, i):
                return None
        elif F[i] != val:
            return None
    return F

def solve(F, s=0):
    '''
    while None in F:
        for i in xrange(N):
            if F[i] is not None:
                continue
            F[i] = True
            Ft = propagate(F[:], i)
            F[i] = False
            Ff = propagate(F[:], i)
            F[i] = None

            yes = False
            #print i, F, Ft, Ff
            if Ft and Ff:
                for j, (a, b) in enumerate(zip(Ft, Ff)):
                    if a is not None and a == b:
                        if F[j] is None:
                            F[j] = a
                            F = propagate(F[:], j)
                            assert F is not None
                            yes = True
                        assert F[j] == a
                        assert propagate(F[:], j) is not None
                if yes:
                    break
            elif Ft or Ff:
                f = Ft or Ff
                F[i] = f[i]
                F = propagate(F, i)
                assert F is not None
                break
        else:
            # Not changed anything
            break
    '''
    if None in F:
        for i in xrange(s, N):
            if F[i] is not None:
                continue
            F[i] = True
            Ft = propagate(F[:], i)
            F[i] = False
            Ff = propagate(F[:], i)
            F[i] = None
            if Ft and Ff:
                Fa = solve(Ft, i+1)
                Fb = solve(Ff, i+1)
                if Fa and Fb:
                    for j, (a, b) in enumerate(zip(Ft, Ff)):
                        if a is not None and a == b and F[j] is None:
                            F[j] = a
                            F = propagate(F[:], j)
                            assert F
                            return solve(F, i+1)

            elif Ft or Ff:
                F[i] = bool(Ft)
                F = propagate(F[:], i)
                return solve(F, i+1)
    return F


for case_no in xrange(1, input() + 1):
    print >> sys.stderr, "Case #%s:" % (case_no,)
    print "Case #%s:" % (case_no,),

    N, M = map(int, raw_input().split())

    I = [list() for _ in xrange(N)]
    S = []
    for _ in xrange(M):
        e = raw_input().split()
        i = int(e[0]) - 1
        t = e[1]
        j = int(e[2]) - 1
        k = None if len(e) == 3 else int(e[3]) - 1
        stmt = (i,t,j,k)
        S.append( stmt )
        I[i].append( derive(*stmt) )
        rd = rev_derive(*stmt)
        I[j].append( rd )
        if k is not None:
            I[k].append( rd )
    dd = {None:'-', False:'L', True:'T'}
    F = [None] * N
    print ' '.join(dd[v] for v in solve(F))
