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


user_input = list(input("Enter code,hint : ").split(','))
letter = list(user_input[0])

diff = ord(user_input[-1])-ord(letter[0])
q = Queue()

for alp in letter:
        q.enqueue(chr(ord(alp)+diff))
        print(q.items)
