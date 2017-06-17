import sys
import time

sys.setrecursionlimit(2000)            #recursive limitation brings up to 2000
start_time = time.time()                #Time Measuring starts

def QuickSort(S):
    QuickSort2(S, 0, len(S)-1)          #call to Quicksort2 function

def QuickSort2(S, start, end):
    if start < end:                     #if start >= end means considered parts of the array are sorted
        PivotIndex = Partition(S, start, end)
        QuickSort2(S, start, PivotIndex - 1)
        QuickSort2(S, PivotIndex + 1, end)

def Partition(S, start, end):

    #Here i select a border, that is act as the pivot. Then going through the array and compare weather the edge value is less
    #greater than the considered value of array. After going through all the elements in the array, edge value and pivot
    #swaps.

    pivotIndex = start          #For this I choose start index as the pivot
    pivotValue = S[pivotIndex]
    S[pivotIndex], S[start] = S[end], S[pivotIndex]
    edge = start

    for i in range(start, end + 1):
        if S[i] < pivotValue:
            edge += 1
            S[i], S[edge] = S[edge], S[i]
    S[start], S[edge] = S[edge], S[start]
    return edge

S = list(map(int, input("Enter elements in array: ").split(' ')))
QuickSort(S)
print("Execution time: %s" % (time.time() - start_time))
print(S)
