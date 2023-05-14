# Project 1: Search

![Bigmaze png](http://ai.berkeley.edu/projects/release/search/v1/001/maze.png)

## Algorithm Expored and Lessons Learned

In this project, I had the opportunity to implement and explore several search algorithms

- Depth-first search
- Breadth-first search
- Uniform cost search
- A* search algorithms
- Heuristic- based approaches

These algorithms are used to solve navigation and traveling salesman problems in the Pacman world
More information about this project, please visit [Origional Source](http://ai.berkeley.edu/search.html)

## Run Project 1 On Terminal
To run AI-Pacman with different searching algorithms, type the following command into the terminal:

---

### DFS, BFS, UCS

```
$ python pacman.py -l bigMaze -z .5 -p SearchAgent -a fn=<algorithm_name>
```

*Replace <algorithm_name> by dfs, bfs, ucs*

---

### A* Search and Heuristic

```
$ python pacman.py -l bigMaze -z .5 -p SearchAgent -a fn=astar,heuristic=manhattanHeuristic
```

---

### Finding All the Corners and Heuristic

```
python pacman.py -l tinyCorners -p SearchAgent -a fn=bfs,prob=CornersProblem
python pacman.py -l mediumCorners -p SearchAgent -a fn=bfs,prob=CornersProblem
python pacman.py -l mediumCorners -p AStarCornersAgent -z 0.5
```

Note: AStarCornersAgent is a shortcut for

`-p SearchAgent -a fn=aStarSearch,prob=CornersProblem,heuristic=cornersHeuristic.`

In this section, I have explored key concepts related to heuristics, including their admissibility, consistency, and the significance of non-trivial heuristics.

### Eating all the dots

```
$ python pacman.py -l trickySearch -p AStarFoodSearchAgent
```

### Suboptimal Search

```
python pacman.py -l bigSearch -p ClosestDotSearchAgent -z .5 
```