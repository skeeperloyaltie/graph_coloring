# Can you color an undirected graph with num_colors so that every two connected nodes have
# different color?
# Implement function
# def solve(
#   adj_lists: 'List[List[int]]',
#   num_colors: int,
#   ) -> List[int]:
# returning colors (ints from [0; num_colors)) of nodes or and empty list if no coloring is possible.
# You can iterate adj_lists like this:
# for node, adj_nodes in enumerate(adj_lists):
#       for adj_node in adj_nodes:
# Graph sizes are growing from 4 to 1000. Time limit is 1 sec.
#
# Example:
# adj_lists = [[1, 2], [0, 3], [0, 3], [1, 2]]
# num_colors = 3
# solve(adj_lists, num_colors) == [1, 2, 0]
#
# adj_lists = [[1, 2, 3], [0, 2], [0, 1, 3], [0, 2]]
# num_colors = 3
# solve(adj_lists, num_colors) == []

import random 
def solve(adj_lists, num_colors):
    colors = [0 for _ in range(len(adj_lists))]
    for node, adj_nodes in enumerate(adj_lists):
        for adj_node in adj_nodes:
            if colors[node] == colors[adj_node]:
                return []
    for node, adj_nodes in enumerate(adj_lists):
        for adj_node in adj_nodes:
            if colors[node] != colors[adj_node]:
                colors[node] = colors[adj_node]
    return colors

def random_test():
    adj_lists = [[random.randint(0, 50) for _ in range(random.randint(0, 50))] for _ in range(random.randint(0, 50))]
    num_colors = random.randint(1, 50)
    # if test is successful print the number of tests passed
    solve(adj_lists, num_colors) == []
    print("Successful tests: ")
    print(adj_lists,  num_colors)
    print(solve(adj_lists, num_colors))
  
        
if __name__ == '__main__':
    random_test()   
