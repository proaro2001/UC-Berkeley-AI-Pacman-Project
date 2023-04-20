# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).

"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    print("Start's successors:", problem.getSuccessors(problem.getStartState()))
    """
    "*** YOUR CODE HERE ***"
    ###########################################################################
    # version 1
    ###########################################################################
    # # # get the successors, it already excluded the walls from the successors
    # start_state = problem.getStartState()
    # # initalize variables
    # fringe = util.Stack()   # stack to store the path to goal
    # visited = set()         # list to store visited successor
    # path = [ start_state ]  # the list to return the path

    # fringe.push( start_state ) # set up the first element to look at

    # while ( not fringe.isEmpty() ):
    #     currNode = fringe.pop() # variable for current node 
    #     print( "Current: ", currNode)

    #     visited.add(currNode) # mark currNode as visited
    #     if problem.isGoalState(currNode):
    #         print( "Find the goal! ")
    #         return path # not sure if we can do this tho
        
    #     # if it's not goal, keep checking the fringe
    #     sucessors = problem.getSuccessors( currNode )
    #     # push all of them into the fringe
    #     for successor, action, stepCost in sucessors:
    #         # if visited, check the next successor
    #         if successor in visited:
    #             continue
    #         # if not visited
    #         else:
    #             fringe.push(successor)   # check this one next
    #             path.append(action)       # push to path
    #             break # break for the for each loop

    ######################################################################

    
    # ###########################################################################
    # # version 2
    # ###########################################################################
    # # initalize variables
    # currNode = problem.getStartState()  # start_stat
    # fringe = util.Stack()               # store used node, push whenever currNode change
    # node = []                           
    # visited = []                        # list to store visited successor
    # path = []                           # the list to return the path

    # # initalize values
    # while True:
    #     import time
    #     time.sleep(2)
    #     print( "Current: ", currNode)

    #     # found goal
    #     if problem.isGoalState(currNode):
    #         return path
        
    #     # not final goal
    #     if currNode not in visited:
    #         visited.append(currNode)
    #     time.sleep(2)
    #     print( "Append to visited: ", visited)
    #     node.append(currNode)
    #     successors = problem.getSuccessors( currNode )
    #     # check every successor and find the first one not visited
    #     for successor, action, stepCost in successors:
    #         if successor not in visited:
    #             fringe.push(currNode)
    #             currNode = successor
    #             path.append(action)
    #             break
        
    #     if currNode == node[len(node)-1]:
    #         time.sleep(2)
    #         print( currNode, " == ", node[len(node) - 1])
    #         # node.pop()
    #         print( "Node Pop", node.pop() )
    #         currNode = fringe.pop()
    #         print( "CurrentNode is :", currNode )
    #         path.pop()
    #         print("Path:" , path)
        
    #     if len(node) == 0:
    #         break

    # return path
    ###########################################################################
    
    ###########################################################################
    # version 3
    # Ronan modified the origional version after researching
    # instead of seperating the path and stack
    # combining them is something I didn't expect
    ###########################################################################
    
    
    # declare variables
    start_stat = problem.getStartState()    # current Node we looking at
    fringe = util.Stack()                   # stack to store the state and path to the goal
    visited = set()                         # list to store visited node

    # initalize fringe
    fringe.push( (start_stat, []) )         # set up the first node to check

    while not fringe.isEmpty():

        # get the node being checking next
        currNode, path = fringe.pop()

        # if Node has been visited, go to the next while loop 
        # for checking the top element on fringe
        if currNode in visited:
            continue 

        # Reaching here means the code hasn't been visited
        # mark as visited
        visited.add(currNode)

        # when currNode is the Goal we return the path
        if problem.isGoalState(currNode):
            return path
        
        # get the successors list
        successors = problem.getSuccessors(currNode)
        
        # push all the successors with path (in a tuple) to the fringe
        for successor, action, stepCost in successors:
                fringe.push( (successor, path + [action] ) ) # old path plus new action (list) here
    
    return [] # reaching here means failure in finding the path




def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    # util.raiseNotDefined()
    
    # declare variable
    fringe = util.Queue()                   # Queue for BFS
    visited = []                            # visited node
    start_stat = problem.getStartState()    # state to start with

    # initalize fringe
    fringe.push( (start_stat, []) )  # (state, action)
    while ( not fringe.isEmpty() ):

        # get the node to check with
        currNode, path = fringe.pop()
        
        
        # if node visited, check next node in fringe
        if currNode in visited:
            continue

        # node not visited
        # mark as visited
        visited.append(currNode)

        # check reach goal
        if problem.isGoalState(currNode):
            return path
        
        # get the successors list
        successors = problem.getSuccessors(currNode)
        
        # push all the successors with path (in a tuple) to the fringe
        for successor, action, stepCost in successors:
            fringe.push( (successor, path + [action] ) )
    
    
    return [] # reaching here means failure in finding the path


def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    # util.raiseNotDefined()

    # delcare variables
    fringe = util.PriorityQueue()
    visited = set()
    start_state = problem.getStartState()

    # initalize fringe
    fringe.push( ( start_state, [], 0 ), 0)
    while ( not fringe.isEmpty() ):

        # extract the currNode information
        currNode,path, currCost = fringe.pop()

        # when its' visited
        if currNode in visited:
            continue

        # mark as visited
        visited.add(currNode)

        # check reach goal
        if problem.isGoalState(currNode):
            return path
        
        # get the successors list
        successors = problem.getSuccessors(currNode)
        
        # push all the successors with path (in a tuple) to the fringe
        for successor, action, stepCost in successors:
            new_Cost = currCost + stepCost
            fringe.push( (successor, path + [action], new_Cost ) , new_Cost)
    return []

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    # a* = f+g
    fringe = util.PriorityQueue()
    visited = []
    start_state = problem.getStartState()

    fringe.push( (start_state, [], 0), 0 )
    while ( not fringe.isEmpty() ):
        # extract the currNode information
        currNode,path, currCost = fringe.pop()

        # when its' visited
        if currNode in visited:
            continue

        # mark as visited
        visited.append(currNode)

        # check reach goal
        if problem.isGoalState(currNode):
            return path
        
        # get the successors list
        successors = problem.getSuccessors(currNode)
        
        # push all the successors with path (in a tuple) to the fringe
        for successor, action, stepCost in successors:
            new_Cost = currCost + stepCost
            h_cost = new_Cost + heuristic(successor, problem)
            fringe.push( (successor, path + [action], new_Cost ) , h_cost)
    return []
    # util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
