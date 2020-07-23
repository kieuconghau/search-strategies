#  Copyright (c) 2020 Kieu Cong Hau

from BFS import *
from UCS import *
from IDS import *
from GBFS import *
from TSA import *
from IOHandle import *

input_file_name = r"../INPUT/maze.txt"

graph, start, goal = read_maze(input_file_name)

if graph is None:
    print("Can not open the file \'" + input_file_name + "\'. Please check again.")
else:
    time, explored_nodes, path = breadth_first_search(graph, start, goal)
    print_solution("Breadth-first search", start, goal, time, explored_nodes, path)