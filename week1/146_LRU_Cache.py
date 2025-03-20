class Node:

    def __init__(self, key=0, value=0):
        self.key = key
        self.value = value
        self.pre = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        # cache information
        self.cache = {}
        self.capacity = capacity
        self.size = 0
        # NodeList information
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.pre = self.head

    def move_to_head(self, node: Node):
        node.pre.next = node.next
        node.next.pre = node.pre

        node.pre = self.head
        node.next = self.head.next
        node.next.pre = node
        self.head.next = node


    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            self.move_to_head(node)
            return node.value
        else:
            return -1

        

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            node.value = value
            self.move_to_head(node)
            return
        if self.size >= self.capacity:
            node = self.tail.pre
            node.pre.next = node.next
            node.next.pre = node.pre
            del self.cache[node.key]
            self.size -= 1

        newNode = Node(key, value)
        newNode.pre = self.head
        newNode.next = self.head.next
        
        newNode.next.pre = newNode
        self.head.next = newNode
        self.cache[key] = newNode
        self.size += 1




# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)