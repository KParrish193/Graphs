"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy

class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        if v1 not in self.vertices:
            self.vertices[v1] = set()

        # add v2 if it's not in self.vertices
        if v2 not in self.vertices:
            self.vertices[v2] = set()

        # add edge to v1
        self.vertices[v1].add(v2)

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        if vertex_id not in self.vertices:
            return None

        return self.vertices[vertex_id]

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
    # Create an empty queue and enqueue the starting vertex ID		
        q = Queue()
        q.enqueue(starting_vertex)

        # Create a Set to store visited vertices
        visited = set()

        # While the queue is not empty...
        while q.size() > 0:
            # Dequeue the first vertex
            v = q.dequeue()

        # If that vertex has not been visited...
            if v not in visited:
                # Visit it
                print(v)
                # Mark it as visited...
                visited.add(v)

                # Then add all of its neighbors to the back of the queue
                for next_vert in self.get_neighbors(v):
                    q.enqueue(next_vert)

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        s = Stack()
        s.push(starting_vertex)

        # Create a Set to store visited vertices
        visited = set()

        # While the stack is not empty...
        while s.size() > 0:
            # pop the first vertex
            v = s.pop()

        # If that vertex has not been visited...
            if v not in visited:
                # Visit it
                print(v)
                # Mark it as visited...
                visited.add(v)

                # Then add all of its neighbors to the back of the queue
                for next_vert in self.get_neighbors(v):
                    s.push(next_vert)


    def dft_recursive(self, starting_vertex, visited=None):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """
        if not visited:
            visited = set()

        if starting_vertex not in visited:
            print(starting_vertex)
            visited.add(starting_vertex)

            for next_vert in self.get_neighbors(starting_vertex):
                self.dft_recursive(next_vert, visited)


    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        # PLAN:
        # Create an empty queue and enqueue A PATH TO the starting vertex ID
        # Create a Set to store visited vertices
        # While the queue is not empty...
            # Dequeue the first PATH
            # Grab the last vertex from the PATH
            # If that vertex has not been visited...
                # CHECK IF IT'S THE TARGET
                    # IF SO, RETURN PATH
                # Mark it as visited...
                # Then add A PATH TO its neighbors to the back of the queue
                    # COPY THE PATH
                    # APPEND THE NEIGHOR TO THE BACK

        # Create an empty queue and enqueue the starting vertex ID		
        q = Queue()
        path = [starting_vertex]
        q.enqueue(path)

        # Create a Set to store visited vertices
        visited = set()

        while q.size() > 0:
            # Dequeue the first vertex
            curr_path = q.dequeue()
            # Grab the last vertex from the PATH
            curr_vert = curr_path[-1]

        # If that vertex has not been visited...
            if curr_vert not in visited:
                # check to see if we've found the node we were looking for
                if curr_vert == destination_vertex:
                    # IF match, RETURN PATH
                    return curr_path
                # not a match keep searching 
                # if not Mark it as visited...
                visited.add(curr_vert)
                # Then add all of its neighbors to the back of the queue
                for nbr_verts in self.get_neighbors(curr_vert):
                    new_path = curr_path + [nbr_verts]
                    q.enqueue(new_path)

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        s = Stack()
        path = [starting_vertex]
        s.push(path)

        # Create a Set to store visited vertices
        visited = set()

        while s.size() > 0:
            # Dequeue the first vertex
            curr_path = s.pop()
            # Grab the last vertex from the PATH
            curr_vert = curr_path[-1]

        # If that vertex has not been visited...
            if curr_vert not in visited:
                # check to see if we've found the node we were looking for
                if curr_vert == destination_vertex:
                    # IF match, RETURN PATH
                    return curr_path
                # not a match keep searching 
                # if not Mark it as visited...
                visited.add(curr_vert)
                # Then add all of its neighbors to the back of the queue
                for nbr_verts in self.get_neighbors(curr_vert):
                    new_path = curr_path + [nbr_verts]
                    s.push(new_path)

    def dfs_recursive(self, starting_vertex, destination_vertex, visited=None, path=None):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        # initialize
        if not visited and not path:
            path = [starting_vertex]
        # Create a Set to store visited vertices
            visited = set()

        # base case to exit, found destination vertex
        if destination_vertex in path:
            return path

        # base case, no path to destination vertex
        if starting_vertex in visited:
            return

        # last element in path list is the vert that hasn't been checked yet
        curr_vert = path[-1]
        visited.add(curr_vert)

        for nbr_verts in self.get_neighbors(curr_vert):
            new_path = path + [nbr_verts]
            visit_next = self.dfs_recursive(nbr_verts, destination_vertex, visited, new_path)
            
            if visit_next is not None: 
                return visit_next

if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    print(graph.vertices)

    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
    graph.bft(1)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    graph.dft(1)
    graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print(graph.dfs(1, 6))
    print(graph.dfs_recursive(1, 6))
