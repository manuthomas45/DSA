from collections import deque
class Graph:
    def __init__(self,edges):
        self.edges=edges
        self.graph_dic={}
        for start,end in self.edges:
            if start in self.graph_dic:
                self.graph_dic[start].append(end)
            else:
                self.graph_dic[start]=[end]
        # print(self.graph_dic)
    def get_path(self,start,end,path=[]):
        path=path+[start]
        if start==end:
            return [path]
        if start not in self.graph_dic:
            return []
        paths=[]
        for node in self.graph_dic[start]:
            if node not in path:
                # print(node)
                new_paths=self.get_path(node,end,path)
                # print(new_paths)
                if new_paths:
                    paths.extend(new_paths)
        return paths
    def get_shortest_path(self,start,end,path=[]):
        path=path+[start]
        if start==end:
            return path
        if start not in self.graph_dic:
            return []
        shortest_path=None
        for node in self.graph_dic[start]:
            if node not in path:
                sp=self.get_shortest_path(node,end,path)
                if sp:
                    if shortest_path is None or len(sp)<len(shortest_path):
                        shortest_path=sp
        return shortest_path
    def add_vertex_and_edge(self,start,end):
        if start not in self.graph_dic:
            self.graph_dic[start]=[]
        if end not in self.graph_dic:
            self.graph_dic[end]=[]
        self.graph_dic[start].append(end)
    def dfs(self,start,visited=None):
        if visited is None:
            visited=set()
        visited.add(start)
        print(start, end=' ')
        for neighbor in self.graph_dic.get(start,[]):
            if neighbor not in visited:
                self.dfs(neighbor,visited)
    def bfs(self,start):
        visited=set()
        queue=deque([start])
        visited.add(start)
        while queue:
            current=queue.popleft()
            print(current,end='')
            for neighbour in self.graph_dic.get(current,[]):
                if neighbour not in visited:
                    visited.add(neighbour)
                    queue.append(neighbour)
    def is_path(self,start,end,visited=None):
        if visited is None:
            visited=set()
        if start==end:
            return True
        if start not in self.graph_dic:
            return False
        visited.add(start)
        for node in self.graph_dic[start]:
            if node not in visited:
                if self.is_path(node,end,visited):
                    return True 
        return False
    def delete_node(self, node):
        # Remove the node from the graph_dict
        if node in self.graph_dict:
            del self.graph_dict[node]

        # Remove the node from adjacency lists of other nodes
        for key in self.graph_dict.keys():
            if node in self.graph_dict[key]:
                self.graph_dict[key].remove(node)
routes=[("Mumbai","Paris"),
            ("Mumbai","Dubai"),
            ("Paris","Dubai"),
            ("Paris","New York"),
            ("Dubai","New York"),
            ("New York","Toronto")
            ]
graph=Graph(routes)
print(graph.get_path("Mumbai","Toronto"))
# print(graph.get_shortest_path("Mumbai","Toronto"))
# graph.add_vertex_and_edge("kochi","calicut")
# graph.add_vertex_and_edge("kochi","Mumbai")
# print(graph.graph_dic)
# graph.dfs("kochi")
# print(graph.is_path("calicut","Mumbai"))
# graph_ = {
#     "A": ["B", "C"],
#     "B": ["C", "D"],
#     "C": ["D"],
#     "D": []
# }#self.graph_dic=graph_