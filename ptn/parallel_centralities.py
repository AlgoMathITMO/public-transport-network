from multiprocessing import Pool, cpu_count
from typing import Optional, List, Dict

import networkx as nx
import pandas as pd


def chunks(list_: list, n_chunks: int) -> List[tuple]:
    return [tuple(list_[i: i + n_chunks]) for i in range(0, len(list_), n_chunks)]


def betweenness_centrality_parallel(
        graph: nx.Graph,
        weight: Optional[str] = 'weight',
        pool: Optional[Pool] = None,
        processes: Optional[int] = None,
) -> Dict[int, float]:
    if processes is None:
        processes = 2 * cpu_count() // 3
        
    close = False
        
    if pool is None:
        pool = Pool(processes=processes)
        close = True

    node_divisor = len(pool._pool) * 4
    node_chunks = chunks(list(graph.nodes()), int(graph.order() / node_divisor))
    n_chunks = len(node_chunks)

    betweenness_centrality_chunks = pool.starmap(
        nx.betweenness_centrality_subset,
        zip(
            [graph] * n_chunks,
            node_chunks,
            [list(graph)] * n_chunks,
            [True] * n_chunks,
            [weight] * n_chunks,
        ),
    )

    betweenness_centrality = betweenness_centrality_chunks[0]

    for betweenness_centrality_chunk in betweenness_centrality_chunks[1:]:
        for n in betweenness_centrality_chunk:
            betweenness_centrality[n] += betweenness_centrality_chunk[n]

    if close:
        pool.close()

    return betweenness_centrality


def single_source_dijkstra_path_subset(
        graph: nx.Graph,
        subset: List[int],
        weight: Optional[str] = 'weight',
) -> Dict[int, Dict[int, float]]:
    return {
        node: dict(nx.single_source_dijkstra_path(graph, node, weight=weight))
        for node in subset
    }


def shortest_paths_parallel(
        graph: nx.Graph,
        weight: Optional[str] = 'weight',
        pool: Optional[Pool] = None,
        processes: Optional[int] = None,
) -> Dict[int, Dict[int, float]]:
    if processes is None:
        processes = 2 * cpu_count() // 3
        
    close = False
        
    if pool is None:
        pool = Pool(processes=processes)
        close = True

    node_divisor = len(pool._pool) * 4
    node_chunks = chunks(list(graph.nodes()), int(graph.order() / node_divisor))
    n_chunks = len(node_chunks)

    shortest_paths_chunks = pool.starmap(
        single_source_dijkstra_path_subset,
        zip(
            [graph] * n_chunks,
            node_chunks,
            [weight] * n_chunks,
        ),
    )

    shortest_paths = shortest_paths_chunks[0]

    for shortest_paths_chunk in shortest_paths_chunks[1:]:
        shortest_paths.update(shortest_paths_chunk)

    if close:
        pool.close()

    return shortest_paths


def single_source_dijkstra_path_length_subset(
        graph: nx.Graph,
        subset: List[int],
        weight: Optional[str] = 'weight',
) -> Dict[int, Dict[int, float]]:
    return {
        node: dict(nx.single_source_dijkstra_path_length(graph, node, weight=weight))
        for node in subset
    }


def shortest_path_lengths_parallel(
        graph: nx.Graph,
        weight: Optional[str] = 'weight',
        pool: Optional[Pool] = None,
        processes: Optional[int] = None,
) -> Dict[int, Dict[int, float]]:
    if processes is None:
        processes = 2 * cpu_count() // 3
        
    close = False
        
    if pool is None:
        pool = Pool(processes=processes)
        close = True

    node_divisor = len(pool._pool) * 4
    node_chunks = chunks(list(graph.nodes()), int(graph.order() / node_divisor))
    n_chunks = len(node_chunks)

    shortest_path_lengths_chunks = pool.starmap(
        single_source_dijkstra_path_length_subset,
        zip(
            [graph] * n_chunks,
            node_chunks,
            [weight] * n_chunks,
        ),
    )

    shortest_path_lengths = shortest_path_lengths_chunks[0]

    for shortest_path_lengths_chunk in shortest_path_lengths_chunks[1:]:
        shortest_path_lengths.update(shortest_path_lengths_chunk)

    if close:
        pool.close()

    return shortest_path_lengths


def closeness_centrality_parallel(shortest_path_lengths: Dict[int, Dict[int, float]]) -> Dict[int, float]:
    shortest_path_lengths = pd.DataFrame(shortest_path_lengths)

    n_nodes = shortest_path_lengths.shape[0]
    n_reachable = shortest_path_lengths.notna().sum(axis=0)

    distances = shortest_path_lengths.sum(axis=0)
    distances[distances == 0] = 1

    return (n_reachable - 1) ** 2 / ((n_nodes - 1) * distances)
