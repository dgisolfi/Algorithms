# Assignment 4

**Daniel Gisolfi**

## Single-Source Shortest Paths 

### Asymptotic Running Time

Bellman–Ford algorithm, O(V * E)

As the size of either vertices or edges of a graph grows the big O of the Bellman-Ford algorithm does as well, this is because for every new vertex there is an additional vertex to test paths through. The edges will also grow the worst case time as each new edge is a new possible path that needs to be check for every connected and neighboring vertex.

### Output

```
NEW GRAPH
----vertices---
1
2
3
4
5
-----edges-----
2 → 3 weight=5
2 → 4 weight=8
2 → 5 weight=-4
3 → 2 weight=-2
4 → 3 weight=-3
4 → 5 weight=9
5 → 3 weight=7
5 → 1 weight=2
1 → 2 weight=6
1 → 4 weight=7

done
1 → 1 distance: 0 path: 1
1 → 2 distance: 2 path: 2 ← 3 ← 4 ← 1
1 → 3 distance: 4 path: 3 ← 4 ← 1
1 → 4 distance: 7 path: 4 ← 1
1 → 5 distance: -2 path: 5 ← 2 ← 3 ← 4 ← 1

NEW GRAPH
----vertices---
1
2
3
4
5
6
7
-----edges-----
1 → 2 weight=0
1 → 5 weight=0
1 → 6 weight=0
2 → 3 weight=0
2 → 5 weight=0
2 → 6 weight=0
3 → 4 weight=0
4 → 5 weight=0
5 → 3 weight=0
5 → 6 weight=0
5 → 7 weight=0
6 → 7 weight=0

done
1 → 1 distance: 0 path: 1
1 → 2 distance: 0 path: 2 ← 1
1 → 3 distance: 0 path: 3 ← 2 ← 1
1 → 4 distance: 0 path: 4 ← 3 ← 2 ← 1
1 → 5 distance: 0 path: 5 ← 1
1 → 6 distance: 0 path: 6 ← 1
1 → 7 distance: 0 path: 7 ← 5 ← 1

NEW GRAPH
----vertices---
1
2
3
4
5
6
7
-----edges-----
1 → 2 weight=1
1 → 5 weight=1
1 → 6 weight=1
2 → 3 weight=1
2 → 5 weight=1
2 → 6 weight=1
3 → 4 weight=1
4 → 5 weight=1
5 → 3 weight=1
5 → 6 weight=1
5 → 7 weight=1
6 → 7 weight=1

done
1 → 1 distance: 0 path: 1
1 → 2 distance: 1 path: 2 ← 1
1 → 3 distance: 2 path: 3 ← 2 ← 1
1 → 4 distance: 3 path: 4 ← 3 ← 2 ← 1
1 → 5 distance: 1 path: 5 ← 1
1 → 6 distance: 1 path: 6 ← 1
1 → 7 distance: 2 path: 7 ← 5 ← 1

NEW GRAPH
----vertices---
1
2
3
4
5
6
7
-----edges-----
1 → 2 weight=2
1 → 5 weight=3
1 → 6 weight=3
2 → 3 weight=7
2 → 5 weight=-1
2 → 6 weight=1
3 → 4 weight=1
4 → 5 weight=-2
5 → 3 weight=5
5 → 6 weight=3
5 → 7 weight=1
6 → 7 weight=14

done
1 → 1 distance: 0 path: 1
1 → 2 distance: 2 path: 2 ← 1
1 → 3 distance: 6 path: 3 ← 5 ← 2 ← 1
1 → 4 distance: 7 path: 4 ← 3 ← 5 ← 2 ← 1
1 → 5 distance: 1 path: 5 ← 2 ← 1
1 → 6 distance: 3 path: 6 ← 1
1 → 7 distance: 2 path: 7 ← 5 ← 2 ← 1
```

## Fractional Knapsack problem

### Asymptotic Running Time

Greedy algorithm, O( n )

The greedy algorithm approach for the Fractional Knapsack problem results in linear running time, this is due to the fact that each new item(in this case spice) is iterated through once at the end of the pass over the items the most optimal choice should have been found.

### Output

```
Preforming greedy solution on Fractional Knapsack with capacity=1;
added orange; q=0.5; v=4.5
added blue; q=0.06; v=0.3
added green; q=0.07; v=0.14
added red; q=0.09; v=0.09
Knapsack filled to 0.7200000000000001/1 with value=5.03;

Preforming greedy solution on Fractional Knapsack with capacity=6;
added orange; q=2; v=9.0
added blue; q=0.5; v=2.5
added green; q=0.58; v=1.16
added red; q=0.73; v=0.73
Knapsack filled to 3.81/6 with value=13.39;

Preforming greedy solution on Fractional Knapsack with capacity=10;
added orange; q=2; v=9.0
added blue; q=8; v=5.0
added green; q=0.0; v=0.0
added red; q=0.0; v=0.0
Knapsack filled to 10.0/10 with value=14.0;

Preforming greedy solution on Fractional Knapsack with capacity=20;
added orange; q=2; v=9.0
added blue; q=8; v=5.0
added green; q=6; v=2.0
added red; q=4; v=1.0
Knapsack filled to 20/20 with value=17.0;

Preforming greedy solution on Fractional Knapsack with capacity=21;
added orange; q=2; v=9.0
added blue; q=8; v=5.0
added green; q=6; v=2.0
added red; q=4; v=1.0
Knapsack filled to 20/21 with value=17.0;
```