# UC-Berkeley-AI-Pacman-Project
## Intro
[The Pacman Projects](http://ai.berkeley.edu/project_overview.html) by the [University of California, Berkeley](http://berkeley.edu/).

![Pacman Overview gif](http://ai.berkeley.edu/images/pacman_game.gif)

This project focuses on exploring foundational AI concepts by implementing search algorithms for Pacman, the iconic video game character. The goal is to develop an intelligent Pacman Agent that can efficiently navigate mazes, collect food, and reach specific destinations.

## Getting Started
To get started with the UCBerkeley AI-Pacman-Project, follow the steps below:
1. Clone or download the project repository.
2. Install [Python](https://www.python.org/) and other necessary dependencies and libraries
3. Play a Pacman game by tpying in the terminal:```$ python pacman.py```
4. Check out all options and their default settings via:```$ python pacman.py -h```
5. Have fun!

## Project 1: Search

![Bigmaze png](http://ai.berkeley.edu/projects/release/search/v1/001/maze.png)

### Algorithm Expored and Lessons Learned
In this project, I had the opportunity to implement and explore several search algorithms

- Depth-first search
- Breadth-first search
- Uniform cost search
- A* search algorithms
- Heuristic- based approaches

These algorithms are used to solve navigation and traveling salesman problems in the Pacman world
More information about this project, please visit [here](http://ai.berkeley.edu/search.html)

### Run Project 1 On Terminal
To run AI-Pacman with different searching algorithms, type the following command into the terminal:

---

**DFS, BFS, UCS**

```
$ python pacman.py -l bigMaze -z .5 -p SearchAgent -a fn=<algorithm_name>
```

*Replace, the <algorithm_name> by dfs, bfs, ucs*

---

**A* Search and Heuristic**

```
$ python pacman.py -l bigMaze -z .5 -p SearchAgent -a fn=astar,heuristic=manhattanHeuristic
```