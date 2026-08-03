"""Graph traversal and shortest-path algorithms."""

from collections import deque
from collections.abc import Hashable, Mapping, Sequence
from heapq import heappop, heappush
from math import inf
from typing import TypeVar

Node = TypeVar("Node", bound=Hashable)


def breadth_first_search(graph: Mapping[Node, Sequence[Node]], start: Node) -> list[Node]:
    """Return reachable nodes in breadth-first order. Time: O(V + E)."""
    visited = {start}; queue = deque([start]); order: list[Node] = []
    while queue:
        node = queue.popleft(); order.append(node)
        for neighbor in graph.get(node, ()):
            if neighbor not in visited:
                visited.add(neighbor); queue.append(neighbor)
    return order


def depth_first_search(graph: Mapping[Node, Sequence[Node]], start: Node) -> list[Node]:
    """Return reachable nodes in iterative depth-first order. Time: O(V + E)."""
    visited: set[Node] = set(); stack = [start]; order: list[Node] = []
    while stack:
        node = stack.pop()
        if node in visited:
            continue
        visited.add(node); order.append(node)
        stack.extend(reversed(graph.get(node, ())))
    return order


def dijkstra(graph: Mapping[Node, Mapping[Node, float]], start: Node) -> dict[Node, float]:
    """Compute shortest distances from start for nonnegative edges. O((V+E)log V)."""
    nodes = set(graph)
    for edges in graph.values():
        nodes.update(edges)
        if any(weight < 0 for weight in edges.values()):
            raise ValueError("Dijkstra's algorithm requires nonnegative weights")
    distances = {node: inf for node in nodes}; distances[start] = 0.0
    heap: list[tuple[float, Node]] = [(0.0, start)]
    while heap:
        distance, node = heappop(heap)
        if distance != distances[node]:
            continue
        for neighbor, weight in graph.get(node, {}).items():
            candidate = distance + weight
            if candidate < distances[neighbor]:
                distances[neighbor] = candidate
                heappush(heap, (candidate, neighbor))
    return distances
