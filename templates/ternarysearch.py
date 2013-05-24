# http://en.wikipedia.org/wiki/Ternary_search


def ternarysearch_min(l, r):
    assert r > l
    if r - l < 0.000000001:
        return (l+r) / 2.
    lt = (2*l + r) / 3.
    rt = (l + 2*r) / 3.
    if swarm(lt) > swarm(rt):
        return ternarysearch_min(lt, r)
    else:
        return ternarysearch_min(l, rt)
