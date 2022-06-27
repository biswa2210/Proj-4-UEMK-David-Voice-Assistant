import pywhatkit
from say import speakNCS
def controlGoogleAutomation(ans,statement):
    if ans == "yes":
        if statement=="Dijkstra's Algorithm":
            pywhatkit.search("Dijkstra's Algorithm")

        elif statement=="Floyd Warshall Algorithm":
            pywhatkit.search("Floyd Warshall Algorithm")

        elif statement=="A star Algorithm":
            pywhatkit.search("A star Algorithm")

        elif statement=="BFS Algorithm":
            pywhatkit.search("BFS Algorithm")

        elif statement=="DFS Algorithm":
            pywhatkit.search("DFS Algorithm")

        elif statement=="Greedy Algorithm":
            pywhatkit.search("Greedy Algorithm")

        elif statement=="Huffman Algorithm":
            pywhatkit.search("Huffman Algorithm")

        elif statement=="Bitwise Algorithm":
            pywhatkit.search("Bitwise Algorithm")

        elif statement=="Graph Algorithm":
            pywhatkit.search("Graph Algorithm")

        elif statement=="Randomized Algorithm":
            pywhatkit.search("Randomized Algorithm")

        elif statement=="Karger Algorithm":
            pywhatkit.search("Karger Algorithm")

        elif statement=="Hamiltonian Cycle Algorithm":
            pywhatkit.search("Hamiltonian Cycle Algorithm")

        elif statement=="Fleury Algorithm":
            pywhatkit.search("Fleury Algorithm")

        elif statement=="Eulerian Path Algorithm":
            pywhatkit.search("Eulerian Path Algorithm")

        elif statement=="Tarjan Algorithm":
            pywhatkit.search("Tarjan Algorithm")

        elif statement=="Transitive Closure Algorithm":
            pywhatkit.search("Transitive Closure Algorithm")

        elif statement=="Biconnected Graph Algorithm":
            pywhatkit.search("Biconnected Graph Algorithm")

        elif statement=="Johnson Algorithm":
            pywhatkit.search("Johnson Algorithm")

        elif statement=="Bellman Ford Algorithm":
            pywhatkit.search("Bellman Ford Algorithm")

        elif statement=="Ford Fulkerson Algorithm":
            pywhatkit.search("Ford Fulkerson Algorithm")

        elif statement=="Hopcroft Karp Algorithm":
            pywhatkit.search("Hopcroft Karp Algorithm")

        elif statement=="Boruvka Algorithm":
            pywhatkit.search("Boruvka Algorithm")

        elif statement=="Karatsuba Algorithm":
            pywhatkit.search("Karatsuba Algorithm")

        elif statement=="Flood Fill Algorithm":
            pywhatkit.search("Flood Fill Algorithm")

        elif statement=="Kruskal Algorithm":
            pywhatkit.search("Kruskal Algorithm")

        elif statement=="Topological Sort Algorithm":
            pywhatkit.search("Topological Sort Algorithm")

        elif statement=="Prim's Minimum Spanning Algorithm":
            pywhatkit.search("Prim's Minimum Spanning Algorithm")

        elif statement=="K Smallest Algorithm":
            pywhatkit.search("K Smallest Algorithm")

        elif statement=="Strassen Algorithm":
            pywhatkit.search("Strassen Algorithm")

        elif statement=="Cooley Tukey Fast Fourier Transform Algorithm":
            pywhatkit.search("Cooley Tukey Fast Fourier Transform Algorithm")

        elif statement=="Divide and Conquer Algorithm":
            pywhatkit.search("Divide and Conquer Algorithm")

        elif statement=="Chinese Remainder Theorem Algorithm":
            pywhatkit.search("Chinese Remainder Theorem Algorithm")

        elif statement=="Amicable Pair Algorithm":
            pywhatkit.search("Amicable Pair Algorithm")

        elif statement=="Brent's Algorithm":
            pywhatkit.search("Brent's Algorithm")

        elif statement=="Reverse Delete Algorithm":
            pywhatkit.search("Reverse Delete Algorithm")

        elif statement=="Edmonds Algorithm":
            pywhatkit.search("Edmonds Algorithm")

    elif ans == "no":
        speakNCS("ok,no  problem")
    else:
        speakNCS("Sorry,I can't recognize your answer properly")


