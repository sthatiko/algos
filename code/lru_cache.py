
# https://www.interviewbit.com/problems/lru-cache/

# https://leetcode.com/problems/lru-cache
import socket
class Node:
    def __init__(self, key, value, prev=None, nxt=None):
        self.key = key
        self.value = value
        self.prev = prev
        self.nxt = nxt


class DLL:
    def __init__(self, cap):
        self.capacity = cap
        self.head = None
        self.rear = None
        self.count = 0

    def is_full(self):
        return self.count == self.capacity

    def get_size(self):
        return self.count

    def is_empty(self):
        return self.count == 0

    def append_left(self, node):
        if self.is_full():
            raise Exception("DLL is full")
        if self.is_empty():
            self.head = self.rear = node
        else:
            node.nxt = self.head
            self.head.prev = node
            self.head = node
        self.count += 1
        return self.head

    def append_right(self, node):
        if self.is_full():
            raise Exception("DLL is full")
        if self.is_empty():
            self.head = self.rear = node
        else:
            self.rear.nxt = node
            node.prev = self.rear
            self.rear = node
        self.count += 1
        return self.rear

    def pop_left(self):
        if self.is_empty():
            raise Exception("DLL is empty")
        if self.head == self.rear:
            self.rear = None
        ret = self.head
        self.head = self.head.nxt
        if self.count != 1:
            self.head.prev = None
        self.count -= 1
        return ret

    def pop_right(self):
        if self.is_empty():
            raise Exception("DLL is empty")
        if self.head == self.rear:
            self.head = None
        ret = self.rear
        self.rear = self.rear.prev
        if self.count != 1:
            self.rear.nxt = None
        self.count -= 1
        return ret

    def remove(self, node):
        if node is None:
            return
        if node.prev is not None:
            node.prev.nxt = node.nxt
        if node.nxt is not None:
            node.nxt.prev = node.prev
        if node == self.rear:
            self.rear = self.rear.prev
            if self.count != 1:
                self.rear.nxt = None
        if node == self.head:
            self.head = self.head.nxt
            if self.count != 1:
                self.head.prev = None
        node.nxt = node.prev = None
        self.count -= 1

    def pretty_print(self):
        if not self.is_empty():
            temp = self.head
            while temp is not None:
                print temp.prev, temp.key, temp, temp.nxt, '#',
                temp = temp.nxt


class LRUCache:

    # @param capacity, an integer
    def __init__(self, cap):
        self.cache = DLL(cap)
        self.lookup = dict()

    def is_full(self):
        return self.cache.is_full()

    # @return an integer
    def get(self, key):
        if key in self.lookup.keys():
            self.cache.remove(self.lookup[key])
            self.cache.append_left(self.lookup[key])
            #self.p_print()
            return self.lookup[key].value
        else:
            return -1

    # @param key, an integer
    # @param value, an integer
    # @return nothing
    def set(self, key, value):
        if key in self.lookup.keys():
            self.cache.remove(self.lookup[key])
        elif self.is_full():
            removed_node = self.cache.pop_right()
            del self.lookup[removed_node.key]
        self.lookup[key] = self.cache.append_left(Node(key, value))
        #self.p_print()

    def p_print(self):
        self.cache.pretty_print()
        print(self.lookup)


if __name__ == '__main__':
    inp = '32 4 G 9 G 13 G 15 S 3 2 G 12 G 7 G 9 G 8 G 5 S 5 10 S 3 4 G 13 G 3 G 7 S 9 10 S 15 12 S 14 3 G 9 S 10 10 G 9 G 5 S 12 15 G 14 G 3 G 4 G 15 G 15 G 9 G 11 S 9 7 G 10 S 14 7'
    inp = inp.split()
    data = iter(inp)
    oper_c = int(next(data))
    capacity = int(next(data))
    my_cache = LRUCache(capacity)
    for _ in range(oper_c):
        oper = next(data)
        if oper == 'S':
            my_cache.set(int(next(data)), int(next(data)))
        else:
            print my_cache.get(int(next(data))),
