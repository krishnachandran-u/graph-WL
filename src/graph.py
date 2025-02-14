from os import getcwd
import graphviz
import json
from src.config import graphvizConfig, graphvizAttrConfig, graphvizEdgeConfig 
from src.misc import get_distinct_colors
class Graph:
    """ use consecutive natural numbers starting from 0 as vertex labels"""

    def __init__(self, filename: str, name: str):
        try:
            with open(f'./data/{filename}') as f:
                data: dict = json.load(f)
                adjList: dict[str, list[int]] = data[name]
                self.vertices = [int(vertex) for vertex in adjList.keys()]
                self.adjList = {int(k): v for k, v in adjList.items()}
        except Exception as e:
            print(f'Error reading graph: {e}')
            print(f'Current path: {getcwd()}')

    def neighbors(self, u: int) -> list[int]:
        return self.adjList[u]

    def draw(self, save: bool = False, color: bool = False, color_map: dict[int, int] = None) -> graphviz.Graph:
        if color ^ (color_map is not None):
            raise ValueError('color and colors must be both True or False') 

        dot = graphviz.Graph(**graphvizConfig)        

        if color:
            distinct_colors = get_distinct_colors(len(set(color_map.values())))
            hex_map = {v: distinct_colors[color_map[v]] for v in self.vertices}
            for vertex in self.vertices: dot.node(str(vertex), style='filled', fillcolor=hex_map[vertex])
        else:
            for vertex in self.vertices: dot.node(str(vertex))
        
        for u in self.vertices:
            for v in self.adjList[u]:
                if u < v:
                    dot.edge(str(u), str(v), **graphvizEdgeConfig)

        if save:
            try:
                dot.render(f'./img/{id(self)}', format='png', cleanup=True)
            except Exception as e:
                print(f'Error rendering graph: {e}')
                print(f'Current path: {getcwd()}')

        return dot