from . import utils
from . import writer
from . import reader

import random
import string
import time

alphabet = string.ascii_letters

def random_string(n):
    return ''.join([random.choice(alphabet) for _ in range(n)])

def test_encode_decode():
    for _ in range(20):
        key = random_string(10)
        value = random_string(10)
        line = utils.encode(key, value)
        assert (key, value) == utils.decode(line)


def test_store_get():
    d = {}
    for _ in range(1000):
        key = random_string(10)
        value = random_string(10)
        d[key] = value

    fname = 'test.log'

    # write all the data to a pysstable file
    assert writer.store(fname, d)

    # load the pysstable file in memory
    reader.load(fname)
    for key, value in d.items():
        got = reader.get(key)
        assert value == got, '%s => %s, Got %s instead' % (key, value, got)

    # also make sure that some keys we did not put are not present
    for _ in range(1000):
        key = random_string(10)
        if key in d: continue

        assert reader.get(key) is None
