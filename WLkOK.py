from src.graph import Graph
from src.WLk import WLk
from src.misc import concat_images

if __name__ == "__main__":
    g = Graph('test.json', 'test1')
    colors_map, exec_time = WLk(g=g, k=3, trace=True)
    print(f'Execution time: {exec_time}')
    # g.drawWLk(save=True, name='test1', colorMap=colors_map)
    # for i, colors in enumerate(colors_stack):
    #     g.draw(save=True, name=f'test1_{i}', color=True, color_map=colors)
    # concat_images_ver([f'test1_{i}.png' for i in range(len(colors_stack))], savePath='test1.png', cleanup=True)
    for i, colors in enumerate(colors_map):
        g.drawWLk(save=True, name=f'test1_{i}', colorMap=colors, caption=str(exec_time))
    concat_images([f'test1_{i}.png' for i in range(len(colors_map))], direction="v", save_path='test1.png', cleanup=True)