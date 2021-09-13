class Stack:

    def __init__(self, list=None):
        if list == None:
            self.items = []
        else:
            self.items = list

    def push(self, data):
        self.items.append(data)

    def pop(self):
        if len(self.items) <= 0:
            return "No element in the Stack"
        else:
            return self.items.pop()

    def size(self):
        return len(self.items)

    def is_empty(self):
        return self.size() == 0


S = Stack()

inp = input('Enter Input : ').split(',')

n = inp[0].split()
answer = 0
for i in range(0, len(inp)):
    x = (inp[i].split())
    if x[0] == "A":
        S.push(x[1])
    if x[0] == "B":
        S.push("B")
for i in range(0, S.size()):
    if S.items[i] == 'B':
        high = i - 1
        for j in range(i - 1, -1, -1):
            if (S.items[j] != "B"):
                highest = S.items[j]
                high = j
                answer += 1
                break
        for j in range(high, -1, -1):
            if (S.items[j] != "B"):

                if (int(highest) <= int(S.items[j])):
                    if int(highest) < int(S.items[j]):
                        answer += 1
                    highest = S.items[j]
        print(answer)
        answer = 0