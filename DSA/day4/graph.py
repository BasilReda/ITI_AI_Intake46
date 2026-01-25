class graph:
    def __init__(self):
        self.adj_list = dict()
    
    def __repr__(self):
        graph_repr = ""
        for node, edges in self.adj_list.items():
            graph_repr += f"{node}->{edges}\n"
        return graph_repr
    
    def add_node(self, node):
        if node not in self.adj_list:
            self.adj_list[node] = set()
        else:
            raise ValueError("Node already exists")
    
    def add_edge(self, from_node, to_node):
        if from_node not in self.adj_list:
            self.add_node(from_node)
        
        if to_node not in self.adj_list:
            self.add_node(to_node)
        
        self.adj_list[from_node].add(to_node)
    
    def bfs_trav(self, start_node):
        visited = set()
        queue = [start_node]
        trav_order = []

        while queue:
            node = queue.pop(0) 
            if node not in visited:
                visited.add(node)
                trav_order.append(node)
                neighbors = self.adj_list.get(node, [])
                for neighbor in neighbors:
                    if neighbor not in visited:
                        queue.append(neighbor)
        return trav_order
            

    def dfs_trav(self, start_node):
        visited = set()
        stack = [start_node]
        trav_order = []

        while stack:
            node = stack.pop()
            if node not in visited:
                visited.add(node)
                trav_order.append(node)
                neighbors = self.adj_list.get(node, [])
                for neighbor in sorted(neighbors, reverse=True):
                    if neighbor not in visited:
                        stack.append(neighbor)
        return trav_order

    def dfs_recursive(self, start_node, visited=None, traversal_order=None):
        if visited is None:
            visited = set()
        if traversal_order is None:
            traversal_order = []
        
        visited.add(start_node)
        traversal_order.append(start_node)
        
        for neighbor in self.adj_list[start_node]:
            if neighbor not in visited:
                self.dfs_recursive(neighbor, visited, traversal_order)
        
        return traversal_order
    
    def bfs_recursive(self, start_node, visited=None, queue=None, traversal_order=None):
        if visited is None:
            visited = set()
        if queue is None:
            queue = []
        if traversal_order is None:
            traversal_order = []
        
        visited.add(start_node)
        traversal_order.append(start_node)
        
        for neighbor in self.adj_list[start_node]:
            if neighbor not in visited and neighbor not in queue:
                queue.append(neighbor)
        
        if queue:
            next_node = queue.pop(0)
            return self.bfs_recursive(next_node, visited, queue, traversal_order)
        
        return traversal_order

grph = graph()
grph.add_node(1)
grph.add_node(2)
grph.add_edge(1, 2)
grph.add_edge(2, 1)
grph.add_edge(5, 2)
grph.add_edge(2, 5)
grph.add_edge(5, 10)
grph.add_edge(10, 5)
grph.add_edge(5, 1)
grph.add_edge(1, 5)
print(grph)
bfs_que = grph.bfs_trav(1)
dfs_stack = grph.dfs_trav(1)
bfs_rec = grph.bfs_recursive(1)
dfs_rec = grph.dfs_recursive(1)
print(f"BFS Que:{bfs_que}\nDFS Stack:{dfs_stack}\nBFS Rec:{bfs_rec}\nDFS Rec:{dfs_rec}")