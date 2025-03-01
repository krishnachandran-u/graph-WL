import networkx as nx
from src.WL1 import checkWL1
from src.WLk import checkWLk
import sys
import json
from src.graph import Graph 
from pprint import pprint
import subprocess
import os
from itertools import combinations

def check_isomorphism(graph1_json, graph2_json):
    G1 = nx.Graph(graph1_json)
    G2 = nx.Graph(graph2_json)
    
    return nx.is_isomorphic(G1, G2)

def wl1xnetworkx(filename, k):
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
        networkx_result = check_isomorphism(data[key1], data[key2])

        g0, g1 = Graph(filename, key1), Graph(filename, key2)

        if k == 1:
            WL_result = checkWL1(g0, g1)
        else:
            WL_result = checkWLk(g0, g1, k)
       
        if networkx_result and WL_result:
            result["true positive"] += 1
        elif networkx_result and not WL_result:
            result["false negative"] += 1
        elif not networkx_result and WL_result:
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
        results[i] = wl1xnetworkx(f'graphs_{i}.json', k)
        # os.remove(f'./data/graphs_{i}.json')
    with open(f'./result/wl{k}xnetworkx.json', 'w') as f:
        f.write(json.dumps(results, indent=2))

        