#  Copyright (c) 2020 Kieu Cong Hau

"""
Iterative deepening search (IDS for short)
Input:  the maze's info as a graph, start state, goal state
Return: - success: the time to escape the maze, the list of explored nodes, the list of nodes on the path found
        - failure: None, None, None
"""
def iterative_deepening_search(graph, start, goal):
    depth = 0
    time = 0
    explore_nodes_list = []

    while True:
        r_time, r_explored_nodes, r_path = depth_limited_tree_search(graph, start, goal, depth)

        if r_time is None:
            return None, None, None                     # failure

        explore_nodes_list.append(r_explored_nodes)
        time += r_time
        depth += 1

        if r_path is not None:
            return time, explore_nodes_list, r_path     # solution


"""
Depth limited tree search (DLTS for short)
Input:  the maze's info as a graph, start state, goal state, limit depth
Return: - success: the time to escape the maze, the list of explored nodes, the list of nodes on the path found
        - cutoff:  the time to try to escape the maze within the limit depth, the list of explored nodes, None
        - failure: None, None, None
"""
def depth_limited_tree_search(graph, start, goal, depth):
    if start == goal:
        return 1, [start], [start]

    explored = []
    current_path = []
    on_current_path = dict()
    for state in graph:
        on_current_path[state] = False

    return recursive_depth_limited_tree_search(graph, start, goal, depth, explored, current_path, on_current_path)


"""
Recursive depth limited tree search (RDLTS for short): Help the DLTS algorithm to explore nodes recursively.
Input:  the maze's info as a graph, start state, goal state, limit depth,
        the list of explored nodes, the list of nodes on the current path,
        the dictionary for checking if a node is on the currentpath
Return: - success: the time to escape the maze, the list of explored nodes, the list of nodes on the path found
        - cutoff:  the time to try to escape the maze within the limit depth, the list of explored nodes, None
        - failure: None, None, None
"""
def recursive_depth_limited_tree_search(graph, state, goal, depth, explored, current_path, on_current_path):
    explored.append(state)
    current_path.append(state)
    on_current_path[state] = True

    if state == goal:
        return len(explored), explored, current_path        # solution
    elif depth == 0:
        return len(explored), explored, None                # cutoff

    cutoff_occured = False

    child_state_list = sorted(graph[state])
    for child_state in child_state_list:
        if not on_current_path[child_state]:
            time, explored_nodes, path = recursive_depth_limited_tree_search(graph, child_state, goal, depth - 1,
                                                                             explored, current_path, on_current_path)

            if time is None or path is None:
                on_current_path[current_path.pop()] = False

            if time is not None and path is None:
                cutoff_occured = True
            elif path is not None:
                return time, explored_nodes, path       # not failure

    if cutoff_occured:
        return len(explored), explored, None            # cutoff

    return None, None, None                             # failure
