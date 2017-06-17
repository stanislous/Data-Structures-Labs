import time
start_time = time.time()
array = list(map(int, input("Enter elements in array: ").split(' ')))
for i in range(1,len(array)):
    for j in range(len(array)-i):
        if array[j] > array[j+1]:
            array[j], array[j+1] = array[j+1], array[j]
print(array)
print("Execution time: %s" % (time.time() - start_time))