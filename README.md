Author: **Kiều Công Hậu**  
ID: 18127259  
Contact: <kieuconghau2000@gmai.com>  
Course: Artificial Intelligence - HCMUS  

<h1 align='center'>SEARCH STRATEGIES</h1>

## Problem description
A robot has been sent to a maze of size 𝑁 × 𝑁 and it must navigate the maze to reach the exit. Given that the robot has the map of the maze and it knows that its initial location is at square 0 and needs to reach some square E (from 0 to 𝑁<sup>2</sup> − 1) to go out of the maze. The below figure demonstrates a maze of size 8 × 8 and the exit 𝐸 is at square 61. 

<p align="center"><img align='center' src="https://github.com/kieuconghau/search-strategies/blob/master/18127259/INPUT/maze_0.png"></p>

Let's use our AI knowledge to help the robot search its path out of the maze. You are asked to implement the following search strategies and provide their output results.
- *Breadth-first search*
- *Uniform-cost search*
- *Iterative deepening search* that uses depth-first tree search as core component and avoids loops by checking a new node against the current path
- *Greedy-best first search* using the Manhattan distance as heuristic
- *Tree-search A\** using the same heuristic as above For consistency, the goal node (i.e., the exit) will be included to every list of explored nodes (though not all strategies really put it to the frontier).

**Output:** Print to the console the following information
- The time to escape the maze
- The list of explored nodes (in correct order)
- The list of nodes on the path found (in correct order). 

[More detail](https://github.com/kieuconghau/search-strategies/blob/master/2020-CSC14003-18CLC-Lab01.pdf)


## My submission
- [Source code](https://github.com/kieuconghau/search-strategies/tree/master/18127259/SOURCE)
- [Input](https://github.com/kieuconghau/search-strategies/tree/master/18127259/INPUT)
- [Output](https://github.com/kieuconghau/search-strategies/tree/master/18127259/OUTPUT)
- [Report](https://github.com/kieuconghau/search-strategies/blob/master/18127259/DOCUMENT/Report.pdf)
