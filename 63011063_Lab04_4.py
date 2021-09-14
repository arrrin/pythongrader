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


user_input = input("Enter Input : ").split(',')

mq = Queue()
yq = Queue()

mAct = Queue()
yAct = Queue()

for a in user_input:
    a = a.split(' ')
    mq.enqueue(a[0])
    yq.enqueue(a[1])

print('My   Queue = ', end='')

while not mq.is_empty():
    temp = ''
    a = mq.dequeue()
    if mq.size() == 0:
        print(a)
    else:
        print(a, end=', ');
    a = a.split(':')
    if a[0] == '0':
        temp += 'Eat:'
    elif a[0] == '1':
        temp += 'Game:'
    elif a[0] == '2':
        temp += 'Learn:'
    elif a[0] == '3':
        temp += 'Movie:'
    if a[1] == '0':
        temp += 'Res.'
    elif a[1] == '1':
        temp += 'ClassR.'
    elif a[1] == '2':
        temp += 'SuperM.'
    elif a[1] == '3':
        temp += 'Home'
    mAct.enqueue(temp)

print('Your Queue = ', end='')
while not yq.is_empty():
    temp = ''
    a = yq.dequeue()
    if yq.size() == 0:
        print(a)
    else:
        print(a, end=', ');
    a = a.split(':')
    if a[0] == '0':
        temp += 'Eat:'
    elif a[0] == '1':
        temp += 'Game:'
    elif a[0] == '2':
        temp += 'Learn:'
    elif a[0] == '3':
        temp += 'Movie:'
    if a[1] == '0':
        temp += 'Res.'
    elif a[1] == '1':
        temp += 'ClassR.'
    elif a[1] == '2':
        temp += 'SuperM.'
    elif a[1] == '3':
        temp += 'Home'
    yAct.enqueue(temp)

score = 0
my_print_temp = []
your_print_temp = []

while not mAct.is_empty():
    myTemp = mAct.dequeue()
    my_print_temp.append(myTemp)
    myTemp = myTemp.split(':')
    yourTemp = yAct.dequeue()
    your_print_temp.append(yourTemp)
    yourTemp = yourTemp.split(':')
    if (myTemp[0] == yourTemp[0]) and (myTemp[1] == yourTemp[1]):
        score += 4
    elif myTemp[0] == yourTemp[0]:
        score += 1
    elif myTemp[1] == yourTemp[1]:
        score += 2
    else:
        score -= 5

print('My   Activity:Location = ', end='')
for i in range(len(my_print_temp)):
    if i != len(my_print_temp) - 1:
        print(my_print_temp[i], end=', ')
    else:
        print(my_print_temp[i])
print('Your Activity:Location = ', end='')
for i in range(len(your_print_temp)):
    if i != len(your_print_temp) - 1:
        print(your_print_temp[i], end=', ')
    else:
        print(your_print_temp[i])

if score >= 7:
    print('Yes! You\'re my love! : Score is ' + str(score) + '.')

elif 0 < score < 7:
    print('Umm.. It\'s complicated relationship! : Score is ' + str(score) + '.')
else:
    print('No! We\'re just friends. : Score is ' + str(score) + '.')