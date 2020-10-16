class DijkstraDistance(object):
    """Implementation of Dijkstra's distance algorithm"""
    def __init__(self, nodes, edges):
        """Initializes Dijkstra's distance class

        Args:
          nodes (list(str)): all nodes in the graph. cannot have duplicate
            values
          edges (list(tuple)): all edges in the graph. each tuple consists of
            two nodes and one edge weight in that order. direction moves from
            the first node to the second in th tuple.

        Returns an instance of the DijkstraDistance class
        """
        self.nodes = nodes
        self.edges = edges

    def find_shortest_path(self, node_a, node_b):
        """Finds the shortst path from node_a to node_b in the graph

        Args:
          node_a (str): start node id. must be from the list of nodes
            used to initialize object.
          node_b (str): end node id. must be from list of nodes used to
            initialize object

        Returns an int (shortest distance between two nodes) and a list
           of nodes in the order you need to traverse from node_a to node_b
           in the shortest possible distance.
        """
        # initialize ditionary of values
        node_wts = {n: None for n in self.nodes}

        # set weight of node_a to 0
        node_wts[node_a] = 0

        # list to store visited nodes and their min path
        visited_nodes = []

        # dict to shortest paths between each node
        shortest_paths = {}

        while True:
            # find node with minimum value that has not been visited
            filtered_node_wts = {k: v for k, v in node_wts.items() if v is not None}
            min_node = [
                n[0] for n in sorted(filtered_node_wts.items(), key=lambda item: item[1])
                if n[0] not in visited_nodes
            ][0]
            if min_node == node_b:
                break

            # get all edges that begin from that node
            from_edges = [edge for edge in self.edges if edge[0] == min_node]

            # iterate through each edge and update the
            # value node at the other end if its value
            # is None or if its valu is less than the edge
            # weight
            for edge in from_edges:
                to_node = edge[1]
                edge_wt = edge[-1]
                total_dist = node_wts[min_node] + edge_wt
                if node_wts[to_node] is None or total_dist < node_wts[to_node]:
                    shortest_paths[to_node] = min_node
                    node_wts[to_node] = total_dist

            # add node to visited nodes list
            visited_nodes.append(min_node)

        # derive and return path
        path = [node_b]
        prev_node = node_b
        while True:
            prev_node = shortest_paths[prev_node]
            path.append(prev_node)
            if prev_node == node_a:
                break

        return node_wts[node_b], path[::-1]
