import array
from collections import defaultdict


def generate_seq(n, m, X, Y, Z, A):
    for i in range(n):
        yield A[i % m]
        A[i % m] = (X * A[i % m] + Y * (i + 1)) % Z

block_size = 512

for case_no in xrange(0, input()):
    print "Case #%s:" % (case_no + 1,),

    n, m, X, Y, Z = list(map(int, raw_input().split()))
    A = [input() for _ in range(m)]

    blocks_sum = array.array('I', (0 for _ in xrange(10**9 / block_size)))
    blocks = defaultdict(lambda: defaultdict(lambda:0))

    for v in generate_seq(n, m, X, Y, Z, A):
        bno, bre = v / block_size, v % block_size
        prev_blocks_sum = sum(blocks_sum[b] for b in xrange(bno))
        curr_block_sum = sum(blocks[bno][i] for i in xrange(bre))
        incr = 1 + prev_blocks_sum + curr_block_sum
        blocks[bno][bre] = (blocks[bno][bre] + incr) % 1000000007
        blocks_sum[v / block_size] = (blocks_sum[v / block_size] + incr) % 1000000007

    print sum(blocks_sum)  % 1000000007
