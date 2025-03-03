import networkx as nx
from src.WL1 import checkWL1
# from src.WLk import checkWLk
import sys
import json
from src.graph import Graph 
from pprint import pprint
from itertools import combinations
from src.naive import naive
from src.WLk import compareGraphs

def wl1xnaive(filename, k):
    result = {
        "true positive": 0,
        "true negative": 0,
        "false positive": 0,
        "false negative": 0
    }
    with open(f'./data/{filename}', 'r') as f:
        data: dict = json.loads(f.read())
    key_pairs = list(combinations(data.keys(), 2)) 
    print(f'Comparing {len(key_pairs)} pairs of graphs')
    for i, item in enumerate(key_pairs):
        key1, key2 = item
        g0, g1 = Graph(filename, key1), Graph(filename, key2)
        WL_result = compareGraphs(data[key1], data[key2], method='WL', k=k, verbose=False)
        naive_result, _ = naive(g0, g1)
        if naive_result and WL_result:
            result["true positive"] += 1
        elif naive_result and not WL_result:
            result["false negative"] += 1
        elif not naive_result and WL_result:
            result["false positive"] += 1
        else:
            result["true negative"] += 1
        print(f'Processed {i+1}/{len(key_pairs)} pairs of graphs')
    return result

if __name__ == "__main__":
    results = {}
    vertices_upper_bound = int(sys.argv[1])
    k = int(sys.argv[2])
    for i in range(k, vertices_upper_bound + 1):
        # subprocess.run(['python', 'generateGraphs.py', str(i)])
        results[i] = wl1xnaive(f'graphs_{i}.json', k)
        # os.remove(f'./data/graphs_{i}.json')
    with open(f'./result/wl{k}naive.json', 'w') as f:
        f.write(json.dumps(results, indent=2))

        