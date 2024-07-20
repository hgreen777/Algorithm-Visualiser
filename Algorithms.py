import random

def bubbleSort(arr, update_visual_callback, quit_call):
    n = len(arr) 
    comparisons = 0
    array_accesses = 0
    for i in range(n):
        swapped = False
        for j in range (0, n-i-1):
            if quit_call():
                print("Stopping Algorithm")
                return

            comparisons += 1
            array_accesses += 2
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1],arr[j]
                swapped = True
                array_accesses += 4
                update_visual_callback(arr,j+1,[comparisons,array_accesses])
        if swapped == False:
            print("Algorithm Completed")
            break

def linearSearch(arr, update_visual_callback, quit_call):
    comparisons = 0
    array_accesses = 0
    searchValue = random.randint(1, len(arr))
    print(f"looking for: {searchValue}")
    for i in range(len(arr)):
        if quit_call():
                print("Stopping Algorithm")
                return
        
        array_accesses += 1
        comparisons += 1

        update_visual_callback(arr,i,[comparisons,array_accesses])
        if arr[i] == searchValue:
            print("Element Found")
            return
    
    print("Error: Element not in array")
    return

def binarySearch(arr, update_visual_callback, quit_call):
    comparisons = 0
    array_accesses = 0
    search_value = random.randint(1, len(arr))
    print(f"Lookign for: {search_value}")
    L = 0
    R = len(arr) - 1

    while L <= R:
        if quit_call():
            print("Stopping Algorithm")
            return
        
        middle = int((L+R) / 2)
        comparisons += 1
        array_accesses += 2

        update_visual_callback(arr, middle,[comparisons,array_accesses])
        if arr[middle] > search_value:
            R = middle - 1
        elif arr[middle] < search_value:
            L = middle + 1
        else:
            print("Element Found")
            return
        



