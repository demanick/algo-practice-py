from src.dijkstra_distance import DijkstraDistance

def test_init():
    dd = DijkstraDistance(
        nodes=['a', 'b'],
        edges=[('a', 'b', 1)]
    )

def test_shortest_distance():
    """Tests the Dijkstra distance algorithm using an
    example graph from Panos Louridas' book, 'Algorithms'.
    """
    nodes=['A', 'B', 'C', 'D', 'E', 'F']
    edges = [
        ('A', 'B', 3),
        ('A', 'C', 1),
        ('B', 'D', 3),
        ('B', 'F', 6),
        ('C', 'D', 4),
        ('C', 'E', 2),
        ('D', 'F', 1),
        ('E', 'F', 5),
        ('F', 'E', 2)
    ]
    dd = DijkstraDistance(nodes=nodes, edges=edges)
    dist, path = dd.find_shortest_path('A', 'F')
    assert dist == 6
    assert all([a == b for a, b in zip(path, ['A', 'C', 'D', 'F'])])