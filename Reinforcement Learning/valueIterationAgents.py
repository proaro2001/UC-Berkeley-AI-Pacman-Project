# valueIterationAgents.py
# -----------------------
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


# valueIterationAgents.py
# -----------------------
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


import mdp, util

from learningAgents import ValueEstimationAgent
import collections


class ValueIterationAgent(ValueEstimationAgent):
    """
    * Please read learningAgents.py before reading this.*

    A ValueIterationAgent takes a Markov decision process
    (see mdp.py) on initialization and runs value iteration
    for a given number of iterations using the supplied
    discount factor.
    """

    def __init__(self, mdp, discount=0.9, iterations=100):
        """
        Your value iteration agent should take an mdp on
        construction, run the indicated number of iterations
        and then act according to the resulting policy.

        Some useful mdp methods you will use:
            mdp.getStates()
            mdp.getPossibleActions(state)
            mdp.getTransitionStatesAndProbs(state, action)
            mdp.getReward(state, action, nextState)
            mdp.isTerminal(state)
        """
        self.mdp = mdp
        self.discount = discount
        self.iterations = iterations
        self.values = util.Counter()  # A Counter is a dict with default 0
        self.runValueIteration()

    def runValueIteration(self):
        # Write value iteration code here
        "*** YOUR CODE HERE ***"
        # value iteration explaination
        # assign q value to each state for self.iterations times
        for i in range(self.iterations):
            # create an empty Counter to store the new values
            new_values = util.Counter()
            # iterate through all states
            for state in self.mdp.getStates():
                # if state is terminal, skip
                if self.mdp.isTerminal(state):
                    continue
                # find the best action for the state
                best_action = self.computeActionFromValues(state)
                # update the value of the state
                new_values[state] = self.computeQValueFromValues(state, best_action)
            # update the values dict
            self.values = new_values



    def getValue(self, state):
        """
        Return the value of the state (computed in __init__).
        """
        return self.values[state]

    def computeQValueFromValues(self, state, action):
        """
        Compute the Q-value of action in state from the
        value function stored in self.values.
        """
        "*** YOUR CODE HERE ***"
        # q value of state = max(list of neighbor q values)
        q_value = 0
        for transition_state, probability in self.mdp.getTransitionStatesAndProbs(state, action):
            # transition_state is the neighbor state, coordinate in this case
            # probability is the probability of going to that particular transition state
            # Q(s,a) = sum(T(s,a,s') * (R(s,a,s') + discount * V(s')))
            rewards = self.mdp.getReward(state, action, transition_state)
            q_value += probability * (rewards + self.discount * self.getValue(transition_state))
        return q_value

    def computeActionFromValues(self, state):
        """
        The policy is the best action in the given state
        according to the values currently stored in self.values.

        You may break ties any way you see fit.  Note that if
        there are no legal actions, which is the case at the
        terminal state, you should return None.
        """
        "*** YOUR CODE HERE ***"
        # choose action from getPossibleAction() that puts you in the state with best q value
        actions = self.mdp.getPossibleActions(state) # list of possible actions
        if not actions:
            return None
        bestAction = max(actions, key=lambda x: self.computeQValueFromValues(state, x))
        # Iterate the actions list and apply the computeQValueFromValues function to each action
        # The result from the computeQValueFromValues function is the q value of that action
        # and used to compare with the current best q value
        return bestAction


    def getPolicy(self, state):
        return self.computeActionFromValues(state)

    def getAction(self, state):
        "Returns the policy at the state (no exploration)."
        return self.computeActionFromValues(state)

    def getQValue(self, state, action):
        return self.computeQValueFromValues(state, action)


class AsynchronousValueIterationAgent(ValueIterationAgent):
    """
    * Please read learningAgents.py before reading this.*

    An AsynchronousValueIterationAgent takes a Markov decision process
    (see mdp.py) on initialization and runs cyclic value iteration
    for a given number of iterations using the supplied
    discount factor.
    """

    def __init__(self, mdp, discount=0.9, iterations=1000):
        """
        Your cyclic value iteration agent should take an mdp on
        construction, run the indicated number of iterations,
        and then act according to the resulting policy. Each iteration
        updates the value of only one state, which cycles through
        the states list. If the chosen state is terminal, nothing
        happens in that iteration.

        Some useful mdp methods you will use:
            mdp.getStates()
            mdp.getPossibleActions(state)
            mdp.getTransitionStatesAndProbs(state, action)
            mdp.getReward(state)
            mdp.isTerminal(state)
        """
        ValueIterationAgent.__init__(self, mdp, discount, iterations)

    def runValueIteration(self):
        "*** YOUR CODE HERE ***"
        # asynchronous value iteration explaination
        # same as Value Iteration but update one value at a time
        # iterate through all states for self.iterations times
        for i in range(self.iterations):
            # get the state to update
            state = self.mdp.getStates()[i % len(self.mdp.getStates())]
            # if state is terminal, skip
            if self.mdp.isTerminal(state):
                continue
            # find the best action for the state
            best_action = self.computeActionFromValues(state)
            # update the value of the state
            self.values[state] = self.computeQValueFromValues(state, best_action)


class PrioritizedSweepingValueIterationAgent(AsynchronousValueIterationAgent):
    """
    * Please read learningAgents.py before reading this.*

    A PrioritizedSweepingValueIterationAgent takes a Markov decision process
    (see mdp.py) on initialization and runs prioritized sweeping value iteration
    for a given number of iterations using the supplied parameters.
    """

    def __init__(self, mdp, discount=0.9, iterations=100, theta=1e-5):
        """
        Your prioritized sweeping value iteration agent should take an mdp on
        construction, run the indicated number of iterations,
        and then act according to the resulting policy.
        """
        self.theta = theta
        ValueIterationAgent.__init__(self, mdp, discount, iterations)

    def runValueIteration(self):
        "*** YOUR CODE HERE ***"
        # Compute predecessors of all states.

        # map to store predecessors of each state
        predecessors = {} 
        # compute the predecessors for all states
        for state in self.mdp.getStates():
            # handle terminal state
            if self.mdp.isTerminal(state):
                continue
            # iteration throught all actions from that state
            for action in self.mdp.getPossibleActions(state):
                # iteration through all transition states from that action
                for next_state, probability in self.mdp.getTransitionStatesAndProbs(state, action):
                    if next_state in predecessors:
                        predecessors[next_state].add(state)
                    else:
                        predecessors[next_state] = {state}
        
        # priority queue to store the states and their priority
        p_queue = util.PriorityQueue() 
        # for all state that are not terminal, get the q value 
        for state in self.mdp.getStates():
            if not self.mdp.isTerminal(state):
                current_value = self.values[state]
                max_q_value = max([self.computeQValueFromValues(state, action) for action in self.mdp.getPossibleActions(state)])
                diff = abs(current_value - max_q_value)
                p_queue.update(state, -diff)

        for i in range(self.iterations):
            # If the priority queue is empty, then terminate.
            if p_queue.isEmpty():
                break
            # Pop a state s off the priority queue.
            state = p_queue.pop()
            # Update the value of s (if it is not a terminal state) in self.values.
            if not self.mdp.isTerminal(state):
                self.values[state] = max([self.computeQValueFromValues(state, action) for action in self.mdp.getPossibleActions(state)])
            # For each predecessor p of s, do:
            for p in predecessors[state]:
                # Find the absolute value of the difference
                diff = abs(self.values[p] - max([self.computeQValueFromValues(p, action) for action in self.mdp.getPossibleActions(p)]))
                # If diff > theta, push p into the priority queue with priority -diff 
                p_queue.update(p, -diff) if diff > self.theta else None