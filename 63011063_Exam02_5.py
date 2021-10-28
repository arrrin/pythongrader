class Queue:
    def __init__(self, list = None):
        if list == None:
            self.items = []
        else:
            self.items = list

    def __str__(self):
        s = ''
        for i in self.items:
            s = s + str(i) + ' '
        if not self.isEmpty():
            return 'Queue data : ' + str(s)
        else:
            return 'Empty Queue'

    def __len__(self):
        return self.size()

    def enQueue(self, data):
        self.items.append(data)

    def deQueue(self):
        if len(self.items) <= 0:
            return "No element in the Stack"
        else:
            return self.items.pop(0)

    def size(self):
        return len(self.items)

    def isEmpty(self):
        return self.size() == 0


def check_duplicates(lst):
    for ele in lst:
        if lst.count(ele) > 1:
            return 'Duplicate'
    return 'NO Duplicate'


q = Queue()
user_input = input("Enter Input : ").split('/')
inp1 = user_input[0].split(' ')
inp2 = user_input[1].split(',')
for i in inp1:
    q.enQueue(i)
for txt in inp2:
    if txt[0] == 'D':
        q.deQueue()
    if txt[0] == 'E':
        q.enQueue(txt[2:])
print(check_duplicates(q.items))