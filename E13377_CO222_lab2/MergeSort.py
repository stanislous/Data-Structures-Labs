import time
start_time = time.time()

def Mergesort(S):
    Mergesort2(S, 0, len(S) - 1)

def Mergesort2(S, first, last):
    if first < last:
        middle = (first + last) // 2
        Mergesort2(S, first, middle)
        Mergesort2(S, middle+1, last)
        Merge(S, first, middle, last)

def Merge(S, first, middle, last):
    temp = S[first:last+1]   # temporary array to store the merged array
    pos = 0
    lpos = first
    rpos = middle + 1

    #until lpos < mid and rpos < right
    while (lpos <= middle and rpos <= last):
        if S[lpos] < S[rpos]:
            temp[pos] = S[lpos]
            pos += 1
            lpos += 1
        else:
            temp[pos] = S[rpos]
            pos += 1
            rpos += 1

    #until (lpos <= mid)
    while lpos <= middle:
        temp[pos] = S[lpos]
        pos += 1
        lpos += 1

    #until (rpos <= right)
    while rpos <= last:
        temp[pos] = S[rpos]
        pos += 1
        rpos += 1

    #copy back the sorted array to the original array
    for counter in range(pos):
        S[counter + first] = temp[counter]

S = list(map(int, input("Enter elements in array: ").split(' ')))
Mergesort(S)
print("Execution time: %s" % (time.time() - start_time))
print(S)