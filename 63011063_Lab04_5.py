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

    def peek(self):
        if not self.is_empty():
            return self.items[0]
        return -1

    def clear(self):
        self.items = []

nor,mir = input("Enter Input (Normal, Mirror) : ").split()
norq = Queue()
mirq = Queue()
tempq = Queue()
outq = Queue()
defuse = []
for x in nor:
    norq.enqueue(x)
for x in mir[::-1]:
    mirq.enqueue(x)
while True:
    pop = False
    while mirq.size() > 0 or tempq.size() > 0:
        if tempq.size() < 3 and mirq.size() > 0:
            tempq.enqueue(mirq.peek())
            mirq.dequeue()
        elif all(element == tempq.items[0] for element in tempq.items) and tempq.size() == 3:
            defuse.append(tempq.peek())
            for j in range(3):
                tempq.dequeue()
            pop = True
            for i in mirq.items:
                outq.enqueue(i)
            mirq.clear()
            for i in outq.items:
                mirq.enqueue(i)
            outq.clear()
            break
        else:
            outq.enqueue(tempq.peek())
            tempq.dequeue()

    if not pop:
        if tempq.size() > 0:
            for i in range(tempq.size()):
                outq.enqueue(tempq.peek())
                tempq.dequeue()
        break
for i in outq.items:
    mirq.enqueue(i)
outq.clear()
mir_pop = len(defuse)
fail = 0
nor_pop = 0
while True:
    pop = False
    while norq.size() > 0 or tempq.size() > 0:
        if tempq.size() < 3 and norq.size() > 0:
            tempq.enqueue(norq.peek())
            norq.dequeue()
        elif tempq.size() >= 3 and len(defuse) > 0:
            if all(element == tempq.items[0] for element in tempq.items) and tempq.size() >= 3:
                tempq.items.insert(2, defuse[0])
                defuse.pop(0)
                pop = True
                if tempq.items[0] == tempq.items[1] == tempq.items[2]:
                    for j in range(3):
                        tempq.dequeue()
                    fail += 1
                    break
                else:
                    for j in range(tempq.size()):
                        outq.enqueue(tempq.peek())
                        tempq.dequeue()
                    break
            else:
                outq.enqueue(tempq.peek())
                tempq.dequeue()
        else:
            if all(element == tempq.items[0] for element in tempq.items) and tempq.size() == 3:
                pop = True
                for j in range(3):
                    tempq.dequeue()
                nor_pop += 1
                for i in norq.items:
                    outq.enqueue(i)
                norq.clear()
                for i in outq.items:
                    norq.enqueue(i)
                outq.clear()
            else:
                outq.enqueue(tempq.peek())
                tempq.dequeue()
    if not pop:
        if tempq.size() > 0:
            for i in range(tempq.size()):
                print(outq.items)
                outq.enqueue(tempq.peek())
                tempq.dequeue()
        break
for i in outq.items:
    norq.enqueue(i)
outq.clear()
print("NORMAL :")
print(norq.size())
if norq.size() == 0:
    print("Empty")
else:
    print(*(e for e in norq.items[::-1]),sep='')
print(nor_pop,"Explosive(s) ! ! ! (NORMAL)")
if fail > 0:
    print("Failed Interrupted",fail,"Bomb(s)")
print("------------MIRROR------------")
print(": RORRIM")
print(mirq.size())
if mirq.size() == 0:
    print("ytpmE")
else:
    print(*(e for e in mirq.items[::-1]),sep='')
print("(RORRIM) ! ! ! (s)evisolpxE",mir_pop)