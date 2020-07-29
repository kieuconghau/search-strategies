#  Copyright (c) 2020 Kieu Cong Hau

import queue
import enum
from collections import deque


class V(enum.Enum):
    NOT_VISITED = 0     # state is not visited yet
    FRONTIER = 1        # state is in frontier
    EXPLORED = 2        # state is explored already


"""
Uniform-cost search (UCS for short)
Input:  the maze's info as a graph, start state, goal state
Return: - success: the time to escape the maze, the list of explored nodes, the list of nodes on the path found
        - failure: None, None, None
"""
def uniform_cost_search(graph, start, goal):
    visited = dict()
    for state in graph:
        visited[state] = V.NOT_VISITED

    node = (0, start, None)     # node = (path cost, state, parent's state)
    frontier = queue.PriorityQueue()
    explored = []

    frontier.put(node)
    visited[node[1]] = V.FRONTIER

    while frontier.queue:
        node = frontier.get()
        explored.append((node[1], node[2]))
        visited[node[1]] = V.EXPLORED

        if node[1] == goal:
            return len(explored), [node[0] for node in explored], get_path(explored)    # success

        child_state_list = sorted(graph[node[1]])
        for child_state in child_state_list:
            if visited[child_state] == V.NOT_VISITED:
                frontier.put((node[0] + 1, child_state, node[1]))
                visited[child_state] = V.FRONTIER
            elif visited[child_state] == V.FRONTIER:
                update(frontier, (node[0] + 1, child_state, node[1]))

    return None, None, None     # failure


"""
Get a path from the list of explored nodes
Input:  the list of explored nodes with the corresponding parents (node, node's parent)
Return: the list of nodes on the path found
"""
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


"""
Update  a node with the lower cost in the frontier
Input:  a froniter, a node.state that you want to update
Return: <update or no update>
"""
def update(frontier, node):
    temp_frontier = []
    while frontier.queue:
        temp_frontier.append(frontier.get())

    for temp_node in temp_frontier:
        if temp_node[1] == node[1]:
            if temp_node[0] > node[0]:
                temp_node = node
        frontier.put(temp_node)
