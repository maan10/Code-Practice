def a_Star_Algorithm(initial_node, goal_node):

        open_set = set(initial_node) 
        closed_set = set()
        g = {} #store distance from starting node
        parents = {}# parents contains an adjacency map of all nodes
        #ditance of starting node from itself is zero
        g[initial_node] = 0
        parents[initial_node] = initial_node     #so initial_node is set to its own parent node
        while len(open_set) > 0:
            n = None
            #node with lowest f() is found
            for v in open_set:
                if n == None or g[v] + heuristic(v) < g[n] + heuristic(n):
                    n = v
            if n == goal_node or Graph_nodes[n] == None:
                pass
            else:
                for (m, weight) in get_neighbors(n):
                    
                    if m not in open_set and m not in closed_set:
                        open_set.add(m)
                        parents[m] = n
                        g[m] = g[n] + weight
                    #for each node m,compare its distance from start i.e g(m) to the
                    #from start through n node
                    else:
                        if g[m] > g[n] + weight:
                            #update g(m)
                            g[m] = g[n] + weight
                            #change parent of m to n
                            parents[m] = n
                            #if m in closed set,remove and add to open
                            if m in closed_set:
                                closed_set.remove(m)
                                open_set.add(m)
            if n == None:
                print('Path not exist!')
                return None
            # if the current node is the goal_node
            # then we begin reconstructin the path from it to the initial_node
            if n == goal_node:
                path = []
                while parents[n] != n:
                    path.append(n)
                    n = parents[n]
                path.append(initial_node)
                path.reverse()
                print('Path found: {}'.format(path))
                return path
            # remove n from the open_list, and add it to closed_list
            # because all of his neighbors were inspected
            open_set.remove(n)
            closed_set.add(n)
        print('Path not exist!')
        return None
#define fuction to return neighbor and its distance
#from the passed node
def get_neighbors(v):
    if v in Graph_nodes:
        return Graph_nodes[v]
    else:
        return None
#for simplicity we ll consider heuristic distances given
#and this function returns heuristic distance for all nodes
def heuristic(n):
        Heuristic_distance = {
            'A': 19,
            'B': 7,
            'C': 86,
            'D': 1,
            'E': 4,
            'G': 0,
            
        }

        return Heuristic_distance[n]

#Describe your graph here  
Graph_nodes = {
    'A': [('B', 2), ('E', 3)],
    'B': [('C', 1),('G', 9)],
    'C': None,
    'D': [('G', 1)], 
    'E': [('D', 6)],
}
a_Star_Algorithm('A', 'G')
