group_of_num = [int(x) for x in input("Enter Your List : ").split()]
if len(group_of_num) <= 2:
    print("Array Input Length Must More Than 2")
else:
    sum = 5
    res = []
    res_1 = []
    for i in range(0, len(group_of_num)-2):
        for j in range(i + 1, len(group_of_num)-1):
            for k in range(j + 1, len(group_of_num)):
                if group_of_num[i] + group_of_num[j] + group_of_num[k] == sum:
                    temp = []
                    temp.append(group_of_num[i])
                    temp.append(group_of_num[j])
                    temp.append(group_of_num[k])
                    temp.sort()
                    res.append(temp)

for i in res:
    if i not in res_1:
        res_1.append(i)


print(res_1)