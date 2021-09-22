class Node:
    def __init__(self, value, next=None, previous=None):
        self.value = value
        self.next = next
        self.previous = previous


class LinkedList:

    def __init__(self):
        self.head = None
        self.size = 0

    def __str__(self):
        if self.is_empty():
            return "Empty"
        cur, s = self.head, str(self.head.value) + "->"
        while cur.next != None:
            s += str(cur.next.value) + '->'
            cur = cur.next
        return s[:-2]

    def is_empty(self):
        return self.head == None

    def __len__(self):
        return self.size

    def size(self):
        return self.size

    def append(self, item):
        p = Node(item)
        if self.head == None:
            self.head = p
        else:
            t = self.head
            while t.next != None:
                t = t.next
            t.next = p
        self.size += 1

    def addHead(self, item):
        if self.is_empty():
            p = Node(item)
            self.head = p
            self.size += 1
        else:
            p = Node(item,self.head)
            self.head = p
            self.size += 1

    def index_of(self, item):
        p = self.head
        for i in range(len(self)):
            if p.value == item:
                return i
            p = p.next
        return -1

    def search(self, item):
        if self.index_of(item) >= 0:
            return 'Found'
        else:
            return 'Not Found'

    def node_at(self, i):
        p = self.head
        for j in range(0, i):
            p = p.next
        return p

    def delete_after(self,i):
        if self.size > 0:
            p = self.node_at(i)
            p.next = p.next.next
            self.size -= 1

    def insert_after(self,data,p):
        q = Node(data)
        q.next = p.next
        p.next = q

    def pop(self, pos):
        if pos < 0 or pos > len(self):
            return 'Out of Range'
        elif pos == 0 and self.size > 0:
            self.head = self.head.next
            self.size -= 1
            return 'Success'
        elif pos == 0 and self.size == 0:
            return 'Out of Range'
        else:
            self.delete_after(pos-1)
            return 'Success'

    def direct(self, pos1, pos2):
        if pos1 == 0 and pos2 == 0 and self.is_empty():
            print("Error! {list is empty}")
        elif not 0 <= pos1 < self.size:
            print('Error! {index not in length}:', pos1)
        elif not 0 <= pos2 < self.size:
            print('index not in length, append :', pos2)
            self.append(pos2)
        else:
            temp = self.head
            count = 0
            while temp is not None and count < pos1:
                temp = temp.next
                count += 1
            node1 = temp
            temp = self.head
            count = 0
            while temp is not None and count < pos2:
                temp = temp.next
                count += 1
            node2 = temp
            node1.next = node2
            node2.previous = node1
            print(f'Set node.next complete!, index:value = {pos1}:{node1.value} -> {pos2}:{node2.value}')

    def findLoop(self):
        mem = []
        count = 0
        temp = self.head
        for _ in range(500):
            count += 1
            if temp is None:
                break
            if temp in mem:
                return True
            mem.append(temp)
            temp = temp.next
        return False


llist = LinkedList()

inp = input('Enter input : ').split(',')
for i in inp:
    cmd, val = i.split()
    if cmd == "A":
        llist.append(i[2:])
        print("{0}".format(llist))
    elif cmd == "S":
        pos1, pos2 = val.split(":")
        llist.direct(int(pos1), int(pos2))
        if llist.findLoop():
            print("Found Loop")
            break
else:
    print('No Loop')
    print("{0}".format(llist))

