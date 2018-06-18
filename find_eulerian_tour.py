# Find Eulerian Tour
#
# Write a function that takes in a graph
# represented as a list of tuples
# and return a list of nodes that
# you would follow on an Eulerian Tour
#
# For example, if the input graph was
# [(1, 2), (2, 3), (3, 1)]
# A possible Eulerian tour would be [1, 2, 3, 1]

def find_eulerian_tour(graph):
    print("-------------------------------------------")
    print("Graph: " + str(graph))
    tour = []
    traversed = []
    first_Node = graph[0][0]
    degrees = {}
    max_degree = 0
    for path in graph:
        a,b = path
        degrees[a] = degrees.get(a,0) + 1
        if degrees[a] >= max_degree:
            max_degree = degrees[a]
            first_node = a
        degrees[b] = degrees.get(b,0) + 1
        if degrees[b] >= max_degree:
            max_degree = degrees[b]
            first_node = b
    
    tour.append(first_node)
    degrees[first_node] = degrees[first_node]-1

    while len(graph) > 0:
        found_next = False
        next_node = None
        max_degree = 0
        next_path = None
        for path in graph:
            a,b = path
            if a == tour[-1]:
                if degrees[b] >= max_degree:
                    next_node = b
                    max_degree = degrees[b]
                    next_path = path
            if b == tour[-1]:
                if degrees[a] >= max_degree:
                    next_node = a
                    max_degree = degrees[a]
                    next_path = path

        if next_node is not None:
            degrees[tour[-1]] = degrees[tour[-1]]-1
            tour.append(next_node)
            graph.remove(next_path)
            found_next = True
            degrees[next_node] = degrees[next_node]-1
        
        if not found_next:
            print("Few were left out: " + str(graph))
            return tour
    print("-------------------------------------------")
    return tour

graph = [(1, 2), (2, 5), (3, 4), (5, 3), (4, 1)]
print(find_eulerian_tour(graph))

graph = [(1, 2), (2, 5), (2, 5), (3, 4), (5, 3), (4, 1)]
print(find_eulerian_tour(graph))

graph = [(1, 3), (3, 5), (3, 4), (5, 3), (4, 1)]
print(find_eulerian_tour(graph))

graph = [(1, 3), (3, 5), (3, 4), (4, 1), (9,7)]
print(find_eulerian_tour(graph))

graph = [(1, 2), (2, 3), (3, 1)]
print(find_eulerian_tour(graph))

graph = [(0, 1), (1, 5), (1, 7), (4, 5),
(4, 8), (1, 6), (3, 7), (5, 9),
(2, 4), (0, 4), (2, 5), (3, 6), (8, 9)]
print(find_eulerian_tour(graph))

graph = [(1, 13), (1, 6), (6, 11), (3, 13),
(8, 13), (0, 6), (8, 9),(5, 9), (2, 6), (6, 10), (7, 9),
(1, 12), (4, 12), (5, 14), (0, 1),  (2, 3), (4, 11), (6, 9),
(7, 14),  (10, 13)]
print(find_eulerian_tour(graph))

graph = [ (8, 18), (16, 17), (18, 19),(8, 16),
(3, 17), (13, 17), (5, 13),(3, 4), (0, 18), (3, 14), (11, 14),
(1, 8), (1, 9), (4, 12), (2, 19),(1, 10), (7, 9), (13, 15),
(6, 12), (0, 1), (2, 11), (3, 18), (5, 6), (7, 15), (8, 13), (10, 17)]
print(find_eulerian_tour(graph))
