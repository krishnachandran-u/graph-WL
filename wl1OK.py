from src.graph import Graph
from src.wl1 import wl1
from src.misc import concat_images

if __name__ == "__main__":
    g = Graph('test.json', 'test1')
    colors_stack, msets_next_occ, exec_time = wl1(g, trace=True)
    print(f'Execution time: {exec_time}')
    for i, colors in enumerate(colors_stack):
        g.draw(save=True, name=f'test1_{i}', color=True, color_map=colors)
    concat_images([f'test1_{i}.png' for i in range(len(colors_stack))], savePath='test1.png', cleanup=True)