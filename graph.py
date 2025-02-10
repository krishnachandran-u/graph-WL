class Graph:
    def __init__(self, vertices):
        self.vertices: list[int] = vertices
        self.adj_list: dict[int, list[int]] = {vertex: [] for vertex in vertices}

    def add_edge(self, u, v) -> None:
        if v not in self.adj_list[u] and u not in self.adj_list[v]:
            self.adj_list[u].append(v)
            self.adj_list[v].append(u)
        else:
            print(f'Edge {u} - {v} already exists')

    def remove_edge(self, u, v) -> None:
        if v in self.adj_list[u] and u in self.adj_list[v]:
            self.adj_list[u].remove(v)
            self.adj_list[v].remove(u)
        else:
            print(f'No edge between {u} and {v}')

    def get_adj_matrix(self):
        adj_matrix: list[list[int]] = [
            [0 for _ in range(len(self.vertices))]
            for _ in range(len(self.vertices))
        ]
        for u in self.vertices:
            for v in self.adj_list[u]:
                adj_matrix[u][v] = 1

    def __str__(self):
        return str(self.adj_list)