from os import getcwd
import graphviz
import json
from src.config import graphvizConfig, graphvizAttrConfig, graphvizEdgeConfig , graphvizCaptionConfig
from src.misc import get_distinct_colors
from pprint import pprint
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

    def nonNeighbors(self, u: int) -> list[int]:
        return [v for v in self.vertices if v not in self.adjList[u] and v != u]

    def adjacent(self, u: int, v: int) -> bool:
        return v in self.adjList[u]

    def draw(self, save: bool = False, name: str = None, color: bool = False, color_map: dict[int, int] = None, caption: str = None) -> graphviz.Graph:
        if color ^ (color_map is not None):
            raise ValueError('color and colors must be both True or False') 

        dot = graphviz.Graph(**graphvizConfig)        

        if color:
            enum_colors = {v: i for i, v in enumerate(set(color_map.values()))}
            distinct_colors = get_distinct_colors(len(set(color_map.values())))
            hex_map = {v: distinct_colors[enum_colors[color_map[v]]] for v in self.vertices}
            for vertex in self.vertices: dot.node(str(vertex), style='filled', fillcolor=hex_map[vertex])
        else:
            for vertex in self.vertices: dot.node(str(vertex))
        
        for u in self.vertices:
            for v in self.adjList[u]:
                if u < v:
                    dot.edge(str(u), str(v), **graphvizEdgeConfig)

        if caption is not None:
            dot.attr(label=caption, **graphvizCaptionConfig)

        if save:
            try:
                name = name if name is not None else id(self)
                dot.render(f'./img/{name}', format='png', cleanup=True)
            except Exception as e:
                print(f'Error rendering graph: {e}')
                print(f'Current path: {getcwd()}')

        return dot

    def drawWLk(self, colorMap: dict[tuple, int], save: bool = False, name: str = None, caption: str = None):

        dot = graphviz.Graph(**graphvizConfig)

        enumColors = {v: i for i, v in enumerate(set(colorMap.values()))}
        distinctColors = get_distinct_colors(len(set(colorMap.values())))
        hexMap = {t: distinctColors[enumColors[colorMap[t]]] for t in colorMap.keys()}
        for t in colorMap.keys():
            # dot.node(str(t), style='"rounded,filled"', fillcolor=hexMap[t], shape='box')
            dot.node(str(t), style='rounded,filled', fillcolor=hexMap[t], shape='box')

        if caption is not None:
            dot.attr(label=caption, **graphvizCaptionConfig)

        if save:
            try:
                name = name if name is not None else id(self)
                dot.render(f'./img/{name}', format='png', cleanup=True)
            except Exception as e:
                print(f'Error rendering graph: {e}')
                print(f'Current path: {getcwd()}')