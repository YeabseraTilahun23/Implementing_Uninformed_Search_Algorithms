# This is an ideal (not true) representation of how one can travel from city to city in Addis.
# selected this approach instead of letters to further enhance the learning experience
from collections import deque
import heapq


graph = {
'Piasa': ['4 kilo', 'Megenagna', 'Merkato', 'Torhayloch', 'Abinet'],
'4 kilo': ['Piasa', '5 kilo',],
'5 kilo': ['4 kilo', 'Bole'],
'Bole': ['5 kilo', 'Megenagna', 'Kazanchis'],
'Megenagna': ['Piasa', 'Bole', 'Mexico', 'Koye'],
'Merkato': ['Piasa', 'Autobistera'],
'Kazanchis': ['Bole'],
'Autobistera': ['Merkato'],
'Mexico': ['Bole', 'Megenagna', '4 kilo'],
'Torhayloch': ['Mexico'],
'Abinet': ['Mexico', 'Merkato', 'Piasa'],
'Koye': ['Megenagna'],
'Mesalemya': ['Merkato']

}



# Implementing Breadth-First Search (BFS)
def bfs(graph, start, goal):
    explored_cities = set()
    paths_queue = deque([[start]])
    node_count = 0

    while paths_queue:
        current_path = paths_queue.popleft()
        current_node = current_path[-1]

        if current_node in explored_cities:
            continue

        explored_cities.add(current_node)
        node_count += 1
        if current_node == goal:
            print("BFS nodes expanded:", node_count)
            return current_path
        
        for neighbor_node in graph.get(current_node, []):
            new_path = list(current_path)
            new_path.append(neighbor_node)
            paths_queue.append(new_path)

    print("BFS nodes expanded:", node_count)
    return None
    



# Implementing Depth-First Search
def dfs(graph, start, goal, explored_cities=None, node_count = None):
    if explored_cities is None:
        explored_cities = set()
        node_count = [0]

    explored_cities.add(start)
    node_count[0] += 1
    if start == goal:
        print ("DFS nodes expanded:", node_count[0])
        return [start]
    

    for neighbor_node in graph.get(start, []):
        if neighbor_node not in explored_cities:
            current_path = dfs(graph, neighbor_node, goal, explored_cities, node_count)
            if current_path:
                return [start] + current_path
            
    return None



# Implementing Uniform-Cost Search
def ucs(graph, start, goal):
    explored_cities = set()
    paths_queue = [(0, [start])]
    node_count = 0

    while paths_queue:
        current_cost, current_path = heapq.heappop(paths_queue)
        current_node = current_path[-1]

        if current_node in explored_cities:
            continue

        explored_cities.add(current_node)
        if current_node == goal:
            print("UCS nodes expanded:", node_count)
            return current_path
        
        for neighbor_node in graph.get(current_node, []):
            extended_path = list(current_path)
            extended_path.append(neighbor_node)
            heapq.heappush(paths_queue, (current_cost + 1, extended_path))

    print("UCS nodes expanded:", node_count)
    return None



# Implementing Iterative Deepening Depth-First Search
def iddfs(graph, start, goal):
    if start not in graph or goal not in graph:
        return None

    def depth_limited_search(current_node, goal, limit, explored_cities, node_count):
        if current_node == goal:
            return [current_node]
        if limit <= 0:
            return None
        
        explored_cities.add(current_node)
        node_count[0] += 1
        for neighbor_node in graph.get(current_node, []):
            if neighbor_node not in explored_cities:
                current_path = depth_limited_search(neighbor_node, goal, limit - 1, explored_cities, node_count)
                if current_path: 
                    return [current_node] + current_path
        return None
    
    node_count = [0]
    for depth in range(len(graph)):
        explored_cities = set()
        current_path = depth_limited_search(start, goal, depth, explored_cities, node_count)  
        if current_path:
            print("IDDFS nodes expanded:", node_count[0])
            return current_path
        
    print("IDDFS nodes expanded:", node_count[0])
    return None




# Travel selection:

print("Welcome to Addis.")
print("From where are you starting your journey? ")
print(", ".join(graph.keys()))

start = input("\nYour strating place is: ")
print("Where is you destination? ")
print(", ".join(graph.keys()))
goal = input("Your destination is: ")


print("\nBFS Path:", bfs(graph, start, goal))
print("DFS Path:", dfs(graph, start, goal))
print("UCS Path:", ucs(graph, start, goal))
print("IDDFS Path:", iddfs(graph, start, goal))