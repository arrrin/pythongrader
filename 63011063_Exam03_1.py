def init(n):
    if n ==0:
        return []
    return [n] + init(n-1)


def move(n,A,B,C):
    if n > 0:
        move(n-1,A,C,B)
        lst[C-1].append(lst[A-1].pop())
        print("move",n,"from ", chr(ord('A')+A-1), "to", chr(ord('A')+C-1))
        print("|  |  |")
        display_lst(lst[0], lst[1], lst[2], size)
        move(n-1,B,A,C)


def display_lst(a,b,c,n):
    if n != 0:
        if len(a)>=n:
            print(a[n-1], end='  ')
        else:
            print("| ", end=' ')
        if len(b)>=n:
            print(b[n-1], end='  ')
        else:
            print("| ", end=' ')
        if len(c)>=n:
            print(c[n-1], end='  ')
        else:
            print("| ", end='')
        print()
        display_lst(a,b,c,n-1)
    else:
        return


size = int(input("Enter Input : "))

lst = [[]]*3
lst[0] = init(size)
lst[1] = list()
lst[2] = list()

print("|  |  |")
display_lst(lst[0],lst[1],lst[2],size)
move(size,1,2,3)