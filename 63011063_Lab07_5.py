class Node:

    def __init__(self, data):
        self.data = data

        self.left = None

        self.right = None

    def __str__(self):
        return str(self.data)


class BST:

    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root is None:
            root = Node(data)
            self.root = root
        else:
            node = self.root
            while True:
                if node.data <= data:
                    if node.right is None:
                        node.right = Node(data)
                        break
                    else:
                        node = node.right
                else:
                    if node.left is None:
                        node.left = Node(data)
                        break
                    else:
                        node = node.left

    def checkpos(self, data):
        if self.root is None:
            print("Not exist")
            return
        if self.root.data == data:
            print("Root")
            return
        node = self.root
        while node is not None:
            if data == node.data:
                if node.left is None and node.right is None:
                    print("Leaf")
                else:
                    print("Inner")
                return
            elif data > node.data:
                node = node.right
            else:
                node = node.left
        print("Not exist")

    def printTree(self, node, level=0):
        if node != None:
            self.printTree(node.right, level + 1)
            print('     ' * level, node)
            self.printTree(node.left, level + 1)


T = BST()
inp = [int(i) for i in input('Enter Input : ').split()]
for i in range(1, len(inp)):
    root = T.insert(inp[i])
T.printTree(T.root)
T.checkpos(inp[0])