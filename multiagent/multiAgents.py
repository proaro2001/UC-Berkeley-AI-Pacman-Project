# multiAgents.py
# --------------
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


from util import manhattanDistance
from game import Directions
import random, util

from game import Agent

class ReflexAgent(Agent):
    """
    A reflex agent chooses an action at each choice point by examining
    its alternatives via a state evaluation function.

    The code below is provided as a guide.  You are welcome to change
    it in any way you see fit, so long as you don't touch our method
    headers.
    """


    def getAction(self, gameState):
        """
        You do not need to change this method, but you're welcome to.

        getAction chooses among the best options according to the evaluation function.

        Just like in the previous project, getAction takes a GameState and returns
        some Directions.X for some X in the set {NORTH, SOUTH, WEST, EAST, STOP}
        """
        # Collect legal moves and successor states
        legalMoves = gameState.getLegalActions()

        # Choose one of the best actions
        scores = [self.evaluationFunction(gameState, action) for action in legalMoves]
        bestScore = max(scores)
        bestIndices = [index for index in range(len(scores)) if scores[index] == bestScore]
        chosenIndex = random.choice(bestIndices) # Pick randomly among the best

        "Add more of your code here if you want to"

        return legalMoves[chosenIndex]

    def evaluationFunction(self, currentGameState, action):
        """
        Design a better evaluation function here.

        The evaluation function takes in the current and proposed successor
        GameStates (pacman.py) and returns a number, where higher numbers are better.

        The code below extracts some useful information from the state, like the
        remaining food (newFood) and Pacman position after moving (newPos).
        newScaredTimes holds the number of moves that each ghost will remain
        scared because of Pacman having eaten a power pellet.

        Print out these variables to see what you're getting, then combine them
        to create a masterful evaluation function.
        """
        # Useful information you can extract from a GameState (pacman.py)
        successorGameState = currentGameState.generatePacmanSuccessor(action)
        newPos = successorGameState.getPacmanPosition()
        newFood = successorGameState.getFood()
        newGhostStates = successorGameState.getGhostStates()
        newScaredTimes = [ghostState.scaredTimer for ghostState in newGhostStates]

        "*** YOUR CODE HERE ***"
        # Base Score
        score = successorGameState.getScore()

        # Distance to food
        suc_food_pos = newFood.asList()                         # successor food coordinate
        food_dist = [manhattanDistance(newPos , food) for food in suc_food_pos]
        min_food_dist = min(food_dist) if food_dist else 0
        score += 1.0/(min_food_dist + 1)                              # plus one to avoid divide by zero

        # Distance to ghost
        ghost_dist = [manhattanDistance(newPos, ghost.getPosition()) for ghost in newGhostStates]
        min_ghost_dist = min( ghost_dist ) if ghost_dist else 0
        score -= 1.0/ (min_ghost_dist + 1)                        # plus one to avoid divide by zero

        # Ghost is really close
        if min_ghost_dist < 2:
            score -= 10

        return score



def scoreEvaluationFunction(currentGameState):
    """
    This default evaluation function just returns the score of the state.
    The score is the same one displayed in the Pacman GUI.

    This evaluation function is meant for use with adversarial search agents
    (not reflex agents).
    """
    return currentGameState.getScore()

class MultiAgentSearchAgent(Agent):
    """
    This class provides some common elements to all of your
    multi-agent searchers.  Any methods defined here will be available
    to the MinimaxPacmanAgent, AlphaBetaPacmanAgent & ExpectimaxPacmanAgent.

    You *do not* need to make any changes here, but you can if you want to
    add functionality to all your adversarial search agents.  Please do not
    remove anything, however.

    Note: this is an abstract class: one that should not be instantiated.  It's
    only partially specified, and designed to be extended.  Agent (game.py)
    is another abstract class.
    """

    def __init__(self, evalFn = 'scoreEvaluationFunction', depth = '2'):
        self.index = 0 # Pacman is always agent index 0
        self.evaluationFunction = util.lookup(evalFn, globals())
        self.depth = int(depth)

class MinimaxAgent(MultiAgentSearchAgent):
    """
    Your minimax agent (question 2)
    """

    def getAction(self, gameState):
        """
        Returns the minimax action from the current gameState using self.depth
        and self.evaluationFunction.

        Here are some method calls that might be useful when implementing minimax.

        gameState.getLegalActions(agentIndex):
        Returns a list of legal actions for an agent
        agentIndex=0 means Pacman, ghosts are >= 1

        gameState.generateSuccessor(agentIndex, action):
        Returns the successor game state after an agent takes an action

        gameState.getNumAgents():
        Returns the total number of agents in the game

        gameState.isWin():
        Returns whether or not the game state is a winning state

        gameState.isLose():
        Returns whether or not the game state is a losing state
        """
        "*** YOUR CODE HERE ***"
        def minimax(agent, depth, gameState):
            """
            return the max utility if agent is Pacman ( agentIndex == 0 )
            return the min utility if agent is Ghost ( agentIndex >= 1 )

            :param agent:       agentIndex, 0 means Pacman, >=1 means Ghost
            :param depth        an int to represent the the agents'( Pacman or Ghost ) term
                                it starts by depth 0 ( Pacman's term )
            :param gameState:   It's the state like the coordinate in the first assignment
            :self.depth         when the depth reach self.depth, end the algorithm
            """
            # won/lost or depth reached, return self.evaluationFunction(gameState)
            if gameState.isWin() or gameState.isLose() or depth == self.depth:
                return self.evaluationFunction(gameState)
            legal_actions = gameState.getLegalActions(agent)    # next level nodes to look at
            
            # Last ghost(agent) to check, go next depth
            if agent == gameState.getNumAgents() - 1:
                # the min value of all pacman node(action) successors get from the function
                return min( minimax(0, depth + 1, gameState.generateSuccessor(agent, action) ) for action in legal_actions )
            # Pacman (agent == 0), max out result from it's node
            elif agent == 0:
                return max( minimax(agent + 1, depth, gameState.generateSuccessor(agent, action) ) for action in legal_actions ) 
            # the ghost in between
            else:
                return min( minimax(agent + 1, depth, gameState.generateSuccessor(agent, action) ) for action in legal_actions ) 
                

        # max for pacman
        # for all actions of pacman
        maximum = float("-inf")
        for agentState in gameState.getLegalActions(0):
            utility = minimax(1, 0, gameState.generateSuccessor(0,agentState))
            
            if utility > maximum:
                maximum = utility
                action = agentState
        return action

class AlphaBetaAgent(MultiAgentSearchAgent):
    """
    Your minimax agent with alpha-beta pruning (question 3)
    """

    def getAction(self, gameState):
        """
        Returns the minimax action using self.depth and self.evaluationFunction
        """
        def alpha_beta(agent, depth, gameState, alpha, beta):
            """
            return the max utility if agent is Pacman ( agentIndex == 0 )
            return the min utility if agent is Ghost ( agentIndex >= 1 )

            :param agent:       agentIndex, 0 means Pacman, >=1 means Ghost
            :param depth        an int to represent the the agents'( Pacman or Ghost ) term
                                it starts by depth 0 ( Pacman's term )
            :param gameState:   It's the state like the coordinate in the first assignment
            :self.depth         when the depth reach self.depth, end the algorithm
            """
            if gameState.isWin() or gameState.isLose() or depth == self.depth:
                return self.evaluationFunction(gameState)
            
            legal_actions = gameState.getLegalActions(agent)
            
            # figuring out what's the next agent and depth
            if agent == gameState.getNumAgents() - 1: 
                next_agent = 0
                next_depth = depth + 1
            else:
                next_agent = agent + 1
                next_depth = depth
            
            if agent == 0:  # if it's pacman, return maximum of it
                value = float('-inf')
                for action in legal_actions:
                    value = max(value, alpha_beta(next_agent, next_depth, gameState.generateSuccessor(agent, action), alpha, beta))
                    if value > beta:    # if value > beta, stop looking at the remainding node
                        return value    # those has zero chance 
                    alpha = max(alpha, value)
                return value
            else:   # if it's ghost return the minimum of it
                value = float('inf')
                for action in legal_actions:
                    value = min(value, alpha_beta(next_agent, next_depth, gameState.generateSuccessor(agent, action), alpha, beta))
                    if value < alpha:
                        return value
                    beta = min(beta, value)
                return value

        alpha = float('-inf')
        beta = float('inf')
        best_action = None
        best_value = float('-inf')

        for action in gameState.getLegalActions():
            value = alpha_beta(1, 0, gameState.generateSuccessor(0, action), alpha, beta)
            if value > alpha:
                alpha = value
                best_action = action

        return best_action


class ExpectimaxAgent(MultiAgentSearchAgent):
    """
      Your expectimax agent (question 4)
    """
    
    ######################################################################################################################
    
    def getAction(self, gameState):
        """
        Returns the expectimax action using self.depth and self.evaluationFunction

        All ghosts should be modeled as choosing uniformly at random from their
        legal moves.
        """
        "*** YOUR CODE HERE ***"
        def expectimax(agent, depth, gameState):
            """
            return the max utility if agent is Pacman ( agentIndex == 0 )
            return the min utility if agent is Ghost ( agentIndex >= 1 )

            :param agent:       agentIndex, 0 means Pacman, >=1 means Ghost
            :param depth        an int to represent the the agents'( Pacman or Ghost ) term
                                it starts by depth 0 ( Pacman's term )
            :param gameState:   It's the state like the coordinate in the first assignment
            :self.depth         when the depth reach self.depth, end the algorithm
            """
            # won/lost or depth reached, return self.evaluationFunction(gameState)
            if gameState.isWin() or gameState.isLose() or depth == self.depth:
                return self.evaluationFunction(gameState)
            legal_actions = gameState.getLegalActions(agent)    # next level nodes to look at
            
            # Last ghost(agent) to check, go next depth
            if agent == gameState.getNumAgents() - 1:
                # the average value of all pacman node(action) successors get from the function
                return sum( expectimax(0, depth + 1, gameState.generateSuccessor(agent, action) ) for action in legal_actions ) / len( legal_actions)
            # Pacman (agent == 0), max out result from it's node
            elif agent == 0:
                return max( expectimax(agent + 1, depth, gameState.generateSuccessor(agent, action) ) for action in legal_actions ) 
            # the ghost in between: looks at average of successors
            else:
                return sum( expectimax(agent + 1, depth, gameState.generateSuccessor(agent, action) ) for action in legal_actions ) / len(legal_actions)
                

        # max for pacman
        # for all actions of pacman
        maximum = float("-inf")
        for agentState in gameState.getLegalActions(0):
            utility = expectimax(1, 0, gameState.generateSuccessor(0,agentState))
            
            if utility > maximum:
                maximum = utility
                action = agentState
        return action
    ######################################################################################################################

def betterEvaluationFunction(currentGameState):
    """
    Your extreme ghost-hunting, pellet-nabbing, food-gobbling, unstoppable
    evaluation function (question 5).

    DESCRIPTION:
    includes:
    1/distance to closest food
    minimum ghost distance
    if ghosts are scared
    if ghost is really close
    distance to capsule
    """
    "*** YOUR CODE HERE ***"

    ####################################################################################################################################################################################
    #successorGameState = currentGameState.generatePacmanSuccessor(action)       #use another thing besides "action" to look at successors, or dont look at succesors at all??
    newPos = currentGameState.getPacmanPosition()
    newFood = currentGameState.getFood()
    newGhostStates = currentGameState.getGhostStates()
    newScaredTimes = [ghostState.scaredTimer for ghostState in newGhostStates]


    # Base Score
    score = currentGameState.getScore()

    # Distance to food
    suc_food_pos = newFood.asList()                         # successor food coordinate
    food_dist = [manhattanDistance(newPos , food) for food in suc_food_pos]
    min_food_dist = min(food_dist) if food_dist else 0
    score += 1.0/(min_food_dist + 1)                        # plus one to avoid divide by zero

    # Distance to ghost
    ghost_dist = [manhattanDistance(newPos, ghost.getPosition()) for ghost in newGhostStates]
    min_ghost_dist = min( ghost_dist ) if ghost_dist else 0
    score -= 1.0/ (min_ghost_dist + 1)                      # plus one to avoid divide by zero
    
    #for all ghosts, go to the closest one that is scared
        #write code here
    for i in range( len( newScaredTimes ) ):
        is_scared_and_within_range = newScaredTimes[i] - ghost_dist[i] > 0
        if is_scared_and_within_range:
            score += 1.0 / (newScaredTimes[i] - ghost_dist[i] + 1)

    # getting closer to the capsule
    # in pacmany.py, a function getCapsules(self) 
    # Returns a list of positions (x,y) of the remaining capsules.
    # capsules_pos = currentGameState.getCapsules()
    # capsules_dist = [manhattanDistance(caps_pos, newPos) for caps_pos in capsules_pos]
    # min_capsules_dist = min(capsules_dist) if capsules_dist else 0
    # score += 1.0 / (min_capsules_dist + 1)
    
    # check if eating any capsules
    capsules_pos = currentGameState.getCapsules()
    total_capsules = 1 if not capsules_pos else len( capsules_pos )
    # if the capsules getting less, mean pacman eats more, and the scores gets bigger
    score += 1.0 / total_capsules


    # Ghost is really close
    if min_ghost_dist < 2:
        score -= 10

    # # Stopping action
    # if action == Directions.STOP:
    #     score -= 10

    # print( f"{action}: {score}")
    return score
    
    ######################################################################################################################################################################################

# Abbreviation
better = betterEvaluationFunction
