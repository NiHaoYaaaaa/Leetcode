import math

class CNTNode:

    def __init__(self, cnt: int):
        self.cnt = cnt
        self.next = None
        self.pre = None
        self.tail = None

class Node:

    def __init__(self, key=0, value=0, parent=None):
        self.key = key
        self.value = value
        self.pre = None
        self.next = None
        self.parent = parent

class LFUCache:

    def __init__(self, capacity: int):
        self.CNTcache = {}
        self.cache = {}
        self.capacity = capacity
        self.size = 0
    
    def remove_node(self, node: Node):
        node.pre.next = node.next
        node.next.pre = node.pre
    
    def move_node(self, node: Node, cnt: int):
        if cnt in self.CNTcache:
            newParent = self.CNTcache[cnt]
            # node
            node.pre = newParent
            node.next = newParent.next
            node.parent = newParent
            # newParent
            newParent.next = node
            # node.next
            node.next.pre = node
        else:
            # newParent
            newParent = CNTNode(cnt)
            newParent_tail = CNTNode(cnt)
            newParent.next = node
            newParent.tail = newParent_tail
            # node
            node.pre = newParent
            node.next = newParent_tail
            node.parent = newParent
            # newParent_tail
            newParent_tail.pre = node
            # CNTcache
            self.CNTcache[cnt] = newParent



    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            self.remove_node(node)
            if node.parent.next == node.parent.tail:
                node.parent.tail = None
                del self.CNTcache[node.parent.cnt]
            self.move_node(node, node.parent.cnt + 1)
            return node.value
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            node.value = value
            self.remove_node(node)
            if node.parent.next == node.parent.tail:
                node.parent.tail = None
                del self.CNTcache[node.parent.cnt]
            self.move_node(node, node.parent.cnt + 1)
            return
        if self.size >= self.capacity:
            parent = self.CNTcache[min(self.CNTcache.keys())]
            node = parent.tail.pre
            self.remove_node(node)
            if parent.next == parent.tail:
                node.parent.tail = None
                del self.CNTcache[node.parent.cnt]
            del self.cache[node.key]
            self.size -= 1

        # add newNode
        newNode = Node(key, value)
        self.move_node(newNode, 1)
        self.cache[key] = newNode
        self.size += 1

        


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)