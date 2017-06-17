import time
start_time = time.time()
array = list(map(int, input("Enter elements in array: ").split(' ')))
for i in range(len(array)-1):
    Max = -10000000
    for j in range(len(array)-i):
        if Max <= array[j]:
            Max = array[j]
            index = j
    array[index], array[len(array)-i-1] = array[len(array)-i-1], array[index]
print(array)
print("Execution time: %s" % (time.time() - start_time))