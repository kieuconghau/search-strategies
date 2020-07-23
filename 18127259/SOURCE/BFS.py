#  Copyright (c) 2020 Kieu Cong Hau

from collections import deque

def breadth_first_search(graph, start, goal):
    explored = [[], []]
    frontier = [deque(), deque()]
    state, parent = start, None

    if state == goal:
        explored[0].append(state)
        explored[1].append(parent)
        return len(explored[0]), explored[0], get_path(explored)

    frontier[0].append(state)
    frontier[1].append(parent)

    while frontier[0]:
        state, parent = frontier[0].popleft(), frontier[1].popleft()
        explored[0].append(state)
        explored[1].append(parent)

        neighbor_state_list = sorted(graph[state])
        for neighbor_state in neighbor_state_list:
            if (neighbor_state not in explored[0]) and (neighbor_state not in frontier[0]):
                if neighbor_state == goal:
                    explored[0].append(neighbor_state)
                    explored[1].append(state)
                    return len(explored[0]), explored[0], get_path(explored)
                frontier[0].append(neighbor_state)
                frontier[1].append(state)

    return None, explored[0], None


def get_path(explored):
    parent_table = dict()

    for i in range(len(explored[0])):
        parent_table[explored[0][i]] = explored[1][i]

    state, parent = explored[0][-1], explored[1][-1]
    path = deque([state])
    while parent is not None:
        state = parent
        parent = parent_table[state]
        path.appendleft(state)

    return list(path)