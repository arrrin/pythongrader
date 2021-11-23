def bubbleSort(arr):
    n = len(arr)

    for i in range(n - 1):

        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


def sortArray(a, n):
    ans = []
    for i in range(n):
        if (a[i] >= 0):
            ans.append(a[i])

    bubbleSort(ans)

    j = 0
    for i in range(n):
        if a[i] >= 0:
            a[i] = ans[j]
            j += 1
    for i in range(n):
        print(a[i], end=" ")



lst =[]
user_input = [int(i) for i in input("Enter Input : ").split()]
n = len(user_input)
sortArray(user_input, n)