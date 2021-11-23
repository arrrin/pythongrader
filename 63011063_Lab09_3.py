def Insertion(inp, ans, cur):
    # print(ans, cur)
    if len(inp) == 0:
        print("\nsorted")
        return

    if len(ans) == 0:
        ans.append(inp.pop(0))
        Insertion(inp, ans, 0)
    else:
        if cur < len(ans) and inp[0] > ans[cur]:
            Insertion(inp, ans, cur+1)
        else:

            temp = inp.pop(0)
            ans.insert(cur, temp)
            # print("*", temp, cur)
            print("insert {0} at index {1} :".format(temp, cur), end=" ")
            print(ans, end=" ")
            if inp:
                print(inp)
            Insertion(inp, ans, 0)
    return ans


inp = list(map(int, input("Enter Input : ").split()))
n = len(inp)
a = list()
# print(inp)
print(Insertion(inp, a, 0))