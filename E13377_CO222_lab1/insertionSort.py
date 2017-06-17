import time
start_time = time.time()
array = list(map(int, input("Enter elements in array: ").split(' ')))
for i in range(1,len(array)):
    temp = array[i]
    index = i
    while index > 0 and array[index-1] > temp:
        array[index] = array[index - 1]
        index = index - 1
    array[index] = temp
print(array)
print("Execution time: %s" % (time.time() - start_time))