class Stack:
    def __init__(self, list = None):
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

    def peek(self):
        return self.items[-1]


user_input = input("Enter Input : ").split()
s = Stack()
isDup = True
dup = 1
combo = 0
isCombo = True
for i in range(5):
    if not s.is_empty():
        user_input = s.items
        s.items = []
        dup =1
    for color in user_input:
        if not s.is_empty():
            if s.peek() == color:
                dup += 1
            else:
                dup = 1
        s.push(color)
        if dup == 3:
            s.pop()
            s.pop()
            s.pop()
            combo += 1
    if s.is_empty():
        break

print(s.size())
(s.items).reverse()
for i in s.items:
    print(i,end='')
if s.is_empty():
    if combo >= 2 :
        print("Empty")
        print("Combo : ",combo," ! ! !",sep="")
    else:
        print("Empty")
else:
    if combo >= 2:
        print("\nCombo : ",combo," ! ! !",sep="")


