'''
>>> t = IntervalTree()
>>> t
[]
>>> t.add(Interval(0, 2, 'a'))
[(0..2='a')]
>>> t.add(Interval(4, 6, 'b'))
[(0..2='a'), (4..6='b')]

>>> list(t.get(Interval(0, 2, None)))
[(0..2='a')]

>>> t
[(0..2='a'), (4..6='b')]
>>> t.update(Interval(1, 5, 'c'))
[(0..1='a'), (1..5='c'), (5..6='b')]

>>> list(t.get(Interval(1, 9, None)))
[(1..5='c'), (5..6='b')]

>>> t.update(Interval(1, 9, 'e'))
[(0..1='a'), (1..9='e')]
>>> t.update(Interval(2, 3, 'f'))
[(0..1='a'), (1..2='e'), (2..3='f'), (3..9='e')]


>>> t = IntervalTree()
>>> t.update(Interval(-25,61,326))
[(-25..61=326)]
>>> list(t.get(Interval(-32, 54, None)))
[(-25..61=326)]
>>> t.update(Interval(-32,54,387))
[(-32..54=387), (54..61=326)]
'''
import collections
import bintrees
import sys


def interval_intersect(i, j):
    '''
    >>> interval_intersect(Interval(0,1, None), Interval(1,2, None)) is None
    True
    >>> interval_intersect(Interval(1,2, None), Interval(0,1, None)) is None
    True
    >>> interval_intersect(Interval(1,4, None), Interval(2,3, None))
    (2..3=None)
    >>> interval_intersect(Interval(1,4, None), Interval(1,3, None))
    (1..3=None)
    >>> interval_intersect(Interval(1,4, None), Interval(0,4, None))
    (1..4=None)
    >>> interval_intersect(Interval(1,4, None), Interval(0,2, None))
    (1..2=None)
    >>> interval_intersect(Interval(1,4, None), Interval(3,5, None))
    (3..4=None)
    >>> interval_intersect(Interval(1,9, None), Interval(5,6, None))
    (5..6=None)
    >>> interval_intersect(Interval(5,6, None), Interval(1,9, None))
    (5..6=None)
    >>> interval_intersect(Interval(-32,54, None), Interval(-25,61, None))
    (-25..54=None)
    >>> interval_intersect(Interval(-25,61, None), Interval(-32,54, None))
    (-25..54=None)
    '''
    if i.b <= j.a or j.b <= i.a:
        return None
    if i.a < j.a:
        l = j.a
    else:
        l = i.a

    if j.b < i.b:
        r = j.b
    else:
        r = i.b
    return Interval(l, r, None)

def interval_subtract(i, j):
    '''
    >>> interval_subtract(Interval(0, 2, 'a'), Interval(1, 2, None))
    [(0..1='a')]
    >>> interval_subtract(Interval(0, 2, 'a'), Interval(0, 1, None))
    [(1..2='a')]
    >>> interval_subtract(Interval(5, 6, 'a'), Interval(5, 6, None))
    []
    >>> interval_subtract(Interval(0, 6, 'a'), Interval(1, 4, None))
    [(0..1='a'), (4..6='a')]
    >>> interval_subtract(Interval(-25,61, None), Interval(-25,54, None))
    [(54..61=None)]
    '''
    if j.a == i.a and j.b == i.b:
        return []
    if j.a == i.a:
        #assert j.b < i.b
        return [Interval(j.b, i.b, i.v)]
    if j.b == i.b:
        #assert i.a < j.a
        return [Interval(i.a, j.a, i.v)]
    if i.a < j.a and j.b < i.b:
        return [Interval(i.a, j.a, i.v), Interval(j.b, i.b, i.v)]
    assert False, (i, j)

Interval = collections.namedtuple('Interval', ['a', 'b', 'v'])
Interval.__repr__ = lambda self:'(%s..%s=%r)' % (self.a, self.b, self.v)

class IntervalTree(object):
    def __init__(self):
        self.t = bintrees.FastAVLTree()

    def get(self, ival):
        t = self.t
        try:
            _, i = t.floor_item(ival.a)
        except KeyError:
            try:
                _, i = t.min_item()
            except ValueError:
                i = None
        while i is not None:
            if i.a >= ival.b:
                break
            if ival.a <= i.a < ival.b or ival.a < i.b < ival.b or (i.a <= ival.a and ival.b <= i.b) :
                yield i
            try:
                _, i = t.succ_item(i.a)
            except KeyError:
                i = None

    def get2(self, ival):
        # Not sure why, but it's _way_ slower
        t = self.t
        try:
            _, i = t.floor_item(ival.a)
        except KeyError:
            try:
                _, i = t.min_item()
            except ValueError:
                return

        for _, i in t.itemslice(i.a, ival.b):
            if ival.a <= i.a < ival.b or ival.a < i.b < ival.b or (i.a <= ival.a and ival.b <= i.b) :
                yield i

    def delete(self, ival):
        del self.t[ival.a]
        return self

    def add(self, ival):
        t = self.t
        t[ival.a] = ival
        return self

    def update(self, ival):
        for i in list(self.get(ival)):
            self.delete(i)
            inter = interval_intersect(ival, i)
            if inter is None: assert False
            for sub in interval_subtract(i, inter):
                self.add(sub)
        self.add(ival)
        return self

    def __repr__(self):
        return '[' + ', '.join(repr(i) for i in self.t.values()) + ']'

    def fill(self, ival):
        l = ival.a
        for i in self.get(ival):
            if l < i.a:
                yield Interval(l, i.a, ival.v)
            inter = interval_intersect(ival, i)
            yield Interval(inter.a, inter.b, i.v)
            l = inter.b
        if l < ival.b:
            yield Interval(l, ival.b, ival.v)

    # def smaller(self, ival):
    #     for i in self.fill(Interval(ival.a, ival.b, None)):
    #         if i.v < ival.v:
    #             return True
    #     return False

    # def bump(self, ival):
    #     u = []
    #     for i in self.fill(Interval(ival.a, ival.b, None)):
    #         if i.v < ival.v:
    #             u.append( Interval(i.a, i.b, ival.v) )
    #     for i in u:
    #         self.update(i)
    #     return self

    # def merge(self):
    #     for 
    #     ival = Interval(ival.a, ival.b, ival.v)
    #         try:
    #             _, p = t.prev_item(ival.a)
    #         except KeyError:
    #             p = None
    #         try:
    #             _, n = t.succ_item(ival.a)
    #         except KeyError:
    #             n = None
    #         if p and p.v == ival.v and p.b == ival.a:
    #             self.delete(p)
    #             ival.a = p.a
    #         if n and n.v == ival.v and n.a == ival.b:
    #             self.delete(n)
    #             ival.b = n.b
