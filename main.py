"""Optional AL08 starter: model Monday, traversals Tuesday, routes Thursday."""

from collections import deque
from network_support import validate_request, record_step
from app_runner import run

STAGE = 2  # Monday 1; Tuesday 2 when traversals work; Thursday 3 when routes work.
MY_RESTRICTION = "A"  # Set this to your instructor-issued case in your personal copy.


# MONDAY — Inspect the supplied model and test copies with a connection mistake.
# No traversal is required for STAGE 1; keep your brief personal model notes.


# TUESDAY — Complete each algorithm separately on the fresh common fixture.
def breadth_first(graph, start):
    """Return BFS order, independent snapshots, and adjacency entries examined."""
    validate_request(graph, start)
    # Queue the start and mark it discovered.
    queue = deque([start])
    discovered = {start}
    # Track visit order, snapshots, and examined adjacency entries.
    order = []
    trace = []
    edges_examined = 0

    # Process the queue and inspect neighbors in listed order.
    while queue:
        node = queue.popleft()
        order.append(node)
        for neighbor in graph[node]:
            edges_examined += 1
            if neighbor not in discovered:
                # Mark each neighbor before queueing it.
                discovered.add(neighbor)
                queue.append(neighbor)
        # Save state after handling this node's neighbors.
        record_step(trace, node, queue, discovered)

    return order, trace, edges_examined


def depth_first(graph, start):
    """Return iterative DFS order, independent snapshots, and adjacency count."""
    validate_request(graph, start)
    # Start with a stack and mark nodes when they are processed.
    stack = [start]
    visited = set()
    # Track visit order, snapshots, and examined adjacency entries.
    order = []
    trace = []
    edges_examined = 0

    # Process the stack, skipping nodes already visited.
    while stack:
        node = stack.pop()
        if node in visited:
            continue
        visited.add(node)
        order.append(node)
        # Reverse neighbors so the first listed available one is next.
        for neighbor in reversed(graph[node]):
            edges_examined += 1
            if neighbor not in visited:
                stack.append(neighbor)
        # Save state after handling this node's neighbors.
        record_step(trace, node, stack, visited)

    return order, trace, edges_examined


# THURSDAY — Save parents during BFS, then follow one chain backward.
def reconstruct_path(parents, goal):
    """Return start-to-goal order by following the BFS parent chain."""
    # Begin at goal and collect names until the parent is None.
    # Reverse the new list before returning it; preserve parents.
    raise NotImplementedError("Complete parent-chain reconstruction.")


def shortest_hop_path(graph, start, goal, blocked=()):
    """Return a permitted fewest-hop path and parents, or None with parent state."""
    blocked_nodes = set(blocked)
    validate_request(graph, start, goal, blocked_nodes)
    # A blocked start or goal returns None and an empty dictionary.
    # Begin parents with start: None and a queue containing start.
    # Process the queue; on reaching goal, return the reconstructed path and parents.
    # For a neighbor not in parents and not blocked, save its first parent and enqueue.
    # If the queue runs out, return None and the parents collected.
    raise NotImplementedError("Complete BFS with parents and blocked nodes.")


def main():
    """Run only the selected completed stage using supplied presentation."""
    run(STAGE, breadth_first, depth_first, shortest_hop_path, MY_RESTRICTION)


if __name__ == "__main__":
    main()