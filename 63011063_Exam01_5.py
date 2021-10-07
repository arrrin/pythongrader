class MyInt:
    def __init__(self,num):
        self.num = num
        self.prime_between = []

    def isPrime(self):
        if self.num == 2:
            return True
        elif self.num == 1 or self.num == 0 or self.num < 0:
            return False
        else:
            for i in range(2,self.num+1):
                if i == self.num:
                    return True
                if self.num % i == 0:
                    return False

    def showPrime(self):
        class InsideInt:
            def __init__(self, num):
                self.num = num
                self.prime_between = []

            def isPrime(self):
                if self.num == 2:
                    return True
                elif self.num == 1 or self.num == 0 or self.num < 0:
                    return False
                else:
                    for i in range(2, self.num + 1):
                        if i == self.num:
                            return True
                        if self.num % i == 0:
                            return False
        for i in range(2,self.num+1):
            num_temp = InsideInt(i)
            if num_temp.isPrime() and num_temp is not i:
                self.prime_between.append(i)

        return " ".join(list(map(str,self.prime_between)))

    def __sub__(self, other):
        return (self.num - int(other.num/2))


def print_list(alist):
    for i in alist:
        print(i,end=' ')



print(" *** class MyInt ***")
inp, inp2 = input("Enter 2 number : ").split(' ')

a = MyInt(int(inp))
b = MyInt(int(inp2))
print("{0} isPrime :".format(inp),end=" ")
print(a.isPrime())
print("{0} isPrime :".format(inp2),end=" ")
print(b.isPrime())
if int(inp) > 1 and int(inp2) > 1:
    print("Prime number between 2 and {0} : ".format(inp),end='')
    print(a.showPrime())
    print("Prime number between 2 and {0} : ".format(inp2),end='')
    print(b.showPrime())
elif int(inp) <= 1 < int(inp2):
    print("Prime number between 2 and {0} : ".format(inp), end='')
    print("!!!A prime number is a natural number greater than 1")
    print("Prime number between 2 and {0} : ".format(inp2), end='')
    print(b.showPrime())

elif int(inp2) <= 1 < int(inp):
    print("Prime number between 2 and {0} : ".format(inp), end='')
    print(a.showPrime())
    print("Prime number between 2 and {0} : ".format(inp2), end='')
    print("!!!A prime number is a natural number greater than 1")
elif int(inp) <=1 and int(inp2)<=1:
    print("Prime number between 2 and {0} : ".format(inp), end='')
    print("!!!A prime number is a natural number greater than 1")
    print("Prime number between 2 and {0} : ".format(inp2), end='')
    print("!!!A prime number is a natural number greater than 1")

print("{0} - {1} =".format(inp,inp2),end=' ')
print(a-b)