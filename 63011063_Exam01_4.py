def print_list(alist):
    for i in alist:
        print(i,end='')


print("*** String Rotation ***")

inp, inp2 = input("Enter 2 strings : ").split(' ')

count = 0
first_inp = []
f = []
second_inp = []
s = []

for i in inp:
    first_inp.append(i)
    f.append(i)
for i in inp2:
    second_inp.append(i)
    s.append(i)

first_inp.insert(0, first_inp.pop())
second_inp.append(second_inp.pop(0))

print("1",end=' ')
print_list(first_inp)
print("",end=' ')
print_list(second_inp)
count += 1
print("", end="\n")

while not (f == first_inp and s == second_inp):
    count += 1
    first_inp.insert(0, first_inp.pop())
    second_inp.append(second_inp.pop(0))
    if count <= 5:
        print(str(count),end=' ')
        print_list(first_inp)
        print("", end=' ')
        print_list(second_inp)
        print("",end="\n")
    else:
        pass
if count == 6:
    print(str(count), end=' ')
    print_list(first_inp)
    print("", end=' ')
    print_list(second_inp)
    print("", end="\n")
elif count > 5:
    print(' . . . . .')
    print(str(count),end=' ')
    print_list(first_inp)
    print("", end=' ')
    print_list(second_inp)
    print("",end="\n")
print("Total of  {0} rounds.".format(count))





