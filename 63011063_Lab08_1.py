class Node:
    def __init__(self, data, freq, left=None, right=None):
        self.data = data
        self.freq = freq
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.data)


class Queue:
    def __init__(self, list=None):
        if list == None:
            self.items = []
        else:
            self.items = list

    def __str__(self):
        data = 'Data in Queue : '
        for item in self.items:
            data += str(item) + ' '
        return data

    def __len__(self):
        return len(self.items)

    def enQueue(self, value):
        self.items.append(value)

    def deQueue(self):
        return self.items.pop(0)

    def isEmpty(self):
        return len(self.items) == 0

    def lookQueueNumber(self, index):
        return self.items[index]


class HuffmanTree:
    def __init__(self):
        self.root = None

    def insert(self, data, freq):
        if self.root == None:
            self.root = Node(data, freq)
        else:
            current_node = self.root
            while True:
                if freq < current_node.freq or (freq == current_node.freq and data < current_node.data):
                    if current_node.left == None:
                        current_node.left = Node(data, freq)
                        break
                    else:
                        current_node = current_node.left
                elif freq > current_node.freq or (freq == current_node.freq and data > current_node.data):
                    if current_node.right == None:
                        current_node.right = Node(data, freq)
                        break
                    else:
                        current_node = current_node.right
        return self.root

    def descendingInorder(self, node):
        if node == None:
            return []
        lists = self.descendingInorder(node.right) + [Node(node.data, node.freq)] + self.descendingInorder(node.left)
        return lists


def search_node(node, data, code):
    if node == None:
        return None
    if data == node.data:
        return code
    if node != None:
        s = search_node(node.right, data, code + '1')
        if s != None:
            return s
        s = search_node(node.left, data, code + '0')
        return s


def printTree(node, level=0):
    if node != None:
        printTree(node.right, level + 1)
        print('     ' * level, node)
        printTree(node.left, level + 1)


def codeList(node, code):
    s = []
    if node != None:
        s += codeList(node.right, code + '1')
        if node.data != '*':
            s += [[node.data, code]]
        s += codeList(node.left, code + '0')
    return s


q = Queue()
huffman = HuffmanTree()
temp_str = list(input('Enter Input : '))
setOfChar = set(temp_str)

for data in setOfChar:
    huffman.root = huffman.insert(data, temp_str.count(data))

sortedData = huffman.descendingInorder(huffman.root)
q.enQueue(sortedData.pop())

while len(sortedData) != 0 or len(q) != 1:
    if len(q) <= 1:
        temp = sortedData.pop()
        q.enQueue(temp)
    else:
        if sortedData == [] or (sortedData[-1].freq >= q.lookQueueNumber(0).freq + q.lookQueueNumber(1).freq):
            l = q.deQueue()
            r = q.deQueue()
            q.enQueue(Node('*', l.freq + r.freq, l, r))
        else:
            temp = sortedData.pop()
            q.enQueue(temp)

root = q.deQueue()
codeword = {}

for i in codeList(root, ""):
    codeword[i[0]] = i[1]
print(codeword)
printTree(root)
print("Encoded! : ", end='')

for key in temp_str:
    print(search_node(root, key, ''), end='')
