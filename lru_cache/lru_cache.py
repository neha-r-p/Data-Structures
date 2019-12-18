from doubly_linked_list import DoublyLinkedList

class LRUCache:
    """
    Our LRUCache class keeps track of the max number of nodes it
    can hold, the current number of nodes it is holding, a doubly-
    linked list that holds the key-value entries in the correct
    order, as well as a storage dict that provides fast access
    to every node stored in the cache.
    """
    def __init__(self, limit=10):
        self.limit = limit
        self.size = 0
        self.order = DoublyLinkedList()
        self.storage = dict()

    """
    Retrieves the value associated with the given key. Also
    needs to move the key-value pair to the end of the order
    such that the pair is considered most-recently used.
    Returns the value associated with the key or None if the
    key-value pair doesn't exist in the cache.
    """
    def get(self, key):
        #returns value associated with key (if nonexistent, return None)
        if key not in self.storage:
            return None
        #Moves k:v pair to most-recently used
        self.order.move_to_front(self.storage[key])
        #retrieves value associated with key
        return self.storage[key].value[1]

    """
    Adds the given key-value pair to the cache. The newly-
    added pair should be considered the most-recently used
    entry in the cache. If the cache is already at max capacity
    before this entry is added, then the oldest entry in the
    cache needs to be removed to make room. Additionally, in the
    case that the key already exists in the cache, we simply
    want to overwrite the old value associated with the key with
    the newly-specified value.
    """
    def set(self, key, value):
        #if key exists in cache, 
        if key in self.storage:
            #overwrite (update dictionary) 
            node = self.storage[key]
            node.value = (key, value)
            #and put at head
            self.order.move_to_front(node)
            return

        #If cache is at max capacity, remove oldest entry to make room (remove from tail)
        if self.size == self.limit:
            del self.storage[self.order.tail.value[0]]
            self.order.remove_from_tail()
            self.size -= 1
        #Add k:v pair to cache into most recently used
            # add node to head in DLL and add k:v to dictionary
        self.order.add_to_head((key, value))
        self.storage[key] = self.order.head
        self.size += 1
