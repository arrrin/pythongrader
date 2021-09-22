class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None


class LinkedList:

    def __init__(self):
        self.head = None
        self.size = 0

    def __str__(self):
        if self.is_empty():
            return ""
        cur, s = self.head, str(self.head.value) + "->"
        while cur.next != None:
            s += str(cur.next.value) + '->'
            cur = cur.next
        return s[:-2]

    def str_reverse(self):
        last = None
        if self.is_empty():
            return ""
        if len(self) == 1:
            return self.head.value
        cur = self.head
        while cur.next != None:
            cur = cur.next
            last = cur
        s = ''
        while last is not None:
            s += str(last.value) + "->"
            last = last.prev
        return s[:-2]

    def __len__(self):
        return self.size

    def add_head(self, new_data):
        p = Node(new_data)
        p.next = self.head
        p.prev = None
        if self.head is not None:
            self.head.prev = p
        self.head = p
        self.size += 1

    def is_empty(self):
        return self.head == None

    def append(self, data):
        p = Node(data)
        t = self.head
        p.next = None

        if self.head is None:
            p.prev = None
            self.head = p
            self.size +=1
            return
        while t.next is not None:
            t = t.next
        t.next = p
        p.prev = t
        self.size += 1

    def insert(self,index,data):
        if index < 0 or index > len(self):
            return 'Data cannot be added'
        if self.head == None and index == 0:
            self.append(data)
            return 'index = ' + str(index) + ' and data = ' + data
        elif index == 0:
            self.add_head(data)
            return 'index = ' + str(index) + ' and data = ' + data
        elif index == len(self):
            self.append(data)
            return 'index = ' + str(index) + ' and data = ' + data
        i = 0
        t = self.head
        p = Node(data)
        while i != index:
            i += 1
            t = t.next
        if t.prev is not None:
            t.prev.next = p
            p.prev = t.prev
            t.prev = p
            p.next = t
        return 'index = ' + str(i) + ' and data = ' + str(data)

    def remove(self, data):
        if self.head is None:
            return 'Not Found!'
        p = Node(data)
        t = self.head
        i = 0
        while t != None:
            if t.value == p.value:
                if t.prev == None and t.next == None:
                    self.head = None
                elif t.prev != None:
                    t.prev.next = t.next
                else:
                    t.next.prev = None
                    self.head = t.next

                if t.next != None:
                    t.next.prev = t.prev
                elif t.next == None and t.prev != None:
                    t.prev.next = None
                break
            t = t.next
            i += 1
        self.size -= 1
        return 'removed : ' + str(p.value) + ' from index : ' + str(i)


L = LinkedList()
inp = input('Enter Input : ').split(',')
for i in inp:
    s = i.split()
    if s[0] == "I":
        j = s[1].split(":")
        print(L.insert(int(j[0]),j[1]))

    elif s[0] == "R":
        print(L.remove(s[1]))

    elif s[0] == "A":
        L.append(s[1])

    elif s[0] == "Ab":
        L.add_head(s[1])

    print("linked list : " + str(L) + "\nreverse : " + L.str_reverse())
