class Stack:
    def __init__(self, list = None):
        if list == None:
            self.items = []
        else:
            self.items = list

    def __str__(self):
        s =''
        for i in self.items:
            s = s + str(i) +' '
        return 'Data in Stack is : ' + str(s)

    def push(self, data):
        self.items.append(data)

    def pop(self):
        if len(self.items) <= 0:
            return "No element in the Stack"
        else:
            return self.items.pop()

    def size(self):
        return len(self.items)

    def isEmpty(self):
        return self.size() == 0

    def peek(self):
        return self.items[-1]

    def bottom(self):
        return self.items[0]


user_input = input("Enter choice : ")

if user_input == '1':
    s1 = Stack()
    s1.push(10)
    s1.push(20)
    print(s1)
    s1.pop()
    s1.push(30)
    print("Peek of stack :", s1.peek())
    print("Bottom of stack :", s1.bottom())
if user_input == '2':
    s1 = Stack()
    s1.push(100)
    s1.push(200)
    s1.push(300)
    s1.pop()
    print(s1)
    print("Stack is Empty :", s1.isEmpty())
if user_input == '3':
    s1 = Stack()
    s1.push(11)
    s1.push(22)
    s1.push(33)
    s1.pop()
    print(s1)
    print("Stack size :", s1.size())