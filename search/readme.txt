---------------------------------------------------------
This assignment is done by Ka Hin Choi, 
and Ronan Dzung Nguyen collaboratively.
---------------------------------------------------------
This README.txt explains our work of each questions
---------------------------------------------------------
Q1:
The function will have a stack called "fringe" that will 
keep track of the actions leading up to the goal, as well 
as a set to keep track of all the visited nodes. The 
function will begin by pushing a tuple of the starting 
node into the fringe, along with an empty list that will 
hold the actions leading up to the goal later on. As long
as there is a node in the fringe, the program will 
continue exploring paths. If the current node being 
examined is not the goal, the code will push it into the 
visited set and move on to its successor, adding the 
action to get from the current node to the successor 
in the process, in order to keep track of the path. 
When the current node is identified as the goal, the 
list that has been keeping track of the actions leading 
up to the current node will be returned.
---------------------------------------------------------
Q2:
The function will have a queue called the "fringe", which 
contains the nodes that will soon be expand upon. A queue 
is used because breadth-first search needs to visit all 
the nodes at a given depth before moving on to the nodes 
at the next depth. To achieve this, the function needs to 
maintain a list of nodes to be visited at the current 
depth, and it needs to visit these nodes in the order in 
which they were discovered. The function starts by pushing 
the start state onto the fringe with an empty list of 
actions. Then, it repeatedly pops a node from the fringe, 
checks if it has been visited before, and adds it to the 
visited list if not. If the current node is the goal 
state, the algorithm returns the list of actions that led 
to that state. Otherwise, the successors of the current 
node are generated and added to the fringe, along with the 
actions that led to them from the current node, which are 
also added to the list of actions. The loop continues 
until the fringe is empty or the goal state is found.
---------------------------------------------------------
Q3:
This function performs a uniform cost search using a 
priority queue as the "fringe" to keep track of nodes with
 the least cost. It starts by pushing the starting state, 
 an empty path, and a cost of 0 onto the fringe. The 
 function repeatedly pops a node, checks if it has been 
 visited before, and adds it to the visited list if not. 
 If the current node is the goal state, the function 
 returns the list of actions that led to that state. 
 Otherwise, the successors of the current node are 
 generated and added to the fringe, along with the actions 
 that led to them. For each successor, the function will 
 also calculates the cost of the path by adding the step 
 cost of the successor to the current cost and uses that 
 as a priority indicator. The loop continues until the 
 fringe is empty or the goal state is found.
---------------------------------------------------------
Q4:
The function maintains a priority queue of nodes to 
explore, with the lowest cost node first. The function 
starts by initializing a priority queue called "fringe" 
and a visited set. It then pushes the start state, an 
empty path, and a cost of zero to the fringe with a 
priority of zero. It then continues to loop until the 
fringe is empty or the goal state is reached. In each 
iteration, it pops the node with the lowest cost from 
the fringe, marks it as visited, checks if it is the 
goal state, and if not, expands its successors and pushes 
them onto the fringe with updated costs based on the current 
path cost and the estimated remaining cost from the 
heuristic function. If the goal state is reached, 
the algorithm returns the path to that node.
---------------------------------------------------------
Q5:
This is an implementation of searchAgent that searches 
all four corners. The state will contain a tuple of the 
"position" and a list that stores the visited corner. When
all four corners are visited, the isGoalState function returns
True. The getSuccessors function search all four directions,
it checks if the direction is legal and are they the corner 
being visited. If not visited, mark as visited and append
to the successors list that will be returned at the end of 
the function.
The key in this question is to realize that Python is 
pass by reference, therefore we need to pass in a copy
of the visited list in order to avoid only visiting one 
corner at the end.
---------------------------------------------------------
Q6:
This is a heuristic function that calculates the heuristic 
value for searching algorithms. It calculates the manhattan
distance of the smallest corner, adding up with the distance
of corner to corner ( except the maximum distance in the list).
This encourage the PacMan to go to the closest food and avoid
the farthest corner.
---------------------------------------------------------
Q7:
This is a heuristic function the calculates the heuristic 
value for searching algorithm, this algorithm return
the farthest mazeDistance to each food that hasn't been
consumed.
The key for this question is discovering the mazeDistance.
---------------------------------------------------------
Q8:
The function starts by initializing a "fringe" that stores 
the nodes to be expanded and a visited set to keep track 
of already visited nodes. The search algorithm used is 
Depth First Search. The method then begins the search by 
adding the starting position and an empty list to the 
fringe. It enters a loop that pops a node from the fringe 
and expands it. The node is added to the visited set to 
avoid revisiting it. If the current node coordinate is 
the same as the coordinate of the first food that it 
expanded to using getFood(), the method returns the path 
that leads up to this current node. Otherwise, the method 
generates the successors of the current node and adds them 
to the fringe if they have not been visited before together 
with the expanded path leading up to the successor.
---------------------------------------------------------