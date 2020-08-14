import random
import timeit
import numpy as np
import matplotlib.pyplot as plt

def getMinMax(low, high, arr):
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
        arr_max1, arr_min1 = getMinMax(low, mid, arr)
        arr_max2, arr_min2 = getMinMax(mid + 1, high, arr)

    return (max(arr_max1, arr_max2), min(arr_min1, arr_min2))

time_arr = []
size_arr = np.arange(1,100)

for size in size_arr:

    arr = np.random.randint(0,1000,size)
    high = len(arr) - 1
    low = 0

    start_time = timeit.default_timer()
    arr_max, arr_min = getMinMax(low, high, arr)
    end_time = timeit.default_timer()

    time_of_execution = end_time - start_time
    time_arr.append(time_of_execution)
    # print('Minimum element is ', arr_min)
    # print('Maximum element is ', arr_max)
    # print('Time of Execution ', time_of_execution)

print("-------GRAPH-------")
plt.plot(size_arr,time_arr)
plt.xlabel('Array Size')
plt.ylabel('Time')
plt.title('GRAPH')
plt.show()