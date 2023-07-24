class HashTable(object):
    def __init__(self):
        self.table = [None]*10000

    def store(self, string):
        id = self.calculate_hash_value(string)
        self.table[id] = string
        pass

    def lookup(self, string):
        """Return the hash value if the
        string is already in the table.
        Return -1 otherwise."""
        
        id = self.calculate_hash_value(string)
        if self.table[id] == None:
            return -1
        else:
            return id

    def calculate_hash_value(self, string):
        """Helper function to calulate a
        hash value from a string."""
        
        ch1 = ord(string[0])
        ch2 = ord(string[1])
        
        return ch1*100 + ch2
