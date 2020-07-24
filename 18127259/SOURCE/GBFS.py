#  Copyright (c) 2020 Kieu Cong Hau

import queue
import enum
import math
from collections import deque


class V(enum.Enum):
    NOT_VISITED = 0
    FRONTIER = 1
    EXPLORED = 2


def greedy_best_first_search(graph, start, goal):
    visited = dict()
    for state in graph:
        visited[state] = V.NOT_VISITED

    node = (manhattan_distance(graph, start, goal), start, None)    # node = (Manhattan distance, state, parent's state)
    frontier = queue.PriorityQueue()
    explored = []

    frontier.put(node)
    visited[node[1]] = V.FRONTIER

    while frontier.queue:
        node = frontier.get()
        explored.append((node[1], node[2]))
        visited[node[1]] = V.EXPLORED

        if node[1] == goal:
            return len(explored), [node[0] for node in explored], get_path(explored)

        child_state_list = sorted(graph[node[1]])
        for child_state in child_state_list:
            if visited[child_state] == V.NOT_VISITED:
                frontier.put((manhattan_distance(graph, child_state, goal), child_state, node[1]))
                visited[child_state] = V.FRONTIER
            elif visited[child_state] == V.FRONTIER:
                update(frontier, (manhattan_distance(graph, child_state, goal), child_state, node[1]))

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


def update(frontier, node):
    for f_node in frontier.queue:
        if f_node[1] == node[1] and f_node[0] > node[0] + 1:
            frontier.get(f_node)
            frontier.put(node)
            break


def manhattan_distance(graph, state, goal):
    n = math.sqrt(len(graph))
    state_x, state_y = int(state / n), state % n
    goal_x, goal_y = int(goal / n), goal % n
    return int(abs(state_x - goal_x) + abs(state_y - goal_y))
