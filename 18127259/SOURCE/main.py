#  Copyright (c) 2020 Kieu Cong Hau

from BFS import breadth_first_search
from UCS import uniform_cost_search
from IDS import iterative_deepening_search
from GBFS import greedy_best_first_search
from GSA import graph_search_a
from IOHandle import *

input_file_name = r"../INPUT/maze_3.txt"        # Change your input text file here

graph, start, goal = read_maze(input_file_name)

if graph is None:
    print("Can not open the file \'" + input_file_name + "\'. Please check again.")
else:
    time, explored_nodes, path = breadth_first_search(graph, start, goal)
    print_solution("Breadth-first search", start, goal, time, explored_nodes, path)

    time, explored_nodes, path = uniform_cost_search(graph, start, goal)
    print_solution("Uniform-cost search", start, goal, time, explored_nodes, path)

    time, explored_nodes_list, path = iterative_deepening_search(graph, start, goal)
    print_solution_ids(start, goal, time, explored_nodes_list, path)

    time, explored_nodes, path = greedy_best_first_search(graph, start, goal)
    print_solution("Greedy-best first search", start, goal, time, explored_nodes, path)

    time, explored_nodes, path = graph_search_a(graph, start, goal)
    print_solution("Graph-search A*", start, goal, time, explored_nodes, path)
