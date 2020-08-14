import random
import timeit
import numpy as np
import matplotlib.pyplot as plt

class pair:
    def __init__(self):
        self.min = 0
        self.max = 0

def getMinMax2(low, high, arr):
    arr_max = arr[low]
    arr_min = arr[low]

    # If there is only one element
    if low == high:
        arr_max = arr[low]
        arr_min = arr[low]
        return (arr_max, arr_min)

        # If there is only two element
    elif high == low + 1:
        if arr[low] > arr[high]:
            arr_max = arr[low]
            arr_min = arr[high]
        else:
            arr_max = arr[high]
            arr_min = arr[low]
        return (arr_max, arr_min)
    else:

        # If there are more than 2 elements
        mid = int((low + high) / 2)
        arr_max1, arr_min1 = getMinMax2(low, mid, arr)
        arr_max2, arr_min2 = getMinMax2(mid + 1, high, arr)

    return (max(arr_max1, arr_max2), min(arr_min1, arr_min2))

def getMinMax(arr: list, n: int) -> pair:
    minmax = pair()

    # If there is only one element then return it as min and max both
    if n == 1:
        minmax.max = arr[0]
        minmax.min = arr[0]
        return minmax

        # If there are more than one elements, then initialize min
    # and max
    if arr[0] > arr[1]:
        minmax.max = arr[0]
        minmax.min = arr[1]
    else:
        minmax.max = arr[1]
        minmax.min = arr[0]

    for i in range(2, n):
        if arr[i] > minmax.max:
            minmax.max = arr[i]
        elif arr[i] < minmax.min:
            minmax.min = arr[i]

    return minmax


# Driver Code
if __name__ == "__main__":
    time_arr = []
    size_arr = np.arange(1,1000)

    time_arr2 = []
    size_arr2 = np.arange(1, 1000)

    for size in size_arr:

        arr = random.sample(range(0,1000),size)
        high = len(arr) - 1
        low = 0

        start_time = timeit.default_timer()
        minmax = getMinMax(arr, size)
        end_time = timeit.default_timer()

        time_of_execution = end_time - start_time
        time_arr.append(time_of_execution)

    # print('Minimum element is ', minmax.min)
    # print('Maximum element is ', minmax.max)
    # print('Time of Execution ', time_of_execution)

    for size2 in size_arr2:
        arr = np.random.randint(0, 1000, size2)
        high = len(arr) - 1
        low = 0

        start_time = timeit.default_timer()
        arr_max, arr_min = getMinMax2(low, high, arr)
        end_time = timeit.default_timer()

        time_of_execution = end_time - start_time
        time_arr2.append(time_of_execution)

    print("-------GRAPH-------")
    plt.plot(size_arr,time_arr,label='min-max')
    plt.plot(size_arr2,time_arr2,'r',label='min-max with DAC')
    plt.xlabel('Array Size')
    plt.ylabel('Time (in sec)')
    plt.title('GRAPH')
    plt.legend()
    plt.show()


