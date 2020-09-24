# Author            : Adhney Nawghare
# Roll No           : B - 34

import math

def dijkstra(matrix : list, locations, starting_vertex, ending_vertex):
    visited = [False] * locations

    actual_vertex = starting_vertex - 1
    distances = []
    path = []

    for i in range(locations):
        distances.append(matrix[actual_vertex][i])

    while False in visited:
        MIN = math.inf
        for k in range(len(distances)):
            if visited[k] == False and distances[k] < MIN:
                MIN = distances[k]
                index = k

        current_vertex = index
        visited[current_vertex] = True


        for j in range(len(distances)):
            if visited[j] == False and distances[current_vertex] + matrix[current_vertex][j] < distances[j]:
                path.append(j+1)
                distances[j] = distances[current_vertex] + matrix[current_vertex][j]

    print(distances)
    print(path)



if __name__ == "__main__":

    # taking a matrix as input
    locations = int(input('No. of locations? : '))

    matrix = [
        [0, 3, 1, 999, 999],
        [3, 0, 7, 5, 1],
        [1, 7, 0, 2, 999],
        [999, 5, 2, 0, 7],
        [999, 1, 999, 7, 0]
    ]
    # print("Enter the matrix Row Wise")
    # for i in range(locations):
    #     temp_row = list(map(int, input('row {}? : '.format(i+1)).split(" ")))
    #     matrix.append(temp_row)

    starting_vertex = int(input("Starting Vertex? : "))
    ending_vertex = int(input("Ending Vertex? : "))
    dijkstra(matrix, locations, starting_vertex, ending_vertex)