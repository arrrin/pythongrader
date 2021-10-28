class LinkedList:
    class Node:
        def __init__(self, data, next=None):
            self.data = data
            if next is None:
                self.next = None
            else:
                self.next = next

        def __str__(self):
            return str(self.data)

    def __init__(self, head=None):
        if head == None:
            self.head = self.tail = None
            self.size = 0
        else:
            self.head = head
            t = self.head
            self.size = 1
            while t.next != None:
                t = t.next
                self.size += 1
            self.tail = t

    def __str__(self):
        s = 'Linked data : '
        p = self.head
        while p != None:
            s += str(p.data) + ' '
            p = p.next
        return s

    def __len__(self):
        return self.size

    def append(self, data):
        p = self.Node(data)
        if self.head == None:
            self.head = self.tail = p
        else:
            t = self.tail
            t.next = p
            self.tail = p
        self.size += 1

    def removeHead(self):
        if self.head == None: return
        if self.head.next == None:
            p = self.head
            self.head = None
        else:
            p = self.head
            self.head = self.head.next
        self.size -= 1
        return p.data

    def isEmpty(self):
        return self.size == 0

    def nodeAt(self, i):
        p = self.head
        for j in range(i):
            p = p.next
        return p

    def index_of(self, item):
        p = self.head
        for i in range(len(self)):
            if p.value == item:
                return i
            p = p.next
        return -1

    def sortlisted(self):
        p = self.head
        t = None
        if p is None:
            return
        else:
            while p is not None:
                t = p.next
                while t is not None:
                    if p.data > t.data:
                        temp = p.data
                        p.data = t.data
                        t.data = temp
                    t = t.next
                p = p.next


    def contentEquivalence(self,other):
        p1 = self.head
        p2 = other.head
        if p1 is None and p2 is None:
            return True
        if len(self) != len(other):
            return False
        while p1 is not None and p1.next is not None and p2 is not None and p2.next is not None:
            if p1.data == p2.data:
                p1 = p1.next
                p2 = p2.next
            else:
                return False
        if p1.next is None and p2.next is None:
            if p1.data == p2.data:
                return True
            else:
                return False


list1 = LinkedList()

list2 = LinkedList()

user_input = input('List1,List2 : ').split(",")
inp1 = user_input[0].split()
inp2 = user_input[1].split()

for i in inp1:
    list1.append(i)

for i in inp2:
    list2.append(i)
list1.sortlisted()
list2.sortlisted()

print("List1 content Equivalence List2 : "+str(list1.contentEquivalence(list2)) + ' ')
