def TSP(distance_matrix, visited, current_vertex, vertices, count, cost,
        path : list, path_list : dict):

    if count == vertices and distance_matrix[current_vertex][0] > 0:
        path_list.update({ cost + distance_matrix[current_vertex][0] : path})
        return

    for i in range(vertices):
        if visited[i] == False and distance_matrix[current_vertex][i] > 0:

            visited[i] = True
            path.append(i)
            TSP(distance_matrix, visited, i, vertices, count+1,
                cost+distance_matrix[current_vertex][i], path, path_list)

            visited[i] = False
