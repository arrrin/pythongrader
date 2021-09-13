count = int(input('Enter Input : '))
star = ''
plus = '+'
point = '.'
shape = '#'
max_y = (count+2)+4
max_x = (count+2)*2
for y in range(0,max_y) :
    if y==0 :
        print(((point.ljust(count+1,point)).ljust(count+1+1,shape)).ljust(max_x,plus))
    if y==1 :
        for i in range(0,count) :
            print(((((point.ljust(count-i,point)).ljust(count+1+1,shape)).ljust(count+3,plus)).ljust(max_x-1,shape)).ljust(max_x,plus))
    if y==count+1 :
        for x in range(0,2) :
            print((shape.ljust(count+2,shape)).ljust(max_x,plus))
    if y== count+3  :
        for i in range(count-1,-1,-1) :
            print(((((point.rjust(count-i,point)).rjust(count+1+1,plus)).rjust(count+3,shape)).rjust(max_x-1,plus)).rjust(max_x,shape))
    if y==max_y-1 :
        print(((point.rjust(count+1,point)).rjust(count+1+1,plus)).rjust(max_x,shape))
