from .base import BaseGraph, if_node_not_exist
from .score_func import *

class Graph(BaseGraph):

    """
    Examples
    --------
    ```python
    from core import Graph
    graph = Graph()

    graph.add_edge(1, 2)
    graph.add_edge(1, 3)

    print(graph.get_nodes)
    >>> [1, 2, 3]

    print(graph.get_average_degree)
    >>> 2.0

    print(graph.get_neighbors(1))
    >>> [2, 3]

    print(graph.get_neighbors_size(1))
    >>> 2

    print(graph.edges)
    >>> {1: [2, 3]}
    ```
    """
    
    @if_node_not_exist
    def common_neighbors(self, node1: nodeId, node2: nodeId) -> int:
        """
        **Common Neighbors**
        --------------------

        > Calculate the common neighbors score between two nodes.

        Parameters
        ----------
        node1 : nodeId
            A node id of the first node.
        node2 : nodeId
            A node id of the second node.

        Returns
        -------
        int
            The common neighbors score between two nodes.
        
        Examples
        --------
        ```python
        from core import Graph

        graph = Graph()
        graph.add_edge(1, 2)
        graph.add_edge(1, 3)
        graph.add_edge(2, 3)

        print(graph.common_neighbors(1, 2))
        >>> 1
        ```
        """
        
        return CommonNeighbors.func(self, node1, node2)

    @if_node_not_exist
    def jaccard_coefficient(self, node1: nodeId, node2: nodeId) -> float:
        """
        **Jaccard Coefficient**
        -----------------------

        > Calculate the Jaccard coefficient score between two nodes.

        Parameters
        ----------
        node1 : nodeId
            A node id of the first node.
        node2 : nodeId
            A node id of the second node.

        Returns
        -------
        float
            The Jaccard coefficient score between two nodes.
        
        Examples
        --------
        ```python
        from core import Graph

        graph = Graph()
        graph.add_edge(1, 2)
        graph.add_edge(1, 3)
        graph.add_edge(2, 3)

        print(graph.jaccard_coefficient(1, 2))
        >>> 0.5
        ```
        """
        
        return JaccardCoefficient.func(self, node1, node2)

    @if_node_not_exist
    def adamic_adar(self, node1: nodeId, node2: nodeId) -> float:
        """
        **Adamic-Adar**
        ---------------
        
        > Calculate the Adamic-Adar score between two nodes.

        Parameters
        ----------
        node1 : nodeId
            A node id of the first node.
        node2 : nodeId
            A node id of the second node.

        Returns
        -------
        float
            The Adamic-Adar score between two nodes.
        
        Examples
        --------
        ```python
        from core import Graph

        graph = Graph()
        graph.add_edge(1, 2)
        graph.add_edge(1, 3)
        graph.add_edge(2, 3)

        print(graph.adamic_adar(1, 2))
        >>> 0.7213475204444817
        ```
        """
        
        return AdamicAdar.func(self, node1, node2)

    @if_node_not_exist
    def shortest_path(self, node1: nodeId, node2: nodeId, max_depth: int=6) -> int:
        """
        **Shortest Path**
        -----------------

        > Calculate the shortest path score between two nodes.

        Parameters
        ----------
        node1 : nodeId
            A node id of the first node.
        node2 : nodeId
            A node id of the second node.

        Returns
        -------
        int
            The shortest path score between two nodes.
        
        Examples
        --------
        ```python
        from core import Graph

        graph = Graph()
        graph.add_edge(1, 2)
        graph.add_edge(1, 3)
        graph.add_edge(2, 4)

        print(graph.shortest_path(1, 4))
        >>> 2
        ```
        """
        return ShortestPath.func(self, node1, node2, max_depth)

    @if_node_not_exist
    def katz_score(self, node1: nodeId, node2: nodeId, alpha: float=1.0, beta: float=1.0, max_length: int=100) -> float:
        """
        **Katz Score**
        --------------

        > Calculate the Katz score between two nodes.

        Parameters
        ----------
        node1 : nodeId
            A node id of the first node.
        node2 : nodeId
            A node id of the second node.

        Returns
        -------
        float
            The Katz score between two nodes.
        
        Examples
        --------
        ```python
        graph = Graph()
        graph.add_edge(1, 2)
        graph.add_edge(1, 4)
        graph.add_edge(4, 3)
        graph.add_edge(4, 2)

        print(graph.katz_score(1, 4, alpha=0.8))
        >>> 1.6
        ```
        """
        return KatzScore.func(self, node1, node2, alpha, beta, max_length)
    
    
    def preferential_attachment(self, node1: nodeId, node2: nodeId) -> int:
        """
        **Preferential Attachment**
        --------------------------

        > Calculate the preferential attachment score between two nodes.

        Parameters
        ----------
        node1 : nodeId
            A node id of the first node.
        node2 : nodeId
            A node id of the second node.

        Returns
        -------
        int
            The preferential attachment score between two nodes.
        
        Examples
        --------
        ```python
        graph = Graph()

        graph.add_edge(1, 2)
        graph.add_edge(1, 4)
        graph.add_edge(4, 3)
        graph.add_edge(4, 2)

        print(graph.preferential_attachment(1, 4))

        """
        pa1 = self.get_neighbors_size(node1)
        pa2 = self.get_neighbors_size(node2)

        # if pa1*pa2 == 0 and pa1+pa2 != 0:
        #     return pa1+pa2
        if pa1 <0 and pa2 <0:
            return pa1+pa2

        # else:
        return pa1*pa2