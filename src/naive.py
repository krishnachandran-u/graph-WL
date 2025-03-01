from src.graph import Graph
from src.misc import generate_permutation_matrices
import numpy as np
import time

def get_adjacency_matrix(g: Graph) -> np.ndarray:
    adjacency_matrix = np.zeros((len(g.vertices), len(g.vertices)), dtype=int)
    for vertex, neighbors in g.adjList.items():
        for neighbor in neighbors:
            adjacency_matrix[vertex][neighbor] = 1
    return np.array(adjacency_matrix)

def naive(g0: Graph, g1: Graph) -> bool:
    start_time = time.perf_counter()
    if len(g0.vertices) != len(g1.vertices):
        return False
    perm = generate_permutation_matrices(len(g0.vertices))
    adj0 = get_adjacency_matrix(g0)
    adj1 = get_adjacency_matrix(g1)
    for p in perm:
        if np.array_equal(adj0 @ p, p @ adj1):
            return True, time.perf_counter() - start_time
    return False, time.perf_counter() - start_time
    