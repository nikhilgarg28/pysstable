import struct


def _bytes_to_int(b):
    return struct.unpack('I', b)[0]


class Reader(object):
    def __init__(self, fname):
        self.fname = fname
        self._values = []
        self._key_data = []
        self._loaded = False

    def _read_value(self, offset, size):
        return self._values[offset:offset + size]

    def load(self):
        if self._loaded:
            return len(self._key_data)

        self._values = []
        self._key_data = []

        with open(self.fname, 'rb') as f:
            # first go to 4 bytes from the end
            f.seek(-4, 2)
            index_offset_b = f.read()
            index_offset = _bytes_to_int(index_offset_b)

            # now go to the top of file and read all the way till index starts
            f.seek(0)
            self._values = f.read(index_offset)

            # now  we are at the start of index
            index_b = f.read()
            # throw away last 4 bytes because they aren't part of index
            index_b = index_b[:-4]

        read = 0
        while read < len(index_b):
            key_len = _bytes_to_int(index_b[read:read+4])
            read += 4

            val_offset = _bytes_to_int(index_b[read:read+4])
            read += 4

            val_len = _bytes_to_int(index_b[read:read+4])
            read += 4

            key =  index_b[read:read+key_len]
            read += key_len

            self._key_data.append((key, val_offset, val_len))

        self._loaded = True
        return len(self._key_data)

    def get(self, key):
        if not self._loaded:
            self.load()

        low = 0
        high = len(self._key_data)

        # invariant is row of our interest is between [low, high)
        while low < high:
            mid = low + (high - low) // 2

            k, val_offset, val_len = self._key_data[mid]
            if k == key:
                return self._read_value(val_offset, val_len)
            if key < k:
                high = mid
            else:
                low = mid + 1

        return None
