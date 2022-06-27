# https://algo-visualize-algorithms.netlify.app/
import pywhatkit
from say import speakAlgo
from Listen import takeCommand


def ALGOS_1(tag, query):
    # searching Algorithms --->

    if "algoLinearSearch" in tag:
        speakAlgo(
            "A linear search is the simplest method of searching a data set. Starting at the beginning of the data set, each item of data is examined until a match is made. Once the item is found, the search ends. If there is no match, the algorithm must deal with this")
        speakAlgo("do you want to know more about Linear Search ?")
        speakAlgo("please say yes or no")
        ans = takeCommand()
        if ans == "yes":
            pywhatkit.search("linear search algorithm")
        elif ans == "no":
            speakAlgo("ok,no  problem")
        else:
            speakAlgo("Sorry,I can't recognize your answer properly")

    elif "algoJumpSearch" in tag:
        speakAlgo(
            "a jump search or block search refers to a search algorithm for ordered lists. It works by first checking all items until an item is found that is larger than the search key")
        speakAlgo("do you want to know more about Jump Search ?")
        speakAlgo("please say yes or no")
        ans = takeCommand()
        if ans == "yes":
            pywhatkit.search("jump search algorithm")
        elif ans == "no":
            speakAlgo("ok,no  problem")
        else:
            speakAlgo("Sorry,I can't recognize your answer properly")

    elif "algoInterpolationSearch" in tag:
        speakAlgo(
            "Interpolation search is an algorithm for searching for a key in an array that has been ordered by numerical values assigned to the keys. It was first described by W. W. Peterson in 1957")
        speakAlgo("do you want to know more about Interpolation Search ?")
        speakAlgo("please say yes or no")
        ans = takeCommand()
        if ans == "yes":
            pywhatkit.search("Interpolation search algorithm")
        elif ans == "no":
            speakAlgo("ok,no  problem")
        else:
            speakAlgo("Sorry,I can't recognize your answer properly")

    elif "algoBinarySearch" in tag:
        speakAlgo(
            "binary search, also known as half-interval search, logarithmic search, or binary chop, is a search algorithm that finds the position of a target value within a sorted array. Binary search compares the target value to the middle element of the array")
        speakAlgo("do you want to know more about Binary Search ?")
        speakAlgo("please say yes or no")
        ans = takeCommand()
        if ans == "yes":
            pywhatkit.search("Binary search algorithm")
        elif ans == "no":
            speakAlgo("ok,no  problem")
        else:
            speakAlgo("Sorry,I can't recognize your answer properly")

    elif "algoExponentialSearch" in tag:
        speakAlgo(
            "an exponential search is an algorithm, created by Jon Bentley and Andrew Chi-Chih Yao in 1976, for searching sorted, unbounded/infinite lists")
        speakAlgo("do you want to know more about Exponential Search ?")
        speakAlgo("please say yes or no")
        ans = takeCommand()
        if ans == "yes":
            pywhatkit.search("Exponential search algorithm")
        elif ans == "no":
            speakAlgo("ok,no  problem")
        else:
            speakAlgo("Sorry,I can't recognize your answer properly")

    elif "algoSublistSearch" in tag:
        speakAlgo(
            "The sublist search algorithm works by comparing the first element of the first list with the first element of the second list. If the two values don't match, it goes to the next element of the second list")
        speakAlgo("do you want to know more about Sublist Search ?")
        speakAlgo("please say yes or no")
        ans = takeCommand()
        if ans == "yes":
            pywhatkit.search("Sublist search algorithm")
        elif ans == "no":
            speakAlgo("ok,no  problem")
        else:
            speakAlgo("Sorry,I can't recognize your answer properly")

    elif "algoFibonacciSearch" in tag:
        speakAlgo(
            "the Fibonacci search technique is a method of searching a sorted array using a divide and conquer algorithm that narrows down possible locations with the aid of Fibonacci numbers")
        speakAlgo("do you want to know more about Fibonacci Search ?")
        speakAlgo("please say yes or no")
        ans = takeCommand()
        if ans == "yes":
            pywhatkit.search("Fibonacci search algorithm")
        elif ans == "no":
            speakAlgo("ok,no  problem")
        else:
            speakAlgo("Sorry,I can't recognize your answer properly")

    elif "algoKSearch" in tag:
        speakAlgo(
            "A step array is an array of integer where each element has a difference of at most k with its neighbor. Given a key x, we need to find the index value of x if multiple element exist return the first occurrence of the key")
        speakAlgo("do you want to know more about K Search ?")
        speakAlgo("please say yes or no")
        ans = takeCommand()
        if ans == "yes":
            pywhatkit.search("K search algorithm")
        elif ans == "no":
            speakAlgo("ok,no  problem")
        else:
            speakAlgo("Sorry,I can't recognize your answer properly")

    elif "algoUbiquitousBinarySearch" in tag:
        speakAlgo(
            "We all aware of binary search algorithm. Binary search is easiest difficult algorithm to get it right. I present some interesting problems that I collected on binary search. There were some requests on binary search")
        speakAlgo("do you want to know more about ubiquitous binary Search ?")
        speakAlgo("please say yes or no")
        ans = takeCommand()
        if ans == "yes":
            pywhatkit.search("ubiquitous binary search algorithm")
        elif ans == "no":
            speakAlgo("ok,no  problem")
        else:
            speakAlgo("Sorry,I can't recognize your answer properly")

    elif "algoAStarSearch" in tag:
        speakAlgo(
            "A star Search algorithm is one of the best and popular technique used in path-finding and graph traversals")
        speakAlgo("do you want to know more about A star Search ?")
        speakAlgo("please say yes or no")
        ans = takeCommand()
        if ans == "yes":
            pywhatkit.search("A star search algorithm")
        elif ans == "no":
            speakAlgo("ok,no  problem")
        else:
            speakAlgo("Sorry,I can't recognize your answer properly")

    elif "algoBreadtheFirstSearch" in tag:
        speakAlgo(
            "BFS and its application in finding connected components of graphs were invented in 1945 by Konrad Zuse")
        speakAlgo("do you want to know more about breadthe first Search ?")
        speakAlgo("please say yes or no")
        ans = takeCommand()
        if ans == "yes":
            pywhatkit.search("breadthe first search algorithm")
        elif ans == "no":
            speakAlgo("ok,no  problem")
        else:
            speakAlgo("Sorry,I can't recognize your answer properly")

    elif "algoDepthFirstSearch" in tag:
        speakAlgo(
            "A version of depth-first search was investigated in the 19th century by French mathematician Charles Pierre Trémaux")
        speakAlgo("do you want to know more about depth first Search ?")
        speakAlgo("please say yes or no")
        ans = takeCommand()
        if ans == "yes":
            pywhatkit.search("depth first search algorithm")
        elif ans == "no":
            speakAlgo("ok,no  problem")
        else:
            speakAlgo("Sorry,I can't recognize your answer properly")

    # sorting algorithms ---->

    elif "algoBubbleSort" in tag:
        speakAlgo(
            "Bubble Sort is the simplest sorting algorithm that works by repeatedly swapping the adjacent elements if they are in wrong order")
        speakAlgo("do you want to know more about bubble sort ?")
        speakAlgo("please say yes or no")
        ans = takeCommand()
        if ans == "yes":
            pywhatkit.search("bubble sort algorithm")
        elif ans == "no":
            speakAlgo("ok,no  problem")
        else:
            speakAlgo("Sorry,I can't recognize your answer properly")

    elif "algoSelectionSort" in tag:
        speakAlgo(
            "The selection sort algorithm sorts an array by repeatedly finding the minimum element considering ascending order from unsorted part and putting it at the beginning")
        speakAlgo("do you want to know more about selection sort ?")
        speakAlgo("please say yes or no")
        ans = takeCommand()
        if ans == "yes":
            pywhatkit.search("selection sort algorithm")
        elif ans == "no":
            speakAlgo("ok,no  problem")
        else:
            speakAlgo("Sorry,I can't recognize your answer properly")

    elif "algoQuickSort" in tag:
        speakAlgo(
            "Quick sort is a highly efficient sorting algorithm and is based on partitioning of array of data into smaller arrays")
        speakAlgo("do you want to know more about quick sort ?")
        speakAlgo("please say yes or no")
        ans = takeCommand()
        if ans == "yes":
            pywhatkit.search("quick sort algorithm")
        elif ans == "no":
            speakAlgo("ok,no  problem")
        else:
            speakAlgo("Sorry,I can't recognize your answer properly")

    elif "algoInsertionSort" in tag:
        speakAlgo(
            "This is an in-place comparison-based sorting algorithm. Here, a sub-list is maintained which is always sorted")
        speakAlgo("do you want to know more about insertion sort ?")
        speakAlgo("please say yes or no")
        ans = takeCommand()
        if ans == "yes":
            pywhatkit.search("insertion sort algorithm")
        elif ans == "no":
            speakAlgo("ok,no  problem")
        else:
            speakAlgo("Sorry,I can't recognize your answer properly")

    elif "algoMergeSort" in tag:
        speakAlgo("Merge Sort is a Divide and Conquer algorithm")
        speakAlgo("do you want to know more about merge sort ?")
        speakAlgo("please say yes or no")
        ans = takeCommand()
        if ans == "yes":
            pywhatkit.search("merge sort algorithm")
        elif ans == "no":
            speakAlgo("ok,no  problem")
        else:
            speakAlgo("Sorry,I can't recognize your answer properly")

    elif "algoHeapSort" in tag:
        speakAlgo(
            "Heap sort works by visualizing the elements of the array as a special kind of complete binary tree called a heap")
        speakAlgo("do you want to know more about heap sort ?")
        speakAlgo("please say yes or no")
        ans = takeCommand()
        if ans == "yes":
            pywhatkit.search("heap sort algorithm")
        elif ans == "no":
            speakAlgo("ok,no  problem")
        else:
            speakAlgo("Sorry,I can't recognize your answer properly")

    elif "algoCountingSort" in tag:
        speakAlgo(
            "Counting sort is a sorting technique based on keys between a specific range. It works by counting the number of objects having distinct key values (kind of hashing). Then doing some arithmetic to calculate the position of each object in the output sequence")
        speakAlgo("do you want to know more about counting sort ?")
        speakAlgo("please say yes or no")
        ans = takeCommand()
        if ans == "yes":
            pywhatkit.search("counting sort algorithm")
        elif ans == "no":
            speakAlgo("ok,no  problem")
        else:
            speakAlgo("Sorry,I can't recognize your answer properly")

    elif "algoRadixSort" in tag:
        speakAlgo(
            "The idea of Radix Sort is to do digit by digit sort starting from least significant digit to most significant digit. Radix sort uses counting sort as a subroutine to sort")
        speakAlgo("do you want to know more about radix sort ?")
        speakAlgo("please say yes or no")
        ans = takeCommand()
        if ans == "yes":
            pywhatkit.search("radix sort algorithm")
        elif ans == "no":
            speakAlgo("ok,no  problem")
        else:
            speakAlgo("Sorry,I can't recognize your answer properly")

    elif "algoBucketSort" in tag:
        speakAlgo(
            "Bucket Sort is a sorting technique that sorts the elements by first dividing the elements into several groups called buckets. The elements inside each bucket are sorted using any of the suitable sorting algorithms or recursively calling the same algorithm.")
        speakAlgo("do you want to know more about bucket sort ?")
        speakAlgo("please say yes or no")
        ans = takeCommand()
        if ans == "yes":
            pywhatkit.search("bucket sort algorithm")
        elif ans == "no":
            speakAlgo("ok,no  problem")
        else:
            speakAlgo("Sorry,I can't recognize your answer properly")

    elif "algoCombSort" in tag:
        speakAlgo(
            "The basic idea of comb sort and the bubble sort is same. In other words, comb sort is an improvement on the bubble sort")
        speakAlgo("do you want to know more about comb sort ?")
        speakAlgo("please say yes or no")
        ans = takeCommand()
        if ans == "yes":
            pywhatkit.search("comb sort algorithm")
        elif ans == "no":
            speakAlgo("ok,no  problem")
        else:
            speakAlgo("Sorry,I can't recognize your answer properly")

    elif "algoTimSort" in tag:
        speakAlgo(
            "Tim-sort is a sorting algorithm derived from insertion sort and merge sort. It was designed to perform in an optimal way on different kind of real world data")
        speakAlgo("do you want to know more about Tim sort ?")
        speakAlgo("please say yes or no")
        ans = takeCommand()
        if ans == "yes":
            pywhatkit.search("Tim sort algorithm")
        elif ans == "no":
            speakAlgo("ok,no  problem")
        else:
            speakAlgo("Sorry,I can't recognize your answer properly")

    elif "algoCycleSort" in tag:
        speakAlgo(
            "Cycle sort is a comparison sorting algorithm which forces array to be factored into the number of cycles where each of them can be rotated to produce a sorted array. It is theoretically optimal in the sense that it reduces the number of writes to the original array")
        speakAlgo("do you want to know more about cycle sort ?")
        speakAlgo("please say yes or no")
        ans = takeCommand()
        if ans == "yes":
            pywhatkit.search("cycle sort algorithm")
        elif ans == "no":
            speakAlgo("ok,no  problem")
        else:
            speakAlgo("Sorry,I can't recognize your answer properly")

    elif "algoBitonicSort" in tag:
        speakAlgo("Bitonic Sort is a classic parallel algorithm for sorting")
        speakAlgo("do you want to know more about Bitonic sort ?")
        speakAlgo("please say yes or no")
        ans = takeCommand()
        if ans == "yes":
            pywhatkit.search("Bitonic sort algorithm")
        elif ans == "no":
            speakAlgo("ok,no  problem")
        else:
            speakAlgo("Sorry,I can't recognize your answer properly")

    elif "algoSleepSort" in tag:
        speakAlgo(
            "sleep sort works by starting a separate task for each item to be sorted, where each task sleeps for an interval corresponding to the item's sort key, then emits the item. Items are then collected sequentially in time")
        speakAlgo("do you want to know more about Sleep sort ?")
        speakAlgo("please say yes or no")
        ans = takeCommand()
        if ans == "yes":
            pywhatkit.search("Sleep sort algorithm")
        elif ans == "no":
            speakAlgo("ok,no  problem")
        else:
            speakAlgo("Sorry,I can't recognize your answer properly")

    elif "algoCoctailSort" in tag:
        speakAlgo(
            "Cocktail Sort is a variation of Bubble sort. The Bubble sort algorithm always traverses elements from left and moves the largest element to its correct position in first iteration and second largest in second iteration and so on")
        speakAlgo("do you want to know more about coctail sort ?")
        speakAlgo("please say yes or no")
        ans = takeCommand()
        if ans == "yes":
            pywhatkit.search("coctail sort algorithm")
        elif ans == "no":
            speakAlgo("ok,no  problem")
        else:
            speakAlgo("Sorry,I can't recognize your answer properly")

    elif "algoStrandSort" in tag:
        speakAlgo(
            "Strand sort is a recursive sorting algorithm that sorts items of a list into increasing order. It has order of n square worst time complexity which occurs when the input list is reverse sorted")
        speakAlgo("do you want to know more about Strand sort ?")
        speakAlgo("please say yes or no")
        ans = takeCommand()
        if ans == "yes":
            pywhatkit.search("Strand sort algorithm")
        elif ans == "no":
            speakAlgo("ok,no  problem")
        else:
            speakAlgo("Sorry,I can't recognize your answer properly")

    elif "algoShellSort" in tag:
        speakAlgo(
            "Shell sort is an algorithm that first sorts the elements far apart from each other and successively reduces the interval between the elements to be sorted. It is a generalized version of insertion sort")
        speakAlgo("do you want to know more about Shell sort ?")
        speakAlgo("please say yes or no")
        ans = takeCommand()
        if ans == "yes":
            pywhatkit.search("Shell sort algorithm")
        elif ans == "no":
            speakAlgo("ok,no  problem")
        else:
            speakAlgo("Sorry,I can't recognize your answer properly")

    elif "algoTreeSort" in tag:
        speakAlgo(
            "Tree sort is a sort algorithm that builds a binary search tree from the elements to be sorted, and then traverses the tree in-order so that the elements come out in sorted order")
        speakAlgo("do you want to know more about Tree sort ?")
        speakAlgo("please say yes or no")
        ans = takeCommand()
        if ans == "yes":
            pywhatkit.search("Tree sort algorithm")
        elif ans == "no":
            speakAlgo("ok,no  problem")
        else:
            speakAlgo("Sorry,I can't recognize your answer properly")

    elif "algoPermutationSort" in tag:
        speakAlgo(
            "BogoSort also known as permutation sort, stupid sort, slow sort, shotgun sort or monkey sort is a particularly ineffective algorithm based on generate and test paradigm. The algorithm successively generates permutations of its input until it finds one that is sorted")
        speakAlgo("do you want to know more about Permutation sort ?")
        speakAlgo("please say yes or no")
        ans = takeCommand()
        if ans == "yes":
            pywhatkit.search("Permutation sort algorithm")
        elif ans == "no":
            speakAlgo("ok,no  problem")
        else:
            speakAlgo("Sorry,I can't recognize your answer properly")

    elif "algoPancakeSort" in tag:
        speakAlgo(
            "Pancake sort is called so because it resembles sorting pancakes on a plate with a spatula, where you can only use the spatula to flip some of the top pancakes in the plate")
        speakAlgo("do you want to know more about Pancake sort ?")
        speakAlgo("please say yes or no")
        ans = takeCommand()
        if ans == "yes":
            pywhatkit.search("Pancake sort algorithm")
        elif ans == "no":
            speakAlgo("ok,no  problem")
        else:
            speakAlgo("Sorry,I can't recognize your answer properly")

    elif "algoGnomeSort" in tag:
        speakAlgo(
            "Gnome Sort also called Stupid sort is based on the concept of a Garden Gnome sorting his flower pots")
        speakAlgo("do you want to know more about Gnome sort ?")
        speakAlgo("please say yes or no")
        ans = takeCommand()
        if ans == "yes":
            pywhatkit.search("Gnome sort algorithm")
        elif ans == "no":
            speakAlgo("ok,no  problem")
        else:
            speakAlgo("Sorry,I can't recognize your answer properly")

    elif "algoBrickSort" in tag:
        speakAlgo(
            "In computing, an odd even sort or odd even transposition sort also known as brick sort or parity sort is a relatively simple sorting algorithm, developed originally for use on parallel processors with local interconnections")
        speakAlgo("do you want to know more about Brick sort ?")
        speakAlgo("please say yes or no")
        ans = takeCommand()
        if ans == "yes":
            pywhatkit.search("Brick sort algorithm")
        elif ans == "no":
            speakAlgo("ok,no  problem")
        else:
            speakAlgo("Sorry,I can't recognize your answer properly")

    elif "algoPegionholeSort" in tag:
        speakAlgo(
            "Pegionhole sort is similar to counting sort, but differs in that it “moves items twice: once to the bucket array and again to the final destination")
        speakAlgo("do you want to know more about Pegionhole sort ?")
        speakAlgo("please say yes or no")
        ans = takeCommand()
        if ans == "yes":
            pywhatkit.search("Pegionhole sort algorithm")
        elif ans == "no":
            speakAlgo("ok,no  problem")
        else:
            speakAlgo("Sorry,I can't recognize your answer properly")










