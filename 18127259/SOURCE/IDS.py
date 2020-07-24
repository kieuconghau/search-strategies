#  Copyright (c) 2020 Kieu Cong Hau

def iterative_deepening_search(graph, start, goal):
    depth = 0
    time = 0
    explore_nodes_list = []

    while True:
        r_time, r_explored_nodes, r_path = depth_limited_tree_search(graph, start, goal, depth)
        explore_nodes_list.append(r_explored_nodes)
        time += r_time

        depth += 1
        
        if r_time is None:                                      # failure
            return None, None, None
        elif r_path is not None:                                # solution
            return time, explore_nodes_list, r_path


def depth_limited_tree_search(graph, start, goal, depth):
    if start == goal:
        return 1, [start], [start]

    explored = []
    current_path = []
    on_current_path = dict()
    for state in graph:
        on_current_path[state] = False

    return recursive_depth_limited_tree_search(graph, start, goal, depth, explored, current_path, on_current_path)


def recursive_depth_limited_tree_search(graph, state, goal, depth, explored, current_path, on_current_path):
    explored.append(state)
    current_path.append(state)
    on_current_path[state] = True

    if state == goal:   # solution
        return len(explored), explored, current_path
    elif depth == 0:    # cutoff
        return len(explored), explored, None

    cutoff_occured = False

    child_state_list = sorted(graph[state])
    for child_state in child_state_list:
        if not on_current_path[child_state]:
            time, explored_nodes, path = recursive_depth_limited_tree_search(graph, child_state, goal, depth - 1,
                                                                             explored, current_path, on_current_path)

            if time is None or path is None:
                on_current_path[current_path.pop()] = False

            if time is not None and path is None:       # cutoff
                cutoff_occured = True
            elif path is not None:                      # not failure
                return time, explored_nodes, path

    if cutoff_occured:
        return len(explored), explored, None    # cutoff

    return None, None, None         # failure
