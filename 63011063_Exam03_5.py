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

    def create(self, data):
        if self.root is None:
                    root = Node(data)
                    self.root = root
        else:
            current_node = self.root
            while True:
                if current_node.data <= data:
                    if current_node.right is None:
                        current_node.right = Node(data)
                        break
                    else:
                        current_node = current_node.right
                else:
                    if current_node.left is None:
                        current_node.left = Node(data)
                        break
                    else:
                        current_node = current_node.left


def printLevelOrder(root,level):
    if root is None:
        return False
    if root:
        if level == 1:
            print(root.data,end=' ')
            return True
        left = printLevelOrder(root.left,level-1)
        right = printLevelOrder(root.right, level - 1)
        return left or right


def levelTraversal(root):
    level = 1
    while printLevelOrder(root,level):
        level += 1


def printPreOrder(root):
    if root is None:
        return
    print(root.data,end=' ')
    printPreOrder(root.left)
    printPreOrder(root.right)
    return


def printInOrder(root):
    if root is None:
        return
    printInOrder(root.left)
    print(root.data,end=' ')
    printInOrder(root.right)
    return


def printPostOrder(root):
    if root:
        printPostOrder(root.left)
        printPostOrder(root.right)
        print(root.data,end=' ')



T = BinarySearchTree()
tree = BinarySearchTree()
n = [int(i) for i in input(" *** Binary Search Tree ***\nEnter Input : ").split()]

for i in n:
    tree.create(i)


print("\n --- Tree traversal ---")
print("Level order : ",end='')
levelTraversal(tree.root)

print("\nPreorder : ",end='')
printPreOrder(tree.root)

print("\nInorder : ",end='')
printInOrder(tree.root)

print("\nPostorder : ",end='')
printPostOrder(tree.root)