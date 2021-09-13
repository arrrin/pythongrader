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
       return self.size()==0

input = (input("Enter Input : ")).split(',')
s  = Stack()
for lst in input:
   for alphabet in lst:
       if alphabet == 'A':
          num =[int(s) for s in lst.split() if s.isdigit()]
          s.push(num[0])
          print("Add = {0} and Size = {1} ".format(num[0], str(s.size())))
       elif alphabet == 'P':
          if not s.size() == 0:

             print("Pop = {0} and Index = {1} ".format(s.pop(), str(s.size())))
          else:
             print("-1")

if(not s.is_empty()):
   print("Value in Stack = ",end='')
   for i in s.items:
      print(i,end=' ')
else:
   print("Value in Stack = Empty")