DELIM = '<@>'

def encode(key, value):
    assert DELIM not in key
    assert DELIM not in value
    return key + DELIM + value


def decode(line):
    key, value = line.split(DELIM)
    return (key, value)
