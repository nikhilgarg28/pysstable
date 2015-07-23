from . import utils

_data = []

def load(fname):
    global _data
    _data = []

    with open(fname, 'r') as f:
        _data = f.readlines()

    for i, line in enumerate(_data):
        _data[i] = line.strip()

    return len(_data)


def get(key):
    global _data
    low = 0
    high = len(_data) - 1

    # invariant is row of our interest is between [low, high] (both incl)
    while low < high:
        mid = low + (high - low) // 2

        s = _data[mid]
        if key < s:
            high = mid
        else:
            low = mid + 1

    if 0 <= low < len(_data):
        row = _data[low]
    else:
        row = ''

    if row.startswith(key):
        key, value = utils.decode(row)
        return value
    else:
        return None
