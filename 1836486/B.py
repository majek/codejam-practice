import sys
import bintrees


class PriorityQueue(object):
    def __init__(self):
        self.d = {}
        self.i = bintrees.FastAVLTree()

    def get(self, key, default=None):
        return self.d.get(key, default)

    def __setitem__(self, key, value):
        prev_v = self.d.get(key, None)
        if prev_v is not None:
            self.i[prev_v].remove( key )
            if not self.i[prev_v]:
                del self.i[prev_v]
        self.d[key] = value
        self.i.setdefault(value, set()).add( key )

    def pop(self):
        v, list_of_keys = self.i.min_item()
        key = list_of_keys.pop()
        if not list_of_keys:
            del self.i[v]
        del self.d[key]
        return key, v

    def __len__(self):
        return len(self.d)


def connected((r, c)):
    ns = [(a, b) for a, b in [(r-1, c), (r+1, c), (r, c-1), (r, c+1)] \
              if 0 <= a < N and 0 <= b < M]
    for a, b in ns:
        if (Floor[r][c] + 50 <= Ceil[a][b] and
            Floor[a][b] + 50 <= Ceil[a][b] and
            Floor[a][b] + 50 <= Ceil[r][c]):
            h = Ceil[a][b] - 50
            assert h + 50 <= Ceil[a][b]
            assert h >= 0
            yield (h, (a,b))

def time_from_h(curr_t, (a,b), req_h, (c,d)):
    curr_h = max(0, H - curr_t * 10)
    if req_h < curr_h:
        curr_t += (curr_h - req_h) / 10.
        curr_h = max(0, H - curr_t * 10)
    #assert curr_h <= req_h
    mov = 1 if curr_h >= Floor[a][b] + 20 else 10
    return curr_t + mov

def solve(accessible, done, H):
    while accessible and (N-1, M-1) not in done:
        pos, curr_t = accessible.pop()
        Times[pos[0]][pos[1]] = curr_t
        done.add(pos)
        for req_h, pos2 in connected(pos):
            if pos2 in done:
                continue
            req_t = time_from_h(curr_t, pos, req_h, pos2)
            if accessible.get(pos2, Ellipsis) > req_t:
                accessible[pos2] = req_t

for case_no in xrange(1, input() + 1):
    print >> sys.stderr, "Case #%s:" % (case_no,)
    print "Case #%s:" % (case_no,),

    H, N, M = map(int, raw_input().split())
    Ceil  = [map(int, raw_input().split()) for _ in xrange(N)]
    Floor = [map(int, raw_input().split()) for _ in xrange(N)]

    Times = [[None] * M for _ in xrange(N)]

    level = [(0,0)]
    done = set()
    accessible = PriorityQueue()
    while level:
        nlevel = set()
        for pos in level:
            Times[pos[0]][pos[1]] = 0.
            done.add(pos)
            for req_h, pos2 in connected(pos):
                if pos2 in done:
                    continue
                if req_h >= H:
                    nlevel.add(pos2)
                else:
                    req_t = time_from_h(0., pos, req_h, pos2)
                    if accessible.get(pos2, Ellipsis) > req_t:
                        accessible[pos2] = req_t
        nlevel -= done
        level = nlevel
    solve(accessible, done, H)
    print '%.6f' % (Times[N-1][M-1],)
