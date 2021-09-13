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


user_input = input("Enter expresion : ")

isParenthesis_unmatch = False

parenthesis_stack = Stack()
print(user_input, end=' ')
for char in user_input:
    if char == '[' or char == '{' or char == '(':
        parenthesis_stack.push(char)

    if char == ']' or char == '}' or char == ')':
        if parenthesis_stack.is_empty():
            isParenthesis_unmatch = True
            print('close paren excess')
            break
        if parenthesis_stack.peek() == '[' and char == ']' or \
                parenthesis_stack.peek() == '{' and char == '}' or \
                parenthesis_stack.peek() == '(' and char == ')':
            parenthesis_stack.pop()
        else:
            print("Unmatch open-close")
            isParenthesis_unmatch = True
            break

if parenthesis_stack.is_empty() and not isParenthesis_unmatch :
    print("MATCH")

elif not parenthesis_stack.is_empty() and not isParenthesis_unmatch:
    print('open paren excess   ' + str(len(parenthesis_stack.items))+ ' : ',end='')
    for items in parenthesis_stack.items:
        print(items,end='')
