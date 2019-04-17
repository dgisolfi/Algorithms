# Assignment 3

**Daniel Gisolfi**

## Traversals of Linked Objects

Within the implementation of the linked object of the graph there are two traversal methods, both have a worse case running time of O(V+E) where V is the number of verticies and E is the number of edges

### Depth First
Using a depth-first traversal we traverse the structure as deep as possible before exploring its width. This creates many cases in which particular nodes are visited more than once in order to move up the graph through the Branch nodes. In practice this type of traversal is implemented with a stack, this can be done recursively or iteratively but in both cases result in the same worst-case running time.

### Breadth-First
Using a breadth-first traversal we traverse the structure one depth level at a time and explore that level in its entirety by breadth before entering a lower level. The advantage here is that more often than not in a graph there are far fewer levels of height than elements of width, meaning fewer nodes are repeated during the traversal. Unline depth-first a queue is used to ensure the most recently discovered children are traversed first rather than the deeper ones found later in the graph.

## Binary Search Tree

### Results

The average case for all 42 searches was around 25-27 comparisons after a handful of tests. 

### Searching

As this is an implementation of a tree the search operation takes time proportional to the tree's height, so there are cases like an unbalanced tree in which searching becomes an O(n) operations. To search this structure a divide and conquer method is used. Start at the root node comparisons are made by using the two children subtrees of the current node to decide which to search through.