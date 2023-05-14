# Project 1: Search

![Bigmaze png](http://ai.berkeley.edu/projects/release/multiagent/v1/002/pacman_multi_agent.png)

## Algorithm Expored and Lessons Learned

In this project, I have explored the following search algorithms:

- Reflex Agent
- Minimax
- Alpha-Beta Pruning
- Expectimax
- Evaluation Function

These algorithms are used to design agents for the classic version of Pacman, including ghosts.

More information about this project, please visit [Origional Source](http://ai.berkeley.edu/multiagent.html)

## Run Project 2 On Terminal
To run AI-Pacman with different searching algorithms, type the following command into the terminal:

### Reflex Agent

A capable reflex agent will have to consider both food locations and ghost locations to perform well. Run the program with:

```
python pacman.py -p ReflexAgent -l testClassic
python pacman.py --frameTime 0 -p ReflexAgent -k 1
python pacman.py --frameTime 0 -p ReflexAgent -k 2
```

---

### Minimax

```
python pacman.py -p MinimaxAgent -l minimaxClassic -a depth=4
python pacman.py -p MinimaxAgent -l trappedClassic -a depth=3
```

This Minimax expand the game tree to an arbitrary depth.

It has a 66.5% win rate against an adversary agent

---

### Alpha-Beta Pruning

```
python pacman.py -p AlphaBetaAgent -a depth=3 -l smallClassic
```

---

### Expectimax

```
python pacman.py -p ExpectimaxAgent -l minimaxClassic -a depth=3
```

Practice of modeling probabilistic behavior of agents who may make suboptimal choices

---

### Evaluation Function

```
python autograder.py -q q5
```

This part writes a better evaluation function for pacman that evaluate states, rather than actions like the reflex agent evaluation function did.