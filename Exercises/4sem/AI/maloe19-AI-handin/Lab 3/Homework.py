class Node:  # Node has only PARENT_NODE, STATE, DEPTH
    def __init__(self, state, parent=None, depth=0):
        self.STATE = state
        self.PARENT_NODE = parent
        self.DEPTH = depth

    def path(self):  # Create a list of nodes from the root to this node.
        current_node = self
        path = [self]
        while current_node.PARENT_NODE:  # while current node has parent
            current_node = current_node.PARENT_NODE  # make parent the current node
            path.append(current_node)   # add current node to path
        return path

    def display(self):
        print(self)

    def __repr__(self):
        return 'State: ' + str(self.STATE) + ' - Depth: ' + str(self.DEPTH)


'''
Search the tree for the goal state and return path from initial state to goal state
'''
def TREE_SEARCH():
    fringe = []
    initial_node = Node(INITIAL_STATE)
    fringe = INSERT(initial_node, fringe)
    while fringe is not None:
        node = REMOVE_FIRST(fringe)
        if node.STATE == GOAL_STATE:
            return node.path()
        children = EXPAND(node)
        fringe = INSERT_ALL(children, fringe)
        print("fringe: {}".format(fringe))


'''
Expands node and gets the successors (children) of that node.
Return list of the successor nodes.
'''
def EXPAND(node):
    successors = []
    children = successor_fn(node.STATE)
    for child in children:
        s = Node(node)  # create node for each in state list
        s.STATE = child  # e.g. result = 'F' then 'G' from list ['F', 'G']
        s.PARENT_NODE = node
        s.DEPTH = node.DEPTH + 1
        successors = INSERT(s, successors)
    return successors


'''
Insert node in to the queue (fringe).
'''
def INSERT(node, queue):
    #queue.insert(0, node)                               ####GBFS-greedy best first search  
    queue.append(node)                          #A*-search/a star search
    return queue
'''
Insert list of nodes into the fringe
'''
def INSERT_ALL(list, queue):
    for node in list:
        INSERT(node,queue)
    #for i in index(len(list)):
        #queue.insert(i, list[i])                            
    return queue

'''
Removes and returns the first element from fringe
'''
def REMOVE_FIRST(queue):
    if len(queue) !=0:
        return queue.pop(0)  

def LOCAL_COST(cost):
    for cost in COST:
        new_cost = COST[cost]
    return new_cost

def REMOVE_LOCAL_BEST(current_cost):
    list = []
    i = current_cost
    best_node = LOCAL_COST(COST[i])
    list.append(LOCAL_COST)
    list.remove(best_node)
    #return 0                                    

'''
Successor function, mapping the nodes to its successors
'''
def successor_fn(state):  # Lookup list of successor states
    return STATE_SPACE[state]  # successor_fn( 'C' ) returns ['F', 'G']

INITIAL_STATE = ('A', 'Dirty', 'Dirty')
GOAL_STATE = ('A', 'Clean', 'Clean') 
STATE_SPACE = {
               ('A', 'Dirty', 'Dirty'): [('A', 'Clean', 'Dirty'), ('A', 'Dirty', 'Dirty'), ('B', 'Dirty', 'Dirty')],  
               ('B', 'Dirty', 'Dirty'): [('B', 'Dirty', 'Clean'), ('A', 'Dirty', 'Dirty'), ('B', 'Dirty', 'Dirty')],   
               ('A', 'Clean', 'Dirty'): [('A', 'Clean', 'Dirty'), ('A', 'Clean', 'Dirty'), ('B', 'Clean', 'Dirty')], 
               ('B', 'Clean', 'Dirty'): [('B', 'Clean', 'Clean'), ('A', 'Clean', 'Dirty'), ('B', 'Clean', 'Dirty')], 
               ('A', 'Dirty', 'Clean'): [('A', 'Clean', 'Clean'), ('A', 'Dirty', 'Clean'), ('B', 'Dirty', 'Clean')],
               ('B', 'Dirty', 'Clean'): [('B', 'Dirty', 'Clean'), ('A', 'Dirty', 'Clean'), ('B', 'Dirty', 'Clean')],
               ('A', 'Clean', 'Clean'): [('A', 'Clean', 'Clean'), ('A', 'Clean', 'Clean'), ('B', 'Clean', 'Clean')],
               ('B', 'Clean', 'Clean'): [('B', 'Clean', 'Clean'), ('A', 'Clean', 'Clean'), ('B', 'Clean', 'Clean')]
               }

COST = { 
    'ADD_ACD' : 6,
    'ADD_ADD' : 0,
    'ADD_BDD' : 6,

    'BDD_BDC' : 10,
    'BDD_ADD' : 8,
    'BDD_BDD' : 0,

    'ACD_ACD' : 0,
    'ACD_ACD' : 0,
    'ACD_BCD' : 3,

    'BCD_BCC' : 6,
    'BCD_ACD' : 4,
    'BCD_BCD' : 0,

    'ADC_ACC' : 0,
    'ADC_ADC' : 0,
    'ADC_BDC' : 5,

    'BDC_BDC' : 0,
    'BDC_ADC' : 4,
    'BDC_BDC' : 0,

    'ACC_ACC' : 0,
    'ACC_ACC' : 0,
    'ACC_BCC' : 6,

    'BCC_BCC' : 0,
    'BCC_ACC' : 8,
    'BCC_BCC' : 0,
    }    


'''
Run tree search and display the nodes in the path to goal node
'''
def run():
    path = TREE_SEARCH()
    print('Solution path:')
    for node in path:
        node.display()


if __name__ == '__main__':
    run()
