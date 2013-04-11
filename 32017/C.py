import math
import itertools


class Heap(object):
    def __init__(self, init):
        self.N = len(init)
        self.R = int(math.ceil(math.log(self.N, 2)))
        self.offset = (2**self.R)
        self.a = [0] * self.offset
        self.a += init
        self.a[0] = None

        for a, b in itertools.izip_longest(xrange(0, self.N, 2), xrange(1, self.N, 2)):
            s = self.a[self.offset + a] + \
                (self.a[self.offset + b] if b is not None else 0)
            self.a[2**(self.R-1) + a / 2] = s
        for r in range(self.R-2, -1, -1):
            for i in range(2**r):
                self.a[2**r + i] = \
                    self.a[2**(r+1) + i*2] + self.a[2**(r+1) + i*2 + 1]

    def p(self):
        for l in range(self.R):
            print '#%i' % (l,), self.a[2**l: 2**(l+1)]
        print '#I', self.a[self.offset:self.offset+self.N]

    def add(self, n, v):
        self.a[self.offset + n] += v
        for r in range(self.R-1, -1, -1):
            n /= 2
            self.a[2**r + n] += v

    def total(self):
        return self.a[1]

    def find(self, v):
        assert v < self.a[1]
        o = 0
        for r in range(1, self.R+1):
            o *= 2
            if v < self.a[2**r+o]:
                o += 0
            else:
                v -= self.a[2**r+o]
                o += 1
        return o


for case_no in xrange(0, input()):
    print "Case #%s:" % (case_no + 1,),

    K = input()
    D = map(int, raw_input().split())[1:]


    h = Heap([1 for x in xrange(K)])
    res = [None for x in xrange(K)]
    c = 0
    for i in xrange(K):
        c = (c + i) % h.total()
        idx = h.find(c)
        h.add(idx, -1)
        res[idx] = i

    print ' '.join([str(res[d-1]+1) for d in D])
