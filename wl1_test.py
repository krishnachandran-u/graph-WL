from src.graph import Graph
from src.wl1 import wl1

if __name__ == "__main__":
    g = Graph('test.json', 'test')
    colors, exec_time = wl1(g, trace=False)
    print(f'Execution time: {exec_time}')
    g.draw(save=True, color=True, color_map=colors)