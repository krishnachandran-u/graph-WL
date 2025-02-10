from os import getcwd
import graphviz
import json
class Graph:
    """ use consecutive natural numbers starting from 0 as vertex labels"""

    def __init__(self, filename: str, name: str):
        try:
            with open(f'../data/{filename}') as f:
                data: dict = json.load(f)
                adjList: dict[str, list[int]] = data[name]
                self.vertices = [int(vertex) for vertex in adjList.keys()]
                self.adjList = {int(k): v for k, v in adjList.items()}
        except Exception as e:
            print(f'Error reading graph: {e}')
            print(f'Current path: {getcwd()}')

    def draw(self) -> graphviz.Graph:
        from config import graphvizConfig, graphvizAttrConfig, graphvizEdgeConfig 

        dot = graphviz.Graph(**graphvizConfig)        
        
        for vertex in self.vertices:
            dot.node(str(vertex))
        
        for u in self.vertices:
            for v in self.adjList[u]:
                if u < v:
                    dot.edge(str(u), str(v), **graphvizEdgeConfig)

        try:
            dot.render(f'./../img/{id(self)}', format='png', cleanup=True)
        except Exception as e:
            print(f'Error rendering graph: {e}')
            print(f'Current path: {getcwd()}')

        return dot