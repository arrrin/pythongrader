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

    def search(self,root, key):
        if root is None or root.data == key:
            return root

        if root.data < key:
            return self.search(root.right, key)

        return self.search(root.left, key)

    def insert(self, root, data):
        if root is None:
            return Node(data)
        else:
            if root.data == data:
                return root
            elif root.data < data:
                root.right = self.insert(root.right, data)
            else:
                root.left = self.insert(root.left, data)
        return root

    def printTree(self, node, level=0):
        if node != None:
            self.printTree(node.right, level + 1)
            print('     ' * level, node)
            self.printTree(node.left, level + 1)

    def lprintTree(self, node, l):

        if node != None:
            self.lprintTree(node.left, l)
            l.append(node.data)
            self.lprintTree(node.right, l)

        return l


T = BST()

inp = input('Enter Input : ').split('|')
lst = []
inp1 = [int(i) for i in inp[0].split()]
inp2 = int(inp[1])
root = Node(inp1[0])
for i in inp1[1:]:
    root = T.insert(root,i)
lst = T.lprintTree(root,[])
T.printTree(root)
print('--------------------------------------------------')

if min([int(e) for e in lst]) < inp2:
    print('Below', inp2, ':', ' '.join([str(e) for e in lst if e < inp2]))

else:
    print('Below ' + str(inp2), ':', 'Not have')