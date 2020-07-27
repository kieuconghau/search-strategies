#  Copyright (c) 2020 Kieu Cong Hau

import queue
import math
from collections import deque


"""
Tree-search A* (TSA for short)
Input:  the maze's info as a graph, start state, goal state
Return: - success: the time to escape the maze, the list of explored nodes, the list of nodes on the path found
        - failure: None, None, None
"""
def tree_search_a(graph, start, goal):
    node = (manhattan_distance(graph, start, goal), (start, 0), (None, 0))    # node = (Manhattan distance, state, parent's state)
    frontier = queue.PriorityQueue()
    explored = []
    frequency = dict()
    for state in graph:
        frequency[state] = 0

    frontier.put(node)

    while frontier.queue:
        node = frontier.get()
        explored.append((node[1], node[2]))

        if node[1][0] == goal:
            return len(explored), [node[0][0] for node in explored], get_path(explored)     # success

        child_state_list = sorted(graph[node[1][0]])
        for child_state in child_state_list:
            if child_state != node[2][0]:
                h_state = manhattan_distance(graph, node[1][0], goal)
                h_child_state = manhattan_distance(graph, child_state, goal)
                frontier.put((node[0] - h_state + 1 + h_child_state, (child_state, frequency[child_state]), node[1]))
                frequency[child_state] += 1

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
    path = deque([state[0]])
    while parent_state != (None, 0):
        state = parent_state
        parent_state = parent_table[state]
        path.appendleft(state[0])

    return list(path)


"""
Calculate the Manhattan distance (heuristic) of a state
Input:  the maze's info as a graph, the state that you want to calculate its Manhattan distance, goal state
Return: the Manhattan distance of the state
"""
def manhattan_distance(graph, state, goal):
    n = math.sqrt(len(graph))
    state_x, state_y = int(state / n), state % n
    goal_x, goal_y = int(goal / n), goal % n
    return int(abs(state_x - goal_x) + abs(state_y - goal_y))
