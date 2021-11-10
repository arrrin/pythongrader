class Node:

    def __init__(self, data):
        self.data = data

        self.left = None

        self.right = None


class BST:

    def __init__(self):
        self.root = None

    def create(self, data):
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


def height(obj):
    if obj is None:
        return 0
    else:
        return max(height(obj.left), height(obj.right)) + 1


def printLevel(r):
    h = height(r) - 1
    for i in range(1, h + 2):
        printLevelOrder(r, i)


def printInorder(obj):
    if obj != None:
        printInorder(obj.left)
        print(obj.data, end=" ")
        printInorder(obj.right)


def printPostorder(obj):
    if obj != None:
        printPostorder(obj.left)
        printPostorder(obj.right)
        print(obj.data, end=" ")


def printPreorder(obj):
    if obj != None:
        print(obj.data, end=" ")
        printPreorder(obj.left)
        printPreorder(obj.right)


def printLevelOrder(obj, level):
    if obj != None:
        if level == 1:
            print(obj.data, end=" ")
        elif level > 1:
            printLevelOrder(obj.left, level - 1)
            printLevelOrder(obj.right, level - 1)


tree = BST()

arr = list(map(int, input("Enter Input : ").split()))

for e in arr:
    tree.create(e)

print("Preorder : ", end="")
printPreorder(tree.root)
print("\nInorder : ", end="")
printInorder(tree.root)
print("\nPostorder : ", end="")
printPostorder(tree.root)
print("\nBreadth : ", end="")
printLevel(tree.root)