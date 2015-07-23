from pysstable import utils, writer, reader

import random
import struct
import time

MAX_ULONG = (1 << 64) - 1

def random_long():
    return str(random.randint(0, MAX_ULONG))

def long_to_long(N):
    """Benchmarks pysstable when both keys/values represent unsigned longs.

    Results:

    Time taken to store 10K key/value pairs is: 15 ms
    Time taken to load 10K key/value pairs is: 2 ms
    Time taken to read random key/value pairs in table of size 10K is: 0 ms

    Time taken to store 100K key/value pairs is: 169 ms
    Time taken to load 100K key/value pairs is: 27 ms
    Time taken to read random key/value pairs in table of size 100K is: 0 ms

    Time taken to store 1M key/value pairs is: 2522 ms
    Time taken to load 1M key/value pairs is: 286 ms
    Time taken to read random key/value pairs in table of size 1M is: 0 ms

    Time taken to store 10M key/value pairs is: 42519 ms
    Time taken to load 10M key/value pairs is: 3412 ms
    Time taken to read random key/value pairs in table of size 10M is: 0 ms

    """
    keys = [random_long() for _ in range(N)]
    values = [random_long() for _ in range(N)]
    d = {k: v for k, v in zip(keys, values)}
    fname = 'long_to_long.log'

    # benchmarking table writes
    start = time.clock()
    writer.store(fname, d)
    stop = time.clock()
    print('Time taken to store %d key/value pairs is: %d ms' % (N,
        (stop-start) * 1000))

    # benchmarking table loads
    start = time.clock()
    reader.load(fname)
    stop = time.clock()
    print('Time taken to load %d key/value pairs is: %d ms' % (N,
        (stop-start) * 1000))

    # benchmarking random reads
    # randomly shuffling keys to avoid any locality benefits
    random.shuffle(keys)
    total = 0
    for k in keys:
        start = time.clock()
        v = reader.get(k)
        stop = time.clock()

        assert v == d[k]
        total += stop - start

    avg = total / len(keys)
    print('Time taken to read random key/value pairs in table of size %d is: %d ms' % (N,
        avg * 1000))
