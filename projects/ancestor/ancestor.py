# import sys
# sys.path.append('../graph')
from graph import Graph


# return furthest ancestor
# data is list of (parent, child) pairs - tuples
# if more than one at "earliest", return lowest numeric ID
# if input has no parents, return -1


def earliest_ancestor(ancestors, starting_node):
    # initialize graph
    g = Graph()

    # index 0 is parent index 1 is child
    # parents are tuples
    # create vertex for each child and neighbors will be parents

    for i in ancestors:
        # add verts to graph
        g.add_vertex(i[0]) # parent
        g.add_vertex(i[1]) # child
        
    for i in range(len(ancestors)):
        # create edge pointing child to parent
        g.add_edge(ancestors[i][1], ancestors[i][0])