"""
  https://codereview.stackexchange.com/questions/181698/new-way-of-doing-the-a-algorithm
  I am still working on this to optimizd as suggested and I will post updated code once I am done
 
  note : My first git repository. Please excuse flaws and lack of adherence to standards.
  I will get there eventually.
 """

import networkx as nx
import pickle

class Map:
    def __init__(self, G):
        self._graph = G
        self.intersections = nx.get_node_attributes(G, "pos")
        self.roads = [list(G[node]) for node in G.nodes()]

def load_map(name):
	with open(name, 'rb') as f:
		G = pickle.load(f)
	return Map(G)

        
def shortest_path(M, start, goal):
    explored = set([start])
    frontier = dict([(i,[start]) for i in M.roads[start]]) if start!=goal else {start:[]}
    while frontier:
        explore = g_h(frontier,goal,M)
        for i in [i for i in M.roads[explore] if i not in frontier.keys()|explored]:
            frontier[i]=frontier[explore]+[explore]
        if explore==goal:return frontier[explore]+[explore]#break when goal is explored.               
        explored.add(explore)
        del frontier[explore]#once explored remove it from frontier. 
        
def g_h(frontier,goal,M): 
    g_h = dict([(len(frontier[node])+hueristic(node,goal,M),node) for node in frontier])
    return g_h[min(g_h)]

def hueristic(p1,p2,M):#use a reference point for better h, reference is vertex 0
    vt = M.intersections
    return ((vt[p1][0]-vt[0][0])**2+(vt[p1][1]-vt[0][1])**2)-((vt[p2][0]-vt[0][0])**2+(vt[p2][1]-vt[0][1])**2)


if __name__ == '__main__':
    maps = load_map('map.pickle')
    starts = ?? #start node
    goal = ?? #goal node.
    print(shortest_path(maps, start, goal))
    
