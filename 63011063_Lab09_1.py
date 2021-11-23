class bubbleSort:
    def __init__(self, array):
        self.array = array
        self.length = len(array)

    def __str__(self):
        return " ".join([str(x)
                         for x in self.array])


    def bubbleSortRecursive(self, n=None):
        if n is None:
            n = self.length
        if n == 1:
            return

        for i in range(n - 1):
            if self.array[i] > self.array[i + 1]:
                self.array[i], self.array[i +
                                          1] = self.array[i + 1], self.array[i]

        self.bubbleSortRecursive(n - 1)


lst =[]
user_input = [int(i) for i in input("Enter Input : ").split()]
bbSort = bubbleSort(user_input)
bbSort.bubbleSortRecursive()
print(user_input)