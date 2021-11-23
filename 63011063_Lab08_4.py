def getPower(index, ls):
    if index >= len(ls):
        return 0
    else:
        return ls[index]+getPower(2*index+1,ls)+getPower(2*index+2,ls)

inp1, inp2 = input("Enter Input : ").split("/")
ls = []
inp1 = inp1.split()
for i in inp1:
    ls.append(int(i))
print(getPower(0,ls))
inp2 = inp2.split(",")
for j in range(len(inp2)):
    st = getPower(int(inp2[j][0]), ls)
    nd = getPower(int(inp2[j][2]), ls)
    f = int(inp2[j][0])
    s = int(inp2[j][2])
    if st == nd:
        print('{0}={1}'.format(f,s))
    elif st < nd:
        print('{0}<{1}'.format(f,s))
    else:
        print('{0}>{1}'.format(f,s))