def aStarAlgo(start_node, stop_node):
    # Initialize the open set with the start node
    open_set = set([start_node])
   
    # Initialize the closed set, g-costs, and parents dictionary
    closed_set = set()
    g = {start_node: 0}  # g-cost from start node to itself is 0
    parents = {start_node: start_node}  # Start node has no parent, so it points to itself
   
    while open_set:
        # Find the node in open_set with the lowest f() = g() + h()
        n = None
        min_f_value = float('inf')  # Start with an infinitely large value

        for node in open_set:
            f_value = g[node] + heuristic(node)  # Calculate f(n)
            if f_value < min_f_value:
                min_f_value = f_value
                n = node

        # If the goal node is reached, reconstruct and return the path
        if n == stop_node:
            return reconstruct_path(parents, start_node, stop_node)
       
        # Move the current node from open_set to closed_set
        open_set.remove(n)
        closed_set.add(n)
       
        # Process each neighbor of the current node
        for (m, weight) in get_neighbors(n):
            if m in closed_set:
                continue  # Skip neighbors that have already been processed
           
            tentative_g = g[n] + weight  # Calculate tentative g-cost
           
            if m not in open_set:  # New node discovered
                open_set.add(m)
            elif tentative_g >= g[m]:
                continue  # This path is not better
           
            # Update the best known path to the neighbor
            parents[m] = n
            g[m] = tentative_g
   
    # If open_set is empty and no path was found
    print('Path does not exist!')
    return None

def reconstruct_path(parents, start_node, stop_node):
    """Helper function to reconstruct the path from start to goal."""
    path = []
    current_node = stop_node
    while current_node != start_node:
        path.append(current_node)
        current_node = parents[current_node]
    path.append(start_node)
    path.reverse()
    print('Path found: {}'.format(path))
    return path

def get_neighbors(v):
    """Return the neighbors of a node."""
    return Graph_nodes.get(v, [])

def heuristic(n):
    """Heuristic function to estimate the distance from the current node to the goal."""
    H_dist = {
        'A': 11,
        'B': 6,
        'C': 5,
        'D': 7,
        'E': 3,
        'F': 6,
        'G': 5,
        'H': 3,
        'I': 1,
        'J': 0
    }
    return H_dist[n]

# Graph definition
Graph_nodes = {
    'A': [('B', 6), ('F', 3)],
    'B': [('A', 6), ('C', 3), ('D', 2)],
    'C': [('B', 3), ('D', 1), ('E', 5)],
    'D': [('B', 2), ('C', 1), ('E', 8)],
    'E': [('C', 5), ('D', 8), ('I', 5), ('J', 5)],
    'F': [('A', 3), ('G', 1), ('H', 7)],
    'G': [('F', 1), ('I', 3)],
    'H': [('F', 7), ('I', 2)],
    'I': [('E', 5), ('G', 3), ('H', 2), ('J', 3)],
}

aStarAlgo('A', 'J')
