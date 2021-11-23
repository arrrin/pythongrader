def cal(cur):
    if temp[cur] != -1:
        return temp[cur]

    cal(2 * cur + 1)
    cal(2 * cur + 2)

    temp[cur] = min(temp[2 * cur + 2], temp[2 * cur + 1])
    temp[2 * cur + 1] -= temp[cur]
    temp[2 * cur + 2] -= temp[cur]


n, inp = input("Enter Input : ").split("/")
n = int(n)

inp = inp.split()
inp = list(map(int, inp))

if (n + 1) // 2 >= len(inp):
    temp = [-1] * n
    for i in range(len(inp)):
        temp[n // 2 + i] = inp[i]

    cal(0)
    print(sum(temp))

else:
    print("Incorrect Input")