class Node:
    def __init__(self, value, next = None):
        self.value = value
        if next == None:
            self.next = None
        else:
            self.next = next


class LinkedList:

    def __init__(self):
        self.head = None
        self.size = 0

    def __str__(self):
        if self.is_empty():
            return "Empty"
        cur, s = self.head, str(self.head.value) + " "
        while cur.next != None:
            s += str(cur.next.value) + " "
            cur = cur.next
        return s

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

    def node_at(self,i):
        p = self.head
        for j in range(0,i):
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


L = LinkedList()
inp = input('Enter Input : ').split(',')
for i in inp:
    if i[:2] == "AP":
        L.append(i[3:])
    elif i[:2] == "AH":
        L.addHead(i[3:])
    elif i[:2] == "SE":
        print("{0} {1} in {2}".format(L.search(i[3:]), i[3:], L))
    elif i[:2] == "SI":
        print("Linked List size = {0} : {1}".format(len(L), L))
    elif i[:2] == "ID":
        print("Index ({0}) = {1} : {2}".format(i[3:], L.index_of(i[3:]), L))
    elif i[:2] == "PO":
        before = "{}".format(L)
        k = L.pop(int(i[3:]))
        print(("{0} | {1}-> {2}".format(k, before, L)) if k == "Success" else ("{0} | {1}".format(k, L)))
print("Linked List :", L)