import re


def is_palindrome(str_list,n):
    if str_list[0] == str_list[n]:
        str_list.pop(0)
        is_palindrome(str_list,n-1)
        return 'is palindrome'
    return 'is not palindrome'


inp = input("Enter Input : ")
print('\''+inp+'\'',end=' ')
inp = ''.join(e for e in inp if e.isalnum())
lst = []
for i in inp:
    lst.append(i.upper())

print(is_palindrome(lst,len(lst)-1))