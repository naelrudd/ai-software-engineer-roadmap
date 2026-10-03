# Module 12 — Graphs

> ⏱ ~5h · 🎯 Model relationships and traverse them correctly.

## Why this matters

Graphs model networks: social, roads, dependencies, the web. BFS/DFS plus shortest-path algorithms are foundational for backend, infrastructure, and AI-tooling work.

---

## Core concepts

### Representations

```python
# adjacency list (most common)
graph = {
    "A": ["B", "C"],
    "B": ["A"],
    "C": ["A"],
}

# grid as implicit graph: neighbors are up/down/left/right
```

Adjacency list: O(V + E) space, fast neighbor iteration. Adjacency matrix: O(V²) space, O(1) edge lookup.

### BFS — shortest path (unweighted)

```python
from collections import deque


def bfs(graph, start):
    dist = {start: 0}
    q = deque([start])
    while q:
        node = q.popleft()
        for nb in graph[node]:
            if nb not in dist:
                dist[nb] = dist[node] + 1
                q.append(nb)
    return dist
```

BFS explores in layers → gives shortest path in unweighted graphs.

### DFS — connectivity, cycles, components

```python
def dfs(graph, node, seen):
    if node in seen:
        return
    seen.add(node)
    for nb in graph[node]:
        dfs(graph, nb, seen)
```

Use an explicit stack if the graph is deep.

### Cycle detection

- Undirected: DFS, if you revisit a node that isn't the parent → cycle.
- Directed: track nodes on the current recursion stack (colors: white/gray/black).

### Topological sort (DAGs)

Order tasks so dependencies come first. Kahn's algorithm (BFS on in-degrees) or DFS postorder reversed.

### Dijkstra (weighted, non-negative)

Priority queue + relaxation. O((V + E) log V).

```python
import heapq


def dijkstra(graph, start):
    dist = {start: 0}
    pq = [(0, start)]
    while pq:
        d, node = heapq.heappop(pq)
        if d > dist.get(node, float("inf")):
            continue
        for nb, w in graph[node]:
            nd = d + w
            if nd < dist.get(nb, float("inf")):
                dist[nb] = nd
                heapq.heappush(pq, (nd, nb))
    return dist
```

---

## Complexity

| Algorithm | Time | Space |
|-----------|------|-------|
| BFS / DFS | O(V + E) | O(V) |
| Topological sort | O(V + E) | O(V) |
| Dijkstra | O((V+E) log V) | O(V) |

---

## Common pitfalls

- Forgetting the visited set → infinite loops.
- Using BFS for weighted shortest paths (use Dijkstra).
- Dijkstra with negative weights (use Bellman-Ford).
- Grid problems: forgetting bounds checks on neighbors.
- Directed vs undirected confusion when building the graph.

---

## Exercises

1. **Number of islands** — grid DFS/BFS.
2. **Clone a graph** — map old→new.
3. **Course schedule** — cycle detection / topological sort.
4. **Shortest path in a grid** — BFS.
5. **Network delay time** — Dijkstra.
6. **Word ladder** — BFS over an implicit graph.

---

## Paired workshop

[Workshop 07 — Evaluate an AI solution](../../workshops/07-evaluate-an-ai-solution/README.md)

## Checklist

- [ ] Can build an adjacency list from edges
- [ ] Can implement BFS and DFS without bugs
- [ ] Understand when BFS beats DFS (shortest path)
- [ ] Can detect cycles and topologically sort
- [ ] Wrote 3 lines in `NOTES.md`
