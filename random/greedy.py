import timeit

def printJobScheduling(arr, t):
    # length of array
    n = len(arr)

    # Sort all jobs according to
    # decreasing order of profit
    for i in range(n):
        for j in range(n - 1 - i):
            if arr[j][2] < arr[j + 1][2]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    #print(arr)
                # To keep track of free time slots
    result = [False] * t

    # To store result (Sequence of jobs)
    job = ['-1'] * t
    total_profit = 0
    # Iterate through all given jobs
    for i in range(len(arr)):
        for j in range(min(t - 1, arr[i][1] - 1), -1, -1):

            # Free slot found
            if result[j] is False:
                result[j] = True
                job[j] = arr[i][0]
                total_profit += arr[i][2]
                break

    # print the sequence
    print(job)
    print("Total Profit is {}".format(total_profit))


# Driver COde
arr = [ ['a', 2, 100],  # Job Array
        ['c', 2, 27],
        ['d', 1, 25],
        ['b', 1, 19],
        ['e', 3, 15],
        ['f', 4, 25],
        ['g', 6, 17],
        ['h', 8, 80],
        ['i', 7, 70],
        ['j', 5, 35],

        ['k', 13, 35],
        ['l', 12, 27],
        ['m', 11, 40],
        ['o', 10, 80],
        ['p', 9, 13]
        ]

print("Following is maximum profit sequence of jobs")
start_time = timeit.default_timer()
printJobScheduling(arr, 13)  # Function Call
end_time = timeit.default_timer()

execution_time = end_time - start_time
print("Time of Execution is {}".format(execution_time))


