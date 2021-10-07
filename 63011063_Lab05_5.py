class Node:
    def __init__(self, value, next=None, previous=None):
        self.value = value
        self.next = next


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
    s = ''
    while p is not None:
        s += f"{p.value} "
        p = p.next
    return s


def size(head):
    p = head
    size = 0
    while p is not None:
        size += 1
        p = p.next
    return size


def bottom_up(head, split):
    old_head = head
    new_tail = head
    for _ in range(0, split - 1):
        new_tail = new_tail.next
    new_head = new_tail.next
    new_tail.next = None

    old_tail = new_head
    while old_tail.next is not None:
        old_tail = old_tail.next
    old_tail.next = old_head

    return new_head


def riffle_shuffle(head, split):
    n = head
    for _ in range(0, split - 1):
        n = n.next
    de_head = n.next
    n.next = None

    new_head = head
    p = head
    q = de_head
    while p.next is not None and q.next is not None:
        p_temp = p.next
        q_temp = q.next
        q_next = p.next
        p.next = q
        q.next = q_next
        p = p_temp
        q = q_temp

    if p.next is not None:
        q_next = p.next
        p.next = q
        q.next = q_next
    else:
        p.next = q

    return new_head


def is_straight(head, complement):
    p = head
    for _ in range(0, complement - 1):
        if int(p.value) + 1 != int(p.next.value):
            return False
        p = p.next
    return True


def scarmble(head, b, r, size):
    b_split = int(size * b / 100)
    r_split = int(size * r / 100)

    head = bottom_up(head, b_split)
    print(f"BottomUp {b:.3f} % : {print_list(head)}")

    head = riffle_shuffle(head, r_split)
    print(f"Riffle {r:.3f} % : {print_list(head)}")

    while not is_straight(head, size - b_split):
        head = riffle_shuffle(head, r_split)
    print(f"Deriffle {r:.3f} % : {print_list(head)}")

    head = bottom_up(head, size - b_split)
    print(f"Debottomup {b:.3f} % : {print_list(head)}")


inp1, inp2 = input('Enter Input : ').split('/')
print('-' * 50)
h = create_list(inp1.split())
for i in inp2.split('|'):
    print("Start : {0}".format(print_list(h)))
    k = i.split(',')
    if k[0][0] == "B" and k[1][0] == "R":
        scarmble(h, float(k[0][2:]), float(k[1][2:]), size(h))
    elif k[0][0] == "R" and k[1][0] == "B":
        scarmble(h, float(k[1][2:]), float(k[0][2:]), size(h))
    print('-' * 50)