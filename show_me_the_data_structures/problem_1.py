''' LRU eviction process
        1.  If the item is in the cache (cache hit), use the hash table to find the node and move it to the head of DLL
        2.  If the item is not in the cache (cache miss), load the item into the cache.  If the cache is full,
            evict the oldest item (remove from Cache and Hash)
        2b. Create a new node, add it to head.
        2c. Add item to hash, store cache node as value
'''


class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None


class LRU_Cache(object):

    def __init__(self, capacity):
        # Initialize class variables
        self.capacity = capacity
        self.hashmap = {}
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head


    def get(self, key):
        # Retrieve item from provided key. Return -1 if nonexistent.
        if key in self.hashmap:
            # retrieve the node, remove it from the cache and insert it back in, return the value
            node = self.hashmap[key]
            self._cache_remove(node)
            self._cache_insert(node)
            return node.value
        else:
            return -1


    def set(self, key, value):
        # Set the value if the key is not present in the cache. If the cache is at capacity remove the oldest item.

        if key in self.hashmap:
            # remove key from hashmap and node from cache
            node = self.hashmap[key]
            self._cache_remove(node)
            del self.hashmap[key]
        else:
            # key not present in cache
            if len(self.hashmap) == self.capacity:
                # cache at full capacity, remove LRU node
                lru_node = self.head.next
                self._cache_remove(lru_node)
                print(f'Cache exceeded capacity...removed LRU Node({lru_node.key}, {lru_node.value}).')
                del self.hashmap[lru_node.key]

        # add node
        new_node = Node(key, value)
        self._cache_insert(new_node)
        self.hashmap[key] = new_node


    def _cache_insert(self, node):
        # inserts a node to the cache at the MRU position (adjacent to the head)
        first_node = self.head.next
        first_node.prev = node
        node.prev = self.head
        node.next = first_node
        self.head.next = node


    def _cache_remove(self, node):
        # remove a node from the cache
        next_node = node.next
        next_node.prev = node.prev
        node.prev.next = next_node




# TEST CASES
our_cache = LRU_Cache(5)

our_cache.set(1, 1)
our_cache.set(2, 2)
our_cache.set(3, 3)
our_cache.set(4, 4)


print(f'test should return 1: {our_cache.get(1)}')     # returns 1
print(f'test should return 2: {our_cache.get(2)}')     # returns 2
print(f'test should return -1: {our_cache.get(9)}')    # returns -1 because 9 is not present in the cache

our_cache.set(5, 5)
our_cache.set(6, 6)                                    # exceeded capacity and removed LRU node(5, 5)

print(f'test should return 3: {our_cache.get(3)}')     # returns 3 because the cache reached it's capacity and 3 was the least recently used entry
our_cache.set(4, 3)
print(f'test should return 3: {our_cache.get(4)}')     # returns 3 beacuse the value of key 4 was overwritten to 3