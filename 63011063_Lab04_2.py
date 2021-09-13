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
            return "No element in the Queue"
        else:
            return self.items.pop(0)

    def size(self):
        return len(self.items)

    def is_empty(self):
        return self.size() == 0


user_input = list(input("Enter people : "))

q_main = Queue()
q_1 = Queue()
q_2 = Queue()

minute = 1
minute1 = 0
minute2 = 0

for people in user_input:
    q_main.enqueue(people)
q_main.dequeue()
q_1.enqueue(user_input[0])
minute1 += 1
print(minute,q_main.items,q_1.items,q_2.items)
for people in user_input:

    if (minute1 != 0) and (minute1%3 == 0) and (not q_1.is_empty()):
        q_1.dequeue()
    if (minute2 != 0) and (minute2%2 == 0) and (not q_2.is_empty()):
        q_2.dequeue()
    if q_1.size() < 5 and not q_main.is_empty():
        q_1.enqueue(q_main.dequeue())
    elif q_2.size() < 5 and not q_main.is_empty():
        q_2.enqueue(q_main.dequeue())

    if q_1.size() > 0:
        minute1 += 1
    elif q_1.size() == 0:
        minute1 = 0
    if q_2.size() > 0:
        minute2 += 1
    elif q_2.size() == 0:
        minute2 = 0

    minute += 1
    if q_main.is_empty():
        print(minute, q_main.items, q_1.items, q_2.items)
        break
    print(minute,q_main.items,q_1.items,q_2.items)