from collections import deque
class Graph:
    def __init__(self,edges):
        self.edges=edges
        self.graph_dict={}
        for start,end in self.edges:
            if start in self.graph_dict:
                self.graph_dict[start].append(end)
            else:
                self.graph_dict[start]=[end]
        # print("Graph dict:",self.graph_dict)
    def get_path(self,start,end,path=[]):
        path=path+[start]
        if start==end:
            return [path]
        if start not in self.graph_dict:
            return []
        paths=[]
        for node in self.graph_dict[start]:

            if node not in path:
                new_paths=self.get_path(node,end,path)
                print(new_paths)
                for p in new_paths:
                    paths.append(p)
        return paths
    def get_shortest_path(self,start,end,path=[]):
        path=path+[start]
        if start==end:
            return path

        if start not in self.graph_dict:
            return None
        shortest_path=None
        for node in self.graph_dict[start]:
            if node not in path:
                sp=self.get_shortest_path(node,end,path)
                if sp:
                    if shortest_path is None or len(sp)<len(shortest_path):
                        shortest_path=sp
        return shortest_path
    def add_vertex_and_edge(self, start, end):
        # Add start vertex if it doesn't exist
        if start not in self.graph_dict:
            self.graph_dict[start] = []
        # Add end vertex if it doesn't exist
        if end not in self.graph_dict:
            self.graph_dict[end] = []
        # Add the edge
        self.graph_dict[start].append(end)
    def dfs(self, start, visited=None):
        if visited is None:
            visited = set()
        visited.add(start)
        print(start, end=" ")  # Process the node
        for neighbor in self.graph_dict.get(start, []):
            if neighbor not in visited:
                self.dfs(neighbor, visited)
    def bfs(self, start):
        visited = set()
        queue = deque([start])
        visited.add(start)

        while queue:
            current = queue.popleft()
            print(current, end=" ")  # Process the node
            for neighbor in self.graph_dict.get(current, []):
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
    def has_path(self, start, end, visited=None):
        if visited is None:
            visited = set()
        if start == end:
            return True
        if start not in self.graph_dic:
            return False
        visited.add(start)
        for node in self.graph_dic[start]:
            if node not in visited:
                if self.has_path(node, end, visited):
                    return True
        return False

    
if __name__=="__main__":
    routes=[("Mumbai","Paris"),
            ("Mumbai","Dubai"),
            ("Paris","Dubai"),
            ("Paris","New York"),
            ("Dubai","New York"),
            ("New York","Toronto")
            ]
    rounter_graph=Graph(routes)
    start="Paris"
    end="New York"
    # print(f"Path between {start} and {end}:",rounter_graph.get_path(start,end))
    # print(f"shortest Path between {start} and {end}:",rounter_graph.get_shortest_path(start,end))
    # rounter_graph.add_vertex_and_edge("kochi","calicut")
    # rounter_graph.dfs("Mumbai")
    rounter_graph.bfs("Mumbai")
    {'A': {'C', 'B'}, 'B': {'A', 'E', 'D'}, 'C': {'F', 'A'}, 'D': {'B'}, 'E': {'F', 'B'}, 'F': {'C', 'E'}}