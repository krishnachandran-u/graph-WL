from src.graph import Graph
from src.VF2 import VF2
from bidict import bidict
from pprint import pprint
from src.misc import concat_images

if __name__ == "__main__":
    g0 = Graph('test.json', 'test0')
    g1 = Graph('test.json', 'test0iso')

    matched, execTime = VF2(g0, g1)

    if matched is not None:
        matchedDict = dict(matched)
        print("Isomorphic with mapping")
        pprint(matchedDict, width=1)
        colors1: dict = {v: i for i, v in enumerate(matchedDict.keys())}
        colors2: dict = {v: i for i, v in enumerate(matchedDict.values())}
        g0.draw(save=True, name='test0', color=True, color_map=colors1, caption=str(execTime))
        g1.draw(save=True, name='test0iso', color=True, color_map=colors2, caption=str(execTime))
        concat_images(['test0.png', 'test0iso.png'], direction="h", save_path='concatImage.png', cleanup=True)
    else: 
        print("Not isomorphic")
