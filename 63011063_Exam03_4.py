class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.level = None

    def __str__(self):
        return str(self.data)


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def create(self, val):
        if self.root == None:
            self.root = Node(val)
        else:
            current = self.root
            while True:
                if val < current.data:
                    if current.left:
                        current = current.left
                    else:
                        current.left = Node(val)
                        break
                elif val > current.data:
                    if current.right:
                        current = current.right
                    else:
                        current.right = Node(val)
                        break
                else:
                    break


def printTree(node, level=0):
    if node != None:
        printTree(node.right, level + 1)
        print('     ' * level, node)
        printTree(node.left, level + 1)


def parents(node, val, parent_node):
    if node is None:
        return
    if node.data == val:
        print( parent_node)
    else:
        parents(node.left,val,node.data)
        parents(node.right, val, node.data)


tree = BinarySearchTree()
data = input("Enter Input : ").split("/")
for e in data[0].split():
    tree.create(e)
printTree(tree.root)
if data[1] == tree.root.data:
    print('\nParents of', data[1], 'is none because', data[1], 'is root!!!', end='')
elif data[1] not in data[0]:
    print('\nParents of', data[1], 'is not found!!!')
else:
    print('\nParents of', data[1], 'is ', end='')
    parents(tree.root, data[1], -1)

