arr = [7, 9, 4, 13, 13, 5, 9, 8, 12, 11, 2, 1, 13, 10]

def bubbleSort(array):

    n = len(array) - 1

    for i in range(n):
        
        for j in range(n - i):

            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]

    print(array)


bubbleSort(arr)


