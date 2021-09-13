class Queue:

    def __init__(self, list=None):
        if list == None:
            self.items = []
        else:
            self.items = list

    def enqueue(self,data):
        self.items.append(data)

    def dequeue(self):
        if len(self.items) <= 0:
            return "No element in the Stack"
        else:
            return self.items.pop(0)
    def size(self):
        return len(self.items)

    def is_empty(self):
        return self.size() == 0

input = (input("Enter Input : ")).split(',')
q = Queue()

for lst in input:
    for alp in lst:
        if alp == 'E':
            num = [int(s) for s in lst.split() if s.isdigit()]
            q.enqueue(num[0])
            print("Add {0} index is {1} ".format(num[0], str(q.items.index(num[0]))))
        elif alp == 'D':
            if not q.size() == 0:
                pop_items = q.dequeue()
                print("Pop {0} size in queue is {1}".format(str(pop_items), q.size()))
            else:
                print("-1")
list_string = map(str,q.items)
if not q.is_empty():
    print("Number in Queue is : ",list(list_string))
else:
    print("Empty")