import random
import timeit
import numpy as np
import matplotlib.pyplot as plt

class pair:
    def __init__(self):
        self.min = 0
        self.max = 0


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
    size_arr = np.arange(1,100)

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

    print("-------GRAPH-------")
    plt.plot(size_arr,time_arr)
    plt.xlabel('Array Size')
    plt.ylabel('Time (in sec)')
    plt.title('GRAPH')
    plt.show()


