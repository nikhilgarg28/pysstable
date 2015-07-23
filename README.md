# pysstable
Sorted string table in Python.

Creates a sorted string table in Python. Using this, you can write string key/value
pairs in a file and after that load it in memory to serve values given the key.
For now, it loads the entire table in memory though in future, it will be
possible to only load an index in memory to support pretty large tables.

Constraints and performance characterstics :

1. Data can't be mutated after it's loaded - so it's only for read only data.
2. Loading data is lot more efficient than inserting all the key/value pairs one
   by one.
3. Read queries are not O(1) but O(log N)
4. Low space overhead - pysstable stores additional 12 bytes per key. If
   key/values are large (say few hundred bytes), this overhead is pretty small.

Wishlist
---------
1. Even lower space overhead, especially if keys/values are smaller. If key/value are small, 
   space overhead of 12 bytes per key will not be acceptable.

2. Not loading the whole table in memory and only loading the index in the
   memory.

3. Exporting pysstable interface as thrift service.
