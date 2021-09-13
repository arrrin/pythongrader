
def odd_list(alist):
    odd_list = []
    for num in alist:
        if not num % 2 == 0:
            odd_list.append(num)
        else:
            pass
    return odd_list

print(" ***Function Odd List***")
ls = [int(e) for e in input("Enter list numbers : ").split()]

opls = odd_list(ls)

print("Input list : ", ls, "\nOutput list : ", opls)