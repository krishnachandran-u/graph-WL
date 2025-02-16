from src.graph import Graph
from src.WL1 import WL1
from src.misc import concat_images_ver

if __name__ == "__main__":
    g = Graph('test.json', 'test1')
    colors_stack, exec_time = WL1(g, trace=True)
    print(f'Execution time: {exec_time}')
    for i, colors in enumerate(colors_stack):
        g.draw(save=True, name=f'test1_{i}', color=True, color_map=colors)
    concat_images_ver([f'test1_{i}.png' for i in range(len(colors_stack))], savePath='test1.png', cleanup=True)