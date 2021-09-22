class Node:
    def __init__(self, value, next = None):
        self.value = value
        self.next = None
    def __str__(self):
        return str(self.value)


def create_list(l=[]):
    if len(l) == 0:
        return None
    p = Node(int(l[0]))
    head = p
    for i in l[1:]:
        p.next = Node(int(i))
        p = p.next
    return head


def print_list(H):
    p = H
    while p is not None:
        print(f"{p} ", end='')
        p = p.next
    print()


def mergeOrderesList(p, q):
    if p.value < q.value:
        m = p
        head = m
        p = p.next
    else:
        m = q
        head = m
        q = q.next

    while p is not None and q is not None:
        if p.value < q.value:
            m.next = p
            p = p.next
        else:
            m.next = q
            q = q.next
        m = m.next

    while p is not None:
        m.next = p
        p = p.next
        m = m.next
    while q is not None:
        m.next = q
        q = q.next
        m = m.next

    return head

inp = input('Enter 2 Lists : ').split(' ')
L1 = inp[0].split(",")
L2 = inp[1].split(",")

LL1 = create_list(L1)
LL2 = create_list(L2)
print('LL1 : ',end='')
print_list(LL1)
print('LL2 : ',end='')
print_list(LL2)

m = mergeOrderesList(LL1,LL2)
print('Merge Result : ',end='')
print_list(m)