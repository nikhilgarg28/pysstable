# pysstable
Rudimentary sorted string table in Python

Creates a sorted string table in Python. Using this, you can write string key/value
pairs in a file and after that load it in memory to serve values given the key. 

The constraints are:

1. Data can't be mutated after it's loaded - so it's only for read only data.
2. Loading data is lot more efficient than inserting all the key/value pairs one
   by one.
3. Read queries are not O(1) but O(log N)


Note: This is a really rudimentary implementation and probably can be made much
much faster and stable.
