_DELIM = '<@>'

def encode(key, value):
    assert _DELIM not in key
    assert _DELIM not in value
    return key + _DELIM + value


def decode(line):
    key, value = line.split(_DELIM)
    return (key, value)
