class HashTableEntry:
    """
    Hash Table entry, as a linked list node.
    """

    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


class HashTable:
    def __init__(self, capacity,):
        self.capacity = capacity
        self.storage = [None] * capacity


    def fnv1(self, key):
        total = 14695981039346656037
        new_key = key.encode()

        for x in new_key:
            total = total * 1099511628211
            total = total ^ x
            total &= 0xffffffffffffffff
        return total    
      
    def djb2(self, key):
        """
        DJB2 32-bit hash function

        Implement this, and/or FNV-1.
        """

    def hash_index(self, key):
        """
        Take an arbitrary key and return a valid integer index
        between within the storage capacity of the hash table.
        """
        return self.fnv1(key) % self.capacity
        # return self.djb2(key) % self.capacity

    def put(self, key, value):
      
        index = self.hash_index(key)
        node = self.storage[index]

        if node is None:
            self.storage[index] = HashTableEntry(key, value)
        elif node.key == key:
            node.value = value
        while node is not None:
            if node.key == key:
                node.value = value
            elif node.next == None:
                node.next = HashTableEntry(key, value)  
            node = node.next
    
            
    def delete(self, key):
        prev = None
        index = self.hash_index(key)
        if not self.storage[index]:
            return None
        else:
            node = self.storage[index]
            while node is not None and node and node.key != key: 
                prev = node
                node = node.next
            # prev = node.next
            if prev is None:
                self.storage[index] = node.next
            else:
                prev.next = prev.next.next
                # self.entries -= 1
                # if self.entries / self.capacity < 0.2:
                #     self.resize(self.capacity * 2)
                return None
        

    

    def get(self, key):
        index = self.hash_index(key)
        if not self.storage[index]:
            return None
        else:
            node = self.storage[index]
            while node and node.key != key: node = node.next
            return node.value

        # index = self.hash_index(key)
        # return self.storage[index]

  
    def resize(self):
        """
        Doubles the capacity of the hash table and
        rehash all key/value pairs.

        Implement this.
        """
       

if __name__ == "__main__":
    ht = HashTable(2)

    ht.put("line_1", "Tiny hash table")
    ht.put("line_2", "Filled beyond capacity")
    ht.put("line_3", "Linked list saves the day!")

    print("")

    # Test storing beyond capacity
    print(ht.get("line_1"))
    print(ht.get("line_2"))
    print(ht.get("line_3"))

    # Test resizing
    old_capacity = len(ht.storage)
    ht.resize()
    new_capacity = len(ht.storage)

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    print(ht.get("line_1"))
    print(ht.get("line_2"))
    print(ht.get("line_3"))

    print("")
