import networkx as nx
import json
import hashlib
from itertools import combinations

def generate_all_graphs(n):
    max_edges = n * (n - 1) // 2
    
    result = {}
    
    canonical_forms = set()
    
    for edge_count in range(max_edges + 1):
        for edges in combinations(combinations(range(n), 2), edge_count):
            G = nx.Graph()
            G.add_nodes_from(range(n))
            G.add_edges_from(edges)
            
            canonical_G = nx.to_graph6_bytes(G)
            
            if canonical_G in canonical_forms:
                continue
                
            canonical_forms.add(canonical_G)
            
            adj_list = {i: sorted(list(G.neighbors(i))) for i in range(n)}
            
            hash_key = hashlib.md5(canonical_G).hexdigest()
            
            result[hash_key] = adj_list
    
    return result

def save_graphs_to_json(n, filename="graphs.json"):
    """
    Generate all non-isomorphic graphs with n vertices and save to a JSON file.
    
    Args:
        n: Number of vertices
        filename: Name of the output JSON file
    """
    graphs = generate_all_graphs(n)
    
    with open(filename, 'w') as f:
        json.dump(graphs, f, indent=2)
    
    print(f"Generated {len(graphs)} non-isomorphic graphs with {n} vertices.")
    return len(graphs)

if __name__ == "__main__":
    import sys
    
    if len(sys.argv) > 1:
        n = int(sys.argv[1])
        # if n > 7:
        #     print("Warning: Generating all graphs for n > 7 may take a very long time.")
        #     response = input("Continue? (y/n): ")
        #     if response.lower() != 'y':
        #         sys.exit(0)
        
        filename = f"./data/graphs_{n}.json"
        count = save_graphs_to_json(n, filename)
        print(f"Saved {count} graphs to {filename}")
    else:
        print("Usage: python generate_graphs.py <number_of_vertices>")
        print("Example: python generate_graphs.py 4")