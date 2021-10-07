def powset(seq):
    if seq:
        p = powset(seq[1:])
        return p + [x + seq[:1] for x in p]
    else:
        return [[]]


s = input('Enter Input : ')
ll = []
s = s.split(',')
v = (powset(s))
for i in v:
    a = 1
    b = 0
    for j in i:
        j = j.split()
        a *= int(j[0])
        b += int(j[1])
        ll.append(abs(a - b))

print(min(ll))