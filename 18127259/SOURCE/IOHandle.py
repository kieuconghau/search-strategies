#  Copyright (c) 2020 Kieu Cong Hau

# Read the maze's info from file
# (graph, start state and goal state)
def read_maze(input_file_name):
    try:
        f = open(input_file_name, "r")
    except FileNotFoundError:
        return None, None, None

    with f:
        graph = dict()
        n = int(f.readline())
        for i in range(n * n):
            graph[i] = [int(x) for x in f.readline().split()]
        goal = int(f.readline())
        f.close()
        return graph, 0, goal


# Print the maze's solution to the console
# (the time to escape the maze, the list of explored nodes, the list of nodes on the path found)
def print_solution(search_stratey, start, goal, time, explored_nodes, path):
    print(search_stratey + " (Start: " + str(start) + "; Goal: " + str(goal) + ")")

    if time is None:
        print("Can not find the path to escape this maze.")
    else:
        print(" - The time to escape the maze: ", end="")
        print(time)
        print(" - The list of explored nodes: ", end="")
        print(explored_nodes)
        print(" - The list of nodes on the path found: ", end="")
        print(path)
        print()