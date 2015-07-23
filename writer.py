import struct


def _int_to_bytes(i):
    return struct.pack('I', i)


class Writer(object):
    def __init__(self, fname):
        self.fname = fname

    def store(self, data):
        """Stores data in pysstable format in a file.

        data is expected to be a dictionary mapping bytes to bytes.

        Storage format is:

        val1 val2 val3...
        len(key1) offset(val1) len(val1) key1
        len(key2) offset(val2) len(val2) key2
        ...

        offset(index)

        """
        index = []
        pos = 0

        with open(self.fname, 'wb') as f:
            for key, value in data.items():
                f.write(value)

                index.append((key, pos, len(value)))
                pos += len(value)

            # sorting here might not be required, not until we deal with such large
            # tables that all data can't be loaded in memory
            index.sort()

            for key, offset, val_len in index:
                key_len_b = _int_to_bytes(len(key))
                val_len_b = _int_to_bytes(val_len)
                val_offset_b = _int_to_bytes(offset)

                f.write(key_len_b)
                f.write(val_offset_b)
                f.write(val_len_b)
                f.write(key)

            # also mark the position where the index started
            index_offset_b = _int_to_bytes(pos)
            f.write(index_offset_b)

        return True
