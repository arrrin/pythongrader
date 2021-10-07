print(" *** Multiples of 3 or 5 or 7 ***")
inp = int(input("Enter number : "))
sum = 0
if inp < 0:
    print("Only positive number !!!")
else:
    for i in range(0,inp):
        if i % 3 == 0 or i%5 ==0 or i % 7==0:
            sum += i
    print("Result : " + str(sum))

