class Node:
    def __init__(self, value, key):
        self.key = key
        self.value = value
        self.left = None
        self.right = None
        self.parent = None

class Map(Node):
    def __init__(self):
        self.root = None
