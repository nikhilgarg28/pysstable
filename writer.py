from . import utils

def store(fname, data):
    d = []
    for key, value in data.items():
        line = utils.encode(key, value)
        d.append(line)

    d.sort()
    contents = '\n'.join(d)

    with open(fname, 'w') as f:
        f.write(contents)

    return True
