"""Optional focused check starting points; expand them across the week."""

from copy import deepcopy

from network_support import validate_model
from main import breadth_first, depth_first, shortest_hop_path, MY_RESTRICTION

TEST_STAGE = 2  # Raise to 3 Thursday after completing the route tests.


def test_model():
    """Begin Monday with a clearly valid two-way model and an unknown reference."""
    assert validate_model({"A": ["B"], "B": ["A"]}) == []
    assert validate_model({"A": ["Missing"]})
    # Add your one broken-and-repaired copy of the workshop model.


def test_traversals():
    """Check independent expectations before trying the full workshop fixture."""
    tiny = {"A": ["B", "C"], "B": ["A"], "C": ["A"], "D": []}
    original = deepcopy(tiny)

    bfs_order, _, bfs_edges = breadth_first(tiny, "A")
    # Expected BFS order
    assert bfs_order == ["A", "B", "C"]
    # No repeated BFS processing
    assert len(bfs_order) == len(set(bfs_order))
    # Four BFS adjacency entries
    assert bfs_edges == 4
    # BFS preserves the source graph
    assert tiny == original

    dfs_order, _, dfs_edges = depth_first(tiny, "A")
    # Expected DFS order
    assert dfs_order == ["A", "B", "C"]
    # No repeated DFS processing
    assert len(dfs_order) == len(set(dfs_order))
    # Four DFS adjacency entries
    assert dfs_edges == 4
    # DFS preserves the source graph
    assert tiny == original


def test_paths_and_personal_case():
    """Check route boundaries and your issued blocked-node result independently."""
    # Check a small known path, start=goal, disconnected goal, and a blocked endpoint.
    # Import the supplied workshop data and use MY_RESTRICTION for your personal case.
    # Check exact expected endpoints/hops or None, consecutive connections, no blocked
    # rooms in a returned route, and unchanged source data.
    raise NotImplementedError("Add Thursday's path and personal-case checks.")


if __name__ == "__main__":
    test_model()
    if TEST_STAGE >= 2:
        test_traversals()
    if TEST_STAGE >= 3:
        test_paths_and_personal_case()
    print("Selected-stage starting checks passed; complete all stages before submission.")