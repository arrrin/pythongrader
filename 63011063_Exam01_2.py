print(" *** Divisible number ***")
inp = int(input("Enter a positive number : "))
count = 0
if inp <= 0:
    print(str(inp)+" is OUT of range !!!")
else:
    print("Output ==> ",end='')
    for i in range(1,inp+1):
        if inp % i ==0:
            count += 1
            print(i,end=' ')
    print("\nTotal ==> " + str(count))
