from . import writer
from . import reader

import random


def random_bytes(n):
    return bytes(random.getrandbits(8) for _ in range(n))


def test_bytes():
    N = 100000
    ksize = random.randint(1, 20)
    vsize = random.randint(1, 20)
    keys = [random_bytes(ksize) for _ in range(N)]
    values = [random_bytes(vsize) for _ in range(N)]
    data = {k: v for k, v in zip(keys, values)}
    fname = 'bytes.log'

    w = writer.Writer(fname)
    w.store(data)

    r = reader.Reader(fname)
    for key, value in data.items():
        got = r.get(key)
        assert value == got, '%s => %s, Got %s instead' % (key, value, got)

    # also make sure that some keys we did not put are not present
    for _ in range(1000):
        key = random_bytes(10)
        if key in data: continue

        assert r.get(key) is None
