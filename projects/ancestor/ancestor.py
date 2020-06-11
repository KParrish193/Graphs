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
        
        # get levels of each node from starting_node
    level = g.get_levels(starting_node)

    # loop through level dictionary and key with most value is the farthes node
    node_list = []
    # use this to check if nodes are on same level
    farthest = 0

    # get node with most value(farthest)
    for key in level:

        if level[key] > farthest:
            farthest = level[key]

    # check each value of key in level
    # if level[key] matches the farthest, append to node_list
    for key in level:
        if level[key] == farthest and level[key] != 0:
            node_list.append(key)

    # if node list contains more more than one node, compare and grab the lowest value
    if len(node_list) >= 1:
        return node_list[0]
    else:
        return -1