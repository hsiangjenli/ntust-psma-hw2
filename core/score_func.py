from .base import nodeId
from collections import deque
import warnings
import math

class CommonNeighbors:
    """
    **Common neighbors**
    --------------------
    """
    @staticmethod
    def func(self, node1: nodeId, node2: nodeId) -> int:
        """

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
        """
        if node1 == node2:
            warnings.warn("func(common_neighbors): The two nodes are the same.")
            return -2
        
        return len(list(set(self.edges[node1]) & set(self.edges[node2])))
        

class JaccardCoefficient:
    """
    **Jaccard coefficient**
    -----------------------
    """
    @staticmethod
    def func(self, node1: nodeId, node2: nodeId) -> float:
        """

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
        """
        union_size = len(set(self.edges[node1]) | set(self.edges[node2]))
        
        if union_size == 0:
            return 0
        
        return CommonNeighbors.func(self, node1, node2) / union_size


class AdamicAdar:
    """
    **Adamic-Adar**
    ---------------
    """
    
    @staticmethod
    def func(self, node1: nodeId, node2: nodeId) -> float:
        """
        
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
        """
        aa = 0
        cn = CommonNeighbors.func(self, node1, node2)
        
        if cn == 0 or cn == -1:
            return 0
        
        neighbors = list(set(self.get_neighbors(node1)) & set(self.get_neighbors(node2)))

        for neighbor in neighbors:            
            degree = self.get_neighbors_size(neighbor)
            
            if degree != 0:
                aa += 1 / math.log(degree)
        
        return aa


class ShortestPath:
    """
    **Shortest path**
    -----------------
    """

    @staticmethod
    def func(self, node1: nodeId, node2: nodeId, max_depth: int=6) -> int:
        """       
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
        """
        # 重複出現的 
        if node1 == node2:
            return 0
        
        # 從未出現過的新 node
        if node1 not in self.get_nodes or node2 not in self.get_nodes:
            return -1
        
        if node2 in self.edges[node1]:
            return 1
        
        """
        DFS 還沒寫完
        """
        visited = set()
        visited.add(node1)
        queue = deque([(node1, 0)])

        while queue:


            node, depth = queue.popleft()
            
            if depth > max_depth:
                depth = -1

            # 如果有在 snapshot 裡面，才繼續往下找
            if node in self.get_nodes:

                try:
                    neighbors = self.edges[node]
                    for neighbor in neighbors:
        
                        if neighbor == node2:
                            return depth + 1
                        
                        for neighbor in self.edges[node]:
                            if neighbor not in visited:
                                visited.add(neighbor)
                                queue.append((neighbor, depth + 1))
                
                except Exception as e:
                    warnings.warn(f"func(shortest_path): The node {e} does not exist.")
                    continue

        return depth


class KatzScore:
    """
    **Katz score**
    --------------
    """

    @staticmethod
    def func(self, node1: nodeId, node2: nodeId, alpha: float=1.0, beta: float=1.0, max_length: int=1000):
        """

        > Calculate the Katz score between two nodes.
        
        1. Measure the relative degree of influence of an actor (or node) within a social network
        1. Measures influence by taking into account the **total number of walks between a pair of actors**

        Similar
        -------
        1. PageRank
        1. Eigenvector centrality

        Parameters
        ----------
        node1 : nodeId
            A node id of the first node.
        node2 : nodeId
            A node id of the second node.
        alpha : float
            Attenuation factor. 衰減係數，用來控制遠近的影響力，通常介於 0~1 之間
            Connections made with distant neighbors are, however, penalized by an attenuation factor *alpha*. Each path or connection between a pair of nodes is assigned a weight determined by *alpha* and the distance between nodes 
        beta : float, optional
            Weight attributed to the immediate neighborhood, by default 1
        max_length : int, optional

        References
        ----------
        1. [Katz Centrality (Centrality Measure) - GeeksforGeeks](https://www.geeksforgeeks.org/katz-centrality-centrality-measure/)
        1. [katz和eigenvector 中心性](https://zhuanlan.zhihu.com/p/456679785)
        """
        katz_score = 0
        
        for l in range(1, max_length+1):
            for path in KatzScore.get_all_possible_path(self, node1, l):
                if node2 in path:
                    katz_score += alpha ** l
                    katz_score = katz_score*self.get_neighbors_size(node2)
        
        return katz_score
    
    @staticmethod
    def get_all_possible_path(self, start: nodeId, max_length: int) -> list:
        """

        Get all possible path from start node to other nodes.

        Parameters
        ----------
        start : nodeId
            A node id of the start node.
        max_length : int
            The max length of the path.

        Returns
        -------
        list
            A list of all possible path.
        """

        visited = {start}
        paths = [[start]]

        while paths:
            path = paths.pop(0) # 將最左邊的刪除
            node = path[-1] # 取最後一個 node

            if len(path) == max_length:
                
                for neighbor in self.edges[node]:
                    
                    if neighbor not in visited:
                        visited.add(neighbor)
                        new_path = path + [neighbor]
                        paths.append(new_path)
                        yield new_path


# class EigenvectorScore:
    
#     @staticmethod
#     def func(self, node: nodeId) -> float:
#         pass