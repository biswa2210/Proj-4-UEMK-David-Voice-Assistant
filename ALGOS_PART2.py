"""
https://algo-visualize-algorithms.netlify.app/
import  pywhatkit
from say import speakAlgo
from Listen import takeCommand
def ALGOS_1(tag,query):
    if "algoLinearSearch" in tag:
        speakAlgo("A linear search is the simplest method of searching a data set. Starting at the beginning of the data set, each item of data is examined until a match is made. Once the item is found, the search ends. If there is no match, the algorithm must deal with this")
        speakAlgo("do you want to know more about Linear Search ?")
        speakAlgo("please say yes or no")
        ans=takeCommand()
        if ans == "yes":
            pywhatkit.search("linear search algorithm")
        elif ans == "no":
            speakAlgo("ok,no  problem")
        else:
            speakAlgo("Sorry,I can't recognize your answer properly")

"""
"""
https://algo-visualize-algorithms.netlify.app/

"""

import pywhatkit
from say import speakAlgo
from Listen import takeCommand
from CGA2 import controlGoogleAutomation


def ALGOS_2(tag, query):
    if "algoDijkstra" in tag:
        speakAlgo(
            "Dijkstra's algorithm is an algorithm that is used to solve the shortest distance problem. That is, we use it to find the shortest distance between two vertices on a graph. Depending on what the graph represents, we can find shortest routes, minimum costs, etc. all using this algorithm.")
        speakAlgo("do you want to know more about Dijkstra's algorithm ?")
        speakAlgo("please say yes or no")
        ans = takeCommand()
        controlGoogleAutomation(ans, "Dijkstra's Algorithm")


    elif "algoFloydWarshall" in tag:
        speakAlgo(
            "Floyd Warshall algorithm is used to find the shortest path between all vertices in the weighted graph. This algorithm works with both directed and undirected graphs but it does not work along with the graph with negative cycles.")
        speakAlgo("do you want to know more about Floyd Warshall algorithm ?")
        speakAlgo("please say yes or no")
        ans = takeCommand()
        controlGoogleAutomation(ans, "Floyd Warshall Algorithm")

    elif "algoAstar" in tag:
        speakAlgo(
            "A star is a graph traversal and path search algorithm, which is often used in many fields of computer science due to its completeness, optimality, and optimal efficiency. One major practical drawback is its {\displaystyle O(b^{d})}O(b^d) space complexity, as it stores all generated nodes in memory. Thus, in practical travel-routing systems, it is generally outperformed by algorithms which can pre-process the graph to attain better performance, as well as memory-bounded approaches.")
        speakAlgo("do you want to know more about A star algorithm ?")
        speakAlgo("please say yes or no")
        ans = takeCommand()
        controlGoogleAutomation(ans, "A star Algorithm")

    elif "algoBFS" in tag:
        speakAlgo(
            "Breadth-first search is a graph traversal algorithm that starts traversing the graph from the root node and explores all the neighboring nodes. Then, it selects the nearest node and explores all the unexplored nodes. While using BFS for traversal, any node in the graph can be considered as the root node.")
        speakAlgo("do you want to know more about BFS algorithm ?")
        speakAlgo("please say yes or no")
        ans = takeCommand()
        controlGoogleAutomation(ans, "BFS Algorithm")

    elif "algoDFS" in tag:
        speakAlgo(
            "Depth first search (DFS) algorithm starts with the initial node of the graph G, and then goes to deeper and deeper until we find the goal node or the node which has no children. The algorithm, then backtracks from the dead end towards the most recent node that is yet to be completely unexplored.")
        speakAlgo("do you want to know more about DFS algorithm ?")
        speakAlgo("please say yes or no")
        ans = takeCommand()
        controlGoogleAutomation(ans, "DFS Algorithm")

    elif "algoGreedy" in tag:
        speakAlgo(
            "A greedy algorithm is a simple, intuitive algorithm that is used in optimization problems. The algorithm makes the optimal choice at each step as it attempts to find the overall optimal way to solve the entire problem.")
        speakAlgo("do you want to know more about Greedy algorithm ?")
        speakAlgo("please say yes or no")
        ans = takeCommand()
        controlGoogleAutomation(ans, "Greedy Algorithm")

    elif "algoHuffman" in tag:
        speakAlgo(
            "Huffman coding is a lossless data compression algorithm. In this algorithm, a variable-length code is assigned to input different characters. The code length is related to how frequently characters are used. Most frequent characters have the smallest codes and longer codes for least frequent characters.")
        speakAlgo("do you want to know more about Huffman algorithm ?")
        speakAlgo("please say yes or no")
        ans = takeCommand()
        controlGoogleAutomation(ans, "Huffman Algorithm")

    elif "algoBitwise" in tag:
        speakAlgo(
            "The Bitwise Algorithms are used to perform operations at bit-level or to manipulate bits in different ways. The bitwise operations are found to be much faster and are some times used to improve the efficiency of a program.")
        speakAlgo("do you want to know more about Bitwise algorithm ?")
        speakAlgo("please say yes or no")
        ans = takeCommand()
        controlGoogleAutomation(ans, "Bitwise Algorithm")

    elif "algoGraph" in tag:
        speakAlgo(
            "A graph is an abstract notation used to represent the connection between pairs of objects. A graph consists of − Vertices − Interconnected objects in a graph are called vertices.")
        speakAlgo("do you want to know more about Graph algorithm ?")
        speakAlgo("please say yes or no")
        ans = takeCommand()
        controlGoogleAutomation(ans, "Graph Algorithm")

    elif "algoRandomized" in tag:
        speakAlgo(
            "An algorithm that uses random numbers to decide what to do next anywhere in its logic is called a Randomized Algorithm. For example, in Randomized Quick Sort, we use a random number to pick the next pivot.")
        speakAlgo("do you want to know more about Randomized algorithm ?")
        speakAlgo("please say yes or no")
        ans = takeCommand()
        controlGoogleAutomation(ans, "Randomized Algorithm")

    elif "algoKarger" in tag:
        speakAlgo(
            "Karger's algorithm is a randomized algorithm to compute a minimum cut of a connected graph. It was invented by David Karger and first published in 1993.")
        speakAlgo("do you want to know more about Karger algorithm ?")
        speakAlgo("please say yes or no")
        ans = takeCommand()
        controlGoogleAutomation(ans, "Karger Algorithm")

    elif "algoHamiltonianCycle" in tag:
        speakAlgo(
            "Hamiltonian Path in an undirected graph is a path that visits each vertex exactly once. A Hamiltonian cycle (or Hamiltonian circuit) is a Hamiltonian Path such that there is an edge (in the graph) from the last vertex to the first vertex of the Hamiltonian Path. Determine whether a given graph contains Hamiltonian Cycle or not. If it contains, then prints the path.")
        speakAlgo("do you want to know more about Hamiltonian Cycle algorithm ?")
        speakAlgo("please say yes or no")
        ans = takeCommand()
        controlGoogleAutomation(ans, "Hamiltonian Cycle Algorithm")

    elif "algoFleury" in tag:
        speakAlgo(
            "Fleury's Algorithm is used to display the Euler path or Euler circuit from a given graph. In this algorithm, starting from one edge, it tries to move other adjacent vertices by removing the previous vertices.")
        speakAlgo("do you want to know more about Fleury algorithm ?")
        speakAlgo("please say yes or no")
        ans = takeCommand()
        controlGoogleAutomation(ans, "Fleury Algorithm")

    elif "algoEulerianPath" in tag:
        speakAlgo(
            "Eulerian Path is a path in graph that visits every edge exactly once. Eulerian Circuit is an Eulerian Path which starts and ends on the same vertex.")
        speakAlgo("do you want to know more about Eulerian Path algorithm ?")
        speakAlgo("please say yes or no")
        ans = takeCommand()
        controlGoogleAutomation(ans, "Eulerian Path Algorithm")

    elif "algoTarjan" in tag:
        speakAlgo(
            "Eulerian Path is a path in graph that visits every edge exactly once. Eulerian Circuit is an Eulerian Path which starts and ends on the same vertex.")
        speakAlgo("do you want to know more about Tarjan algorithm ?")
        speakAlgo("please say yes or no")
        ans = takeCommand()
        controlGoogleAutomation(ans, "Tarjan Algorithm")

    elif "algoTransitiveClosure" in tag:
        speakAlgo(
            "Transitive Closure it the reachability matrix to reach from vertex u to vertex v of a graph. One graph is given, we have to find a vertex v which is reachable from another vertex u, for all vertex pairs (u, v).")
        speakAlgo("do you want to know more about Transitive Closure algorithm ?")
        speakAlgo("please say yes or no")
        ans = takeCommand()
        controlGoogleAutomation(ans, "Transitive Closure Algorithm")

    elif "algoBiconnectedGraph" in tag:
        speakAlgo(
            "A Biconnected Graph is a connected and non-separable graph, meaning that if any one vertex were to be removed, the graph will remain connected. Therefore a biconnected graph has no articulation vertices.")
        speakAlgo("do you want to know more about Biconnected Graph algorithm ?")
        speakAlgo("please say yes or no")
        ans = takeCommand()
        controlGoogleAutomation(ans, "Biconnected Graph Algorithm")

    elif "algoJohnson" in tag:
        speakAlgo(
            "Johnson's algorithm is a way to find the shortest paths between all pairs of vertices in an edge-weighted directed graph. It allows some of the edge weights to be negative numbers, but no negative-weight cycles may exist. It works by using the Bellman–Ford algorithm to compute a transformation of the input graph that removes all negative weights, allowing Dijkstra's algorithm to be used on the transformed graph.")
        speakAlgo("do you want to know more about Johnson algorithm ?")
        speakAlgo("please say yes or no")
        ans = takeCommand()
        controlGoogleAutomation(ans, "Johnson Algorithm")

    elif "algoBellmanFord" in tag:
        speakAlgo(
            "The Bellman–Ford algorithm is an algorithm that computes shortest paths from a single source vertex to all of the other vertices in a weighted digraph.")
        speakAlgo("do you want to know more about Bellman Ford algorithm ?")
        speakAlgo("please say yes or no")
        ans = takeCommand()
        controlGoogleAutomation(ans, "Bellman Ford Algorithm")

    elif "algoFordFulkerson" in tag:
        speakAlgo(
            "The Ford–Fulkerson method or Ford–Fulkerson algorithm (FFA) is a greedy algorithm that computes the maximum flow in a flow network. It is sometimes called a method instead of an algorithm as the approach to finding augmenting paths in a residual graph is not fully specified or it is specified in several implementations with different running times.")
        speakAlgo("do you want to know more about Ford Fulkerson algorithm ?")
        speakAlgo("please say yes or no")
        ans = takeCommand()
        controlGoogleAutomation(ans, "Ford Fulkerson Algorithm")

    elif "algoHopcroftKarp" in tag:
        speakAlgo(
            "Hopcroft–Karp algorithm (sometimes more accurately called the Hopcroft–Karp–Karzanov algorithm) is an algorithm that takes as input a bipartite graph and produces as output a maximum cardinality matching – a set of as many edges as possible with the property that no two edges share an endpoint.")
        speakAlgo("do you want to know more about Hopcroft Karp algorithm ?")
        speakAlgo("please say yes or no")
        ans = takeCommand()
        controlGoogleAutomation(ans, "Hopcroft Karp Algorithm")

    elif "algoBoruvka" in tag:
        speakAlgo(
            "Borůvka's algorithm is a greedy algorithm for finding a minimum spanning tree in a graph, or a minimum spanning forest in the case of a graph that is not connected.")
        speakAlgo("do you want to know more about Boruvka algorithm ?")
        speakAlgo("please say yes or no")
        ans = takeCommand()
        controlGoogleAutomation(ans, "Boruvka Algorithm")

    elif "algoKaratsuba" in tag:
        speakAlgo(
            "The Karatsuba algorithm is a fast multiplication algorithm. It was discovered by Anatoly Karatsuba in 1960 and published in 1962.")
        speakAlgo("do you want to know more about Karatsuba algorithm ?")
        speakAlgo("please say yes or no")
        ans = takeCommand()
        controlGoogleAutomation(ans, "Karatsuba Algorithm")

    elif "algoFloodFill" in tag:
        speakAlgo(
            "Flood fill, also called seed fill, is a flooding algorithm that determines and alters the area connected to a given node in a multi-dimensional array with some matching attribute. It is used in the bucket fill tool of paint programs to fill connected, similarly-colored areas with a different color.")
        speakAlgo("do you want to know more about Flood Fill algorithm ?")
        speakAlgo("please say yes or no")
        ans = takeCommand()
        controlGoogleAutomation(ans, "Flood Fill Algorithm")

    elif "algoKruskal" in tag:
        speakAlgo(
            "Kruskal's algorithm finds a minimum spanning forest of an undirected edge-weighted graph. If the graph is connected, it finds a minimum spanning tree.")
        speakAlgo("do you want to know more about Kruskal algorithm ?")
        speakAlgo("please say yes or no")
        ans = takeCommand()
        controlGoogleAutomation(ans, "Kruskal Algorithm")

    elif "algoTopologicalSort" in tag:
        speakAlgo(
            "The topological sort algorithm takes a directed graph and returns an array of the nodes where each node appears before all the nodes it points to.")
        speakAlgo("do you want to know more about Topological Sort algorithm ?")
        speakAlgo("please say yes or no")
        ans = takeCommand()
        controlGoogleAutomation(ans, "Topological Sort Algorithm")

    elif "algoPrims" in tag:
        speakAlgo(
            "Prim's Algorithm is a greedy algorithm that is used to find the minimum spanning tree from a graph. Prim's algorithm finds the subset of edges that includes every vertex of the graph such that the sum of the weights of the edges can be minimized.")
        speakAlgo("do you want to know more about Prim's Minimum Spanning algorithm ?")
        speakAlgo("please say yes or no")
        ans = takeCommand()
        controlGoogleAutomation(ans, "Prim's Minimum Spanning Algorithm")

    elif "algoKSmallest" in tag:
        speakAlgo(
            "The Kth smallest algorithm is the minimum possible n such that there are at least k elements in the array <= n. In other words, if the array A was sorted, then A[k - 1] ( k is 1 based, while the arrays are 0 based ).")
        speakAlgo("do you want to know more about K Smallest algorithm ?")
        speakAlgo("please say yes or no")
        ans = takeCommand()
        controlGoogleAutomation(ans, "K Smallest Algorithm")

    elif "algoStrassen" in tag:
        speakAlgo(
            "The Strassen algorithm, named after Volker Strassen, is an algorithm for matrix multiplication. It is faster than the standard matrix multiplication algorithm for large matrices, with a better asymptotic complexity, although the naive algorithm is often better for smaller matrices.")
        speakAlgo("do you want to know more about Strassen's algorithm ?")
        speakAlgo("please say yes or no")
        ans = takeCommand()
        controlGoogleAutomation(ans, "Strassen Algorithm")

    elif "algoCooleyTukeyFFT" in tag:
        speakAlgo(
            "The Cooley–Tukey algorithm, named after J. W. Cooley and John Tukey, is the most common fast Fourier transform (FFT) algorithm. It re-expresses the discrete Fourier transform (DFT) of an arbitrary composite size {\displaystyle N=N_{1}N_{2}}{\displaystyle N=N_{1}N_{2}} in terms of N1 smaller DFTs of sizes N2, recursively, to reduce the computation time to O(N log N) for highly composite N (smooth numbers).")
        speakAlgo("do you want to know more about Cooley Tukey Fast Fourier Transform algorithm ?")
        speakAlgo("please say yes or no")
        ans = takeCommand()
        controlGoogleAutomation(ans, "Cooley Tukey Fast Fourier Transform Algorithm")

    elif "algoDivideAndConquer" in tag:
        speakAlgo(
            "Divide and Conquer is an algorithm design paradigm. A divide-and-conquer algorithm recursively breaks down a problem into two or more sub-problems of the same or related type, until these become simple enough to be solved directly. The solutions to the sub-problems are then combined to give a solution to the original problem.")
        speakAlgo("do you want to know more about Divide and Conquer algorithm ?")
        speakAlgo("please say yes or no")
        ans = takeCommand()
        controlGoogleAutomation(ans, "Divide and Conquer Algorithm")

    elif "algoChineseRemainder" in tag:
        speakAlgo(
            "The Chinese remainder theorem states that if one knows the remainders of the Euclidean division of an integer n by several integers, then one can determine uniquely the remainder of the division of n by the product of these integers, under the condition that the divisors are pairwise coprime.")
        speakAlgo("do you want to know more about Chinese Remainder Theorem algorithm ?")
        speakAlgo("please say yes or no")
        ans = takeCommand()
        controlGoogleAutomation(ans, "Chinese Remainder Theorem Algorithm")

    elif "algoAmicablePair" in tag:
        speakAlgo(
            "An amicable pair consists of two integers for which the sum of proper divisors (the divisors excluding the number itself) of one number equals the other. Amicable pairs are occasionally called friendly pairs.")
        speakAlgo("do you want to know more about Amicable Pair algorithm ?")
        speakAlgo("please say yes or no")
        ans = takeCommand()
        controlGoogleAutomation(ans, "Amicable Pair Algorithm")

    elif "algoBrent" in tag:
        speakAlgo(
            "Brent's method is a hybrid root-finding algorithm combining the bisection method, the secant method and inverse quadratic interpolation. It has the reliability of bisection but it can be as quick as some of the less-reliable methods. The algorithm tries to use the potentially fast-converging secant method or inverse quadratic interpolation if possible, but it falls back to the more robust bisection method if necessary.")
        speakAlgo("do you want to know more about Brent's algorithm ?")
        speakAlgo("please say yes or no")
        ans = takeCommand()
        controlGoogleAutomation(ans, "Brent's Algorithm")

    elif "algoReverseDelete" in tag:
        speakAlgo(
            "The reverse-delete algorithm is an algorithm in graph theory used to obtain a minimum spanning tree from a given connected, edge-weighted graph. It first appeared in Kruskal (1956), but it should not be confused with Kruskal's algorithm which appears in the same paper. If the graph is disconnected, this algorithm will find a minimum spanning tree for each disconnected part of the graph.")
        speakAlgo("do you want to know more about Reverse Delete algorithm ?")
        speakAlgo("please say yes or no")
        ans = takeCommand()
        controlGoogleAutomation(ans, "Reverse Delete Algorithm")

    elif "algoEdmonds" in tag:
        speakAlgo(
            "Edmonds' algorithm or Chu–Liu/Edmonds' algorithm is an algorithm for finding a spanning arborescence of minimum weight (sometimes called an optimum branching). It is the directed analog of the minimum spanning tree problem. The algorithm was proposed independently first by Yoeng-Jin Chu and Tseng-Hong Liu (1965) and then by Jack Edmonds (1967).")
        speakAlgo("do you want to know more about Edmonds algorithm ?")
        speakAlgo("please say yes or no")
        ans = takeCommand()
        controlGoogleAutomation(ans, "Edmonds Algorithm")



