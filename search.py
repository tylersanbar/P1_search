# search.py
# ---------
# This codebase is adapted from UC Berkeley AI. Please see the following information about the license.

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

from sre_parse import expand_template
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
    
    # def dfs(problem, state, path = [], visited = set(), action = "start"):
    #     if(action != "start"): path.append(action)
    #     if problem.isGoalState(state):
    #         return path
    #     visited.add(state)
    #     successors = problem.getSuccessors(state)
    #     for successor in successors:
    #         nextState = successor[0]
    #         nextAction = successor[1]
    #         if nextState not in visited:
    #             result = dfs(problem, nextState, path, visited, nextAction)
    #             if result is not None:
    #                 return result
    #     path.pop()
    #     return None

    # path = dfs(problem,problem.getStartState())
    path = graphSearch("dfs", problem)
    return getActionsFromPath(path)
    util.raiseNotDefined()

def graphSearch(strategy, problem):
    expandedNode = [problem.getStartState(),"start"]
    
    expanded = set()
    if strategy == "dfs":
        frontier = util.Stack()
    elif strategy == "bfs":
        frontier = util.Queue()
    elif strategy == "ucs":
        frontier = util.PriorityQueue()
    elif strategy == "astar":
        frontier = util.PriorityQueueWithFunction()
    args = []
    
    args.append([expandedNode])
    if(strategy == "ucs"): args.append(0)
    frontier.push(*args)
    print("Args are ", *args)
    while(not problem.isGoalState(expandedNode[0]) and frontier):
        
        path = frontier.pop()
        print("Path is", path)
        node = (path[-1])[0]
        print("Node is ",node)
        if problem.isGoalState(node): return path
        if(node not in expanded):
            expanded.add(node)
            neighbours = problem.getSuccessors(node)
            for neighbour in neighbours:
                new_path = list(path)
                new_path.append(neighbour)
                args = []
                args.append(new_path)
                if(strategy == "ucs"): args.append(getTotalPathCost(new_path))
                frontier.push(*args)
    return
def getTotalPathCost(path):
    cost = 0
    for node in path:
        if(node[1] != "start"): cost += node[2]
    return cost
def getActionsFromPath(path):
    actions = []
    for node in path:
        if(node[1] != "start"): actions.append(node[1])
    return actions

def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    """def bfs():
        queue = util.Queue()
        path = []
        visited = set()
        start = problem.getStartState()
        queue.push([[start,"start"]])
        visited.add(start)
        while queue:
            path = queue.pop()
            state = (path[-1])[0]
            if problem.isGoalState(state):
                return path
            successors = problem.getSuccessors(state)
            for successor in successors:
                nextState = successor[0]
                nextAction = successor[1]
                actionState = [nextState,nextAction]
                if nextState not in visited:
                    new_path = list(path)
                    new_path.append(actionState)
                    queue.push(new_path)
                    visited.add(nextState)
    path = bfs()    
    path.pop(0)
    actionPath = []
    for stateAction in path:
        actionPath.append(stateAction[1])
    return actionPath
    """
    path = graphSearch("bfs", problem)
    return getActionsFromPath(path)
    util.raiseNotDefined()
    # Frontier to add successors to
    # front = util.Queue()
    
    # # List of explored nodes
    # visited = []
    
    # # Start state and starting node to be pushed to queue first
    # sState = problem.getStartState()
    # sNode = (sState, [], 0)
    # front.push(sNode)

    # # While the queue is not empty
    # while not front.isEmpty():
    # 	# Make the current state and move actions equal to first node in the queue
    #     currentState, moves, currCost = front.pop()
    #     # Check if this state has been visited if not add it to the visited list
    #     if currentState not in visited:
    #         visited.append(currentState)
            
    #         # Check if we are at goal state, if not create a new node based on each of the successors and push it to the frontier
    #         if problem.isGoalState(currentState):
    #             return moves
    #         else:
    #             potentialSucc = problem.getSuccessors(currentState)
    #             for state, move, cost in potentialSucc:
    #                 tmpMoves = moves + [move]
    #                 tmpCost = currCost + cost
    #                 tmpNode = (state, tmpMoves, tmpCost)
    #                 front.push(tmpNode)
                
    # return moves
    util.raiseNotDefined()
    
def uniformCostSearch(problem):
    # """Search the node of least total cost first."""
    # "*** YOUR CODE HERE ***"
    # # Frontier to add successors to
    # front = util.PriorityQueue()
    
    # # List of explored nodes storing the node location and cost
    # visited = {}
    
    # # Start state and starting node to be pushed to queue first
    # sState = problem.getStartState()
    # sNode = (sState, [], 0)
    # front.push(sNode, 0)
    # # While the queue is not empty
    # while not front.isEmpty():
    # 	# Make the current state and move actions equal to the lowest cost node in the frontier
    #     currentState, moves, currCost = front.pop()
    #     # Check if this state has been visited if not add it to the visited with its cost
    #     if currentState not in visited or currCost < visited[currentState] :
    #         visited[currentState] = currCost
            
    #         # Check if we are at goal state, if not create a new node based on each of the successors and update 	       the total cost to reach that state
    #         if problem.isGoalState(currentState):
    #             return moves
    #         else:
    #             potentialSucc = problem.getSuccessors(currentState)
    #             for state, move, cost in potentialSucc:
    #                 tmpMoves = moves + [move]
    #                 tmpCost = currCost + cost
    #                 tmpNode = (state, tmpMoves, tmpCost)
    #                 front.update(tmpNode,tmpCost)
                
    # return moves
    path = graphSearch("ucs", problem)
    return getActionsFromPath(path)
    util.raiseNotDefined()

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
