print(" *** String count ***")

inp = input("Enter message : ")

count_upper = 0
upper_unique = []
count_lower = 0
lower_unique = []


for i in inp:
    if i.isupper():
        count_upper += 1
        if i not in upper_unique:
            upper_unique.append(i)
for i in inp:
    if i.islower():
        count_lower += 1
        if i not in lower_unique:
            lower_unique.append(i)

upper_unique.sort()
lower_unique.sort()
print("No. of Upper case characters : "+str(count_upper))
print("Unique Upper case characters : ",end='')
for i in upper_unique:
    print(i,end='  ')

print("\nNo. of Lower case Characters : "+str(count_lower))
print("Unique Lower case characters : ",end='')
for i in lower_unique:
    print(i,end='  ')
