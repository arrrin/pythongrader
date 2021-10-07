def swap_element(arr,i,j):
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp


def reverse_sort(arr, n):
    if n > 0:
        for i in range(0, n):
            if arr[i] <= arr[n - 1]:
                swap_element(arr, i, n - 1)
        reverse_sort(arr, n - 1)


def print_arr(arr,n):
    for i in range(0, n):
        print(arr[i],end=" ")


arr = list(input("Enter your List : ").split(','))
reverse_sort(arr,len(arr))

print("List after Sorted :",end=' ')

print(list(map(int,arr)))