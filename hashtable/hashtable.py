class HashTableEntry:
    """
    Linked List hash table key/value pair
    """
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


# Hash table can't have fewer than this many slots
MIN_CAPACITY = 8


class HashTable:
    """
    A hash table that with `capacity` buckets
    that accepts string keys

    Implement this.
    """

    def __init__(self, capacity, auto_resize=True):
        self.capacity = capacity
        self.size = 0
        self.storage = [None] * capacity
        self.auto_resize = auto_resize

    
    def __len__(self):
        """ returns the number of items stored in this hash table """
        return self.size


    def __str__(self):
        """ returns the contents of this hash table as a formatted """
        output = ""
        for item in self.storage:
            if item is not None:
                output += f"\t{item.key}: {item.value}\n"

                # check linked list items
                node = item.next
                while node is not None:
                    output += f"\t{item.key}: {item.value}\n"
                    node = node.next
        
        return "{\n" + output + "}"


    def get_num_slots(self):
        """
        Return the length of the list you're using to hold the hash
        table data. (Not the number of items stored in the hash table,
        but the number of slots in the main list.)

        One of the tests relies on this.

        Implement this.
        """
        return len(self.storage)


    def get_load_factor(self):
        """
        Return the load factor for this hash table.

        Implement this.
        """
        return self.size / self.capacity


    def fnv1(self, key):
        """
        FNV-1 Hash, 64-bit

        Implement this, and/or DJB2.
        """
        prime = 1099511628211
        # start at this offset
        hash = 14695981039346656037
        for letter in key:
            # for each letter, multiply by the prime
            hash *= prime
            # then XOR with the letter unicode value
            hash = hash ^ ord(letter)
        return hash


    def djb2(self, key):
        """
        DJB2 hash, 32-bit

        Implement this, and/or FNV-1.
        """
        # start at 5381
        hash = 5381
        for letter in key:
            # add bitwise shift left 5 and the unicode letter
            hash += (hash << 5) + ord(letter)
        return hash


    def hash_index(self, key):
        """
        Take an arbitrary key and return a valid integer index
        between within the storage capacity of the hash table.
        """
        #return self.fnv1(key) % self.capacity
        return self.djb2(key) % self.capacity


    def put(self, key, value):
        """
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Implement this.
        """
        index = self.hash_index(key)

        if self.storage[index] is None:
            # No value there yet, just insert new entry
            self.storage[index] = HashTableEntry(key, value)
        else:
            # Collision, add to linked list
            node = self.storage[index]
            while node.next is not None:
                if node.key == key:
                    # existing key was given, overwrite the value
                    node.value = value
                    return
                node = node.next

            if node.key == key:  # Check last node
                node.value = value
                return

            node.next = HashTableEntry(key, value)  # Create new node
        
        self.size += 1
        if self.auto_resize:
            self.check_load()


    def delete(self, key):
        """
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Implement this.
        """
        index = self.hash_index(key)

        if self.storage[index] is None:
            # No keys at this index
            print("Warning, key not found")
            return

        prev = None
        node = self.storage[index]

        while True:
            if node.key == key:
                # key found, delete it
                if prev is None:  # node was the head
                    self.storage[index] = node.next
                else:  # node was not the head
                    prev.next = node.next
                self.size -= 1
                if self.auto_resize:
                    self.check_load()
                return

            # move to next nodes
            prev, node = node, node.next
            if node is None:  # end of list reached
                break

        # Key not found
        print("Warning, key not found")


    def get(self, key):
        """
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Implement this.
        """
        index = self.hash_index(key)
        if self.storage[index] is not None:
            # find the item with this key and return it
            node = self.storage[index]
            while node.next is not None:
                if node.key == key:  # check this node
                    return node.value
                node = node.next  # move to next node

            # last node reached here
            if node.key == key:
                return node.value
            else:
                # key not found
                return None
        else:
            return None

    
    def check_load(self):
        """
        Checks load factor and resizes if necessary
        """
        load = self.get_load_factor()
        if load > .7:
            self.resize(self.capacity * 2)  # high load, resize up
        elif load < .2:
            self.resize(self.capacity / 2)  # low load, resize down


    def resize(self, new_capacity):
        """
        Changes the capacity of the hash table and
        rehashes all key/value pairs.

        Implement this.
        """
        # Ensure new_capacity is an int
        new_capacity = int(new_capacity)

        # reset variables
        self.capacity = new_capacity
        old = self.storage
        self.storage = [None] * new_capacity

        # rehash old items into the new list
        for item in old:
            if item is not None:
                self.put(item.key, item.value)

                # traverse linked lists to add all items
                node = item.next
                while node is not None:
                    self.put(node.key, node.value)
                    node = node.next


if __name__ == "__main__":
    ht = HashTable(8)

    ht.put("line_1", "'Twas brillig, and the slithy toves")
    ht.put("line_2", "Did gyre and gimble in the wabe:")
    ht.put("line_3", "All mimsy were the borogoves,")
    ht.put("line_4", "And the mome raths outgrabe.")
    ht.put("line_5", '"Beware the Jabberwock, my son!')
    ht.put("line_6", "The jaws that bite, the claws that catch!")
    ht.put("line_7", "Beware the Jubjub bird, and shun")
    ht.put("line_8", 'The frumious Bandersnatch!"')
    ht.put("line_9", "He took his vorpal sword in hand;")
    ht.put("line_10", "Long time the manxome foe he sought--")
    ht.put("line_11", "So rested he by the Tumtum tree")
    ht.put("line_12", "And stood awhile in thought.")

    print("")

    # Test storing beyond capacity
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    # Test resizing
    old_capacity = ht.get_num_slots()
    ht.resize(ht.capacity * 2)
    new_capacity = ht.get_num_slots()

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))
    
    # Test __str__()
    print("\nHash table contents:")
    print(ht)

    print("")
