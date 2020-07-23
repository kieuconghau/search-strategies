#  Copyright (c) 2020 Kieu Cong Hau

from collections import deque

def breadth_first_search(graph, start, goal):
    visited = dict()
    for state in graph:
        visited[state] = False

    node = (start, None)    # node = (state, parent's state)
    explored = []
    frontier = deque([node])
    visited[node[0]] = True

    if node[0] == goal:
        explored.append(node)
        return len(explored), [node[0] for node in explored], get_path(explored)

    while frontier:
        node = frontier.popleft()
        explored.append(node)

        child_state_list = sorted(graph[node[0]])
        for child_state in child_state_list:
            if not visited[child_state]:
                if child_state == goal:
                    explored.append((child_state, node[0]))
                    return len(explored), [node[0] for node in explored], get_path(explored)
                frontier.append((child_state, node[0]))
                visited[child_state] = True

    return None, None, None


def get_path(explored):
    parent_table = dict()
    for node in explored:
        parent_table[node[0]] = node[1]

    state, parent_state = explored[-1][0], explored[-1][1]
    path = deque([state])
    while parent_state is not None:
        state = parent_state
        parent_state = parent_table[state]
        path.appendleft(state)

    return list(path)
