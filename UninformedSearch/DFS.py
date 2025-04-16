class StackFrontier:
    def __init__(self):
        self.frontier = []
    
    def frontier_isempty(self):
        if len(self.frontier) == 0:
            isempty = True
        else:
            isempty = False
        return isempty
    
    def add_to_frontier(self, value):
        self.frontier.append(value)
        return value
    
    def remove_from_frontier(self):
        element = self.frontier.pop(-1)
        return element
    
    def show_frontier(self):
        return self.frontier

   
    
class QueueFrontier(StackFrontier):
    def __init__(self):
        self.frontier = []

    def remove_from_frontier(self):
        element = self.frontier.pop(0)
        return element
        

def uninformed_search(initial_state, goal_state, tree_space, frontier = StackFrontier()):
    frontier = frontier
    frontier.add_to_frontier(initial_state)
    explored_path = []
    cost= 0

    while  not frontier.frontier_isempty():
        current_state = frontier.remove_from_frontier()
        print(f"removed {current_state} from frontier")
        explored_path.append(current_state)

        if current_state == goal_state:
            print('result found ')
            print('the path followed was::=> ', explored_path, 'total cost travelled', cost)
            break
        
        else:
            for i in tree_space.edges.keys():
                # print(current_state, 'current state ')
                for value in i:
                    if current_state in i and value not in explored_path:
                        print(f"added {value} to frontier")
                        frontier.add_to_frontier(value)
                        cost += tree_space.edges[i]

                
            print("explored path", explored_path, cost)




class Tree:
    def __init__(self, root):
        self.root = root
        self.edges = {}
        self.vertices  = []
        self.vertices.append(self.root)


    def add_vertex(self, vertex):
        if vertex not in self.vertices:
            self.vertices.append(vertex)
            #print(self.vertices, 'list of vertices')
        return vertex
    
    def add_edge(self, edge, weight):
        # print(self.edges, edge)
        self.edges[edge] = weight
        return self.edges
    
    def show_tree(self):
        # print(self.vertices, 'vertices')
        # print(self.edges, 'edges')
        self.tree = [self.edges, self.vertices]
        print(self.tree)

sample_tree = Tree('A')
sample_tree.add_vertex('B')
sample_tree.add_edge( ('A', "B"), 3)
sample_tree.add_vertex('C')
sample_tree.add_edge(('A', 'C'), 23 )
sample_tree.add_vertex('D')
sample_tree.add_edge( ('B', "D"), 4)
sample_tree.add_vertex('E')
sample_tree.add_edge(('C', 'E'), 1 )
sample_tree.add_vertex('F')
sample_tree.add_edge( ('C', "F"), 3)
sample_tree.add_vertex('G')
sample_tree.add_edge(('E', 'G'), 2 )
sample_tree.show_tree()


print('using DFS')
uninformed_search('A', "D", sample_tree)
print('==>'*30)
print("using BFS")
uninformed_search('A', 'D', sample_tree, frontier=QueueFrontier())
