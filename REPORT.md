# **Report**

## **What is new?**
1. deep_common_neighbors
2. deep_neighbors
3. deep_jaccard_coefficient


## **10 Experiment**

### **E1-networkX `networkX.ipynb`**
> **Concept**  
> - I tested the `greedy_modularity_communities` function in networkX to address my concerns about the effectiveness of my own algorithm implementation.
> - The actual results were unsatisfactory, leading me to speculate that using this method for community detection may result in overly fine-grained partitions.

### **E2 ~ E4 `hw02.ipynb`**
1. E2-deep_common_neighbor-level-1
1. E3-deep_common_neighbor-level-2
1. E4-deep_common_neighbor-level-3

> **Concept**
> If two nodes recursively search for common neighbors within (1, 2, 3) levels, it implies that they are likely to be in the same community, as they will be connected within six steps.

### **E5 ~ E7 `hw02.ipynb`**
1. E5-deep_jaccard_coefficient-level-1-threshold-mean
1. E6-deep_jaccard_coefficient-level-2-threshold-mean
1. E7-deep_jaccard_coefficient-level-3-threshold-mean

> **Concept**  
> - Search for common neighbors between two nodes and **consider the common neighbors and the size of their union neighbors**, the Jaccard coefficient (JC) formula denominator, which is the union neighbor size, may cause the JC to decrease if both nodes have a large number of friends  
> - Additionally, I made a mistake in **only calculating the average JC for the test data**, rather than considering the **average JC for all node combinations**. However, due to computational limitations, I was unable to perform the latter calculation :)  

### **E8 ~ E10 `hw02.ipynb`**
1. E8-deep_jaccard_coefficient-level-1-threshold-mean-minus-var
1. E9-deep_jaccard_coefficient-level-2-threshold-mean-minus-var
1. E10-deep_jaccard_coefficient-level-3-threshold-mean-minus-var

> **Concept**  
> - Same as above, the threshold is the average JC minus variance
> - Their still have mistake in my implementation.

### **Summary and Conclusion**

|Experiment|Accuracy|
|----------|--------|
|E1-networkX|0.49|
|E2-deep_common_neighbor-level-1|0.7|
|E3-deep_common_neighbor-level-2|0.79333|
|E4-deep_common_neighbor-level-3|0.78|
|E5-deep_jaccard_coefficient-level-1-threshold-mean|0.67166|
|E6-deep_jaccard_coefficient-level-2-threshold-mean|0.69166|
|E7-deep_jaccard_coefficient-level-3-threshold-mean|0.705|
|E8-deep_jaccard_coefficient-level-1-threshold-mean-minus-var|0.68333|
|E9-deep_jaccard_coefficient-level-2-threshold-mean-minus-var|0.71666|
|E10-deep_jaccard_coefficient-level-3-threshold-mean-minus-var|0.75666|

I initially intended to use an algorithm similar to "greedy_modularity_communities" in networkX for my homework. 

However, after actually doing it, I found that the results were not satisfactory and the compute time was too long (about 12 hours). 

Later on, I realized that this assignment only focuses on node1 and node2. So, I changed my approach and considered only node1 and node2, which greatly improved the final result.