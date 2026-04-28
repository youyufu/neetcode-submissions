class Node():
    def __init__(self, key, val):
        self.left = None
        self.right = None
        self.key = key
        self.val = val

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.keyMap = {}
        self.left = Node(0, 0) # access to least frequent
        self.right = Node(0, 0) # access to most frequent
        self.left.right = self.right
        self.right.left = self.left

    def get(self, key: int) -> int:
        if key not in self.keyMap:
            return -1
        node = self.keyMap[key]
        # remove from current position
        node.left.right, node.right.left = node.right, node.left
        # insert just before self.right
        node.left, node.right = self.right.left, self.right
        self.right.left.right, self.right.left = node, node
        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.keyMap:
            node = self.keyMap[key]
            node.val = value
            node.left.right, node.right.left = node.right, node.left
        else:
            node = Node(key, value)
            self.keyMap[key] = node
            if len(self.keyMap) > self.capacity:
                delNode = self.left.right
                del self.keyMap[delNode.key]
                self.left.right, delNode.right.left = delNode.right, self.left
        # insert just before self.right (shared by both branches)
        node.left, node.right = self.right.left, self.right
        self.right.left.right, self.right.left = node, node