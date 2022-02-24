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

    node = []
    path = []
    ##empty path + visited state
    frontier = util.Stack()
    ##stack for frontier
    frontier.push((problem.getStartState(),path))

    while not frontier.isEmpty():
        state, path = frontier.pop()
        ##pop state and path while frontier has not entirely been visites

        if problem.isGoalState(state):
            return path

        ##if state is goal, return the path arr

        elif state not in node:
            node.append(state)
            ##if current state not in visited nodes, add curr state to node
            for incstate, singlepath, cost in problem.getSuccessors(state):
                if incstate not in node:
                    frontier.push((incstate, path + [singlepath]))
                    ##if the next state is not in visited nodes, pushes next state to frontier alongside the updated path

    util.raiseNotDefined()



def breadthFirstSearch(problem):
    node = []
    path = []
    ##empty path + visited state
    frontier = util.Queue()
    ##queue for frontier,
    frontier.push((problem.getStartState(), path))

    while not frontier.isEmpty():
        state, path = frontier.pop()
        ##pop state and path while frontier has not entirely been visites

        if problem.isGoalState(state):
            return path

        ##if state is goal, return the path arr

        elif state not in node:
            node.append(state)
            ##if current state not in visited nodes, add curr state to node
            for incstate, singlepath, cost in problem.getSuccessors(state):
                if incstate not in node:
                    frontier.push((incstate, path + [singlepath]))
                    ##if the next state is not in visited nodes, pushes next state to frontier alongside the updated path

    util.raiseNotDefined()


def uniformCostSearch(problem):
    node1 = problem.getStartState()
    if problem.isGoalState(node1):
        return []

    ## if problem starts at goal start, cost is effectively 0, meaning a blank arr is returned.
    frontier = util.PriorityQueue()
    node = []
    frontier.push((node1, [], 0), 0)

    ##elif problem does not start at goal state, frontier pushes (starting node, path, cost, priority)

    while not frontier.isEmpty():

        state, path, cost1 = frontier.pop()

        if state not in node:
            node.append(state)

            ##if curr state not in visited nodes, add curr state.

            if problem.isGoalState(state):
                return path

            ##is curr state is goal, return path.

            for incstate, singlepath, cost2 in problem.getSuccessors(state):
               frontier.push((incstate, path + [singlepath], cost1 + cost2), cost1 + cost2)

                ##pushes nect state, total path, total cost, then priority onto the pq.

    util.raiseNotDefined()

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""

    node1 = problem.getStartState()
    if problem.isGoalState(node1):
        return []

    frontier = util.PriorityQueue()
    node = []
    frontier.push((node1, [], 0), 0)

    ##elif problem does not start at goal state, frontier pushes (starting node, path, cost, priority)

    while not frontier.isEmpty():

        state, path, cost1 = frontier.pop()

        if state not in node:
            node.append(state)

            ##if curr state not in visited nodes, add curr state.

            if problem.isGoalState(state):
                return path

            ##is curr state is goal, return path.

            for incstate, singlepath, cost2 in problem.getSuccessors(state):
                frontier.push((incstate, path + [singlepath], cost1 + cost2),
                              cost1 + cost2 + heuristic(incstate, problem))
                ##pushes next state, total path, total cost, then priority heuristoc onto the pq.

    util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
