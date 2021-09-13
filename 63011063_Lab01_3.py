
print(" *** Summation of each digit ***")
user_input = input("Enter a positive number : ")

digits = [int(x) for x in str(user_input)]

input_sum = 0

for i in digits:
    input_sum += i

print("Summation of each digit =  {0}".format(input_sum))