from DAA.Travelling_Salesperson_Problem.dynamic_approach import TSP

if __name__ == '__main__':
    vertices = int(input("vertices? : "))

    distance_matrix = []
    for _ in range(vertices):
        print('Enter a Row : ',end="")
        temp_row = list(map(int,input().split(" ")))

        if len(temp_row) != vertices:
            print('Invalid input')
            break
        else:
            distance_matrix.append(temp_row)

    visited = [False] * vertices

    print('Starting Vertex? : ',end='')
    starting_vertex = int(input())

    visited[0] = True

    path = []
    path.append(starting_vertex)
    path_cost = {}
    TSP(distance_matrix, visited, 0, vertices, 1, 0, path, path_cost)

    print('Minimum cost of path is: ',end=" ")
    print(min(  [ i for i,j in path_cost.items()] ))


