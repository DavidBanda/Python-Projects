# Hash Value = (ASCII Value of First Letter * 100) +
# ASCII Value of Second Letter

# HashValue = f'{ord("U")}{ord("D")}'
# print(int(HashValue))


class HashTable(object):
    def __init__(self):
        self.table = [None]*10000

    def store(self, string):
        """Input a string that's stored in
        the table."""
        self.index_hash_value = self.lookup(string)
        if self.index_hash_value == -1:
            self.index_hash_value =self.calculate_hash_value(string)
            self.table[self.index_hash_value] = string

    def lookup(self, string):
        """Return the hash value if the
        string is already in the table.
        Return -1 otherwise."""
        self.string_hash = self.calculate_hash_value(string)
        self.verify = self.table[self.string_hash]
        if self.verify:
            return self.string_hash
        else:
            return -1

    def calculate_hash_value(self, string):
        """Helper function to calulate a
        hash value from a string."""
        # self.hash_value = f'{ord(string[0])}{ord(string[1])}'
        self.hash_value = '{0}{1}'.format(ord(string[0]), ord(string[1]))
        self.hash_value = int(self.hash_value)
        return self.hash_value

    def size(self):
        return len(self.table)


hsh = HashTable()
hsh.store('UDACITY')
print(hsh.lookup('UDACITY'))
print(hsh.lookup('KJACITY'))



